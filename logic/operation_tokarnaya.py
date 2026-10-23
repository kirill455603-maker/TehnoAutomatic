# logic/operation_tokarnaya.py
from logic.instrument_manager import InstrumentManager
from logic.automation import TechnoproAutomation
from logic.operation_base import OperationBase
from logic import constants


class Tokarnaya(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/image_find/tok_find.PNG'

        self.instrument_manager = InstrumentManager()

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    # ================= БИЗНЕС-ЛОГИКА =================
    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def start_obrabotki(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter_zag = d['диаметр заготовки']
        diameter_yst = self.format_num(d['диаметр установки'])
        patron = self.instrument_manager.get_patron(diameter_zag)
        if d['статус чек']:
            text = f'Установить за {str(diameter_yst).replace('.', ',')}, выверить'
            if d['биение торцевое'] > 0 and d['биение радиальное'] > 0:
                instrument_1 = self.instrument_manager.add('СИ Индикатор ИРТ ГОСТ 5584-75')
                instrument_2 = self.instrument_manager.add('СИ Индикатор ИРБ ГОСТ 5584-75')
                result['инструмент'].append(instrument_1)
                result['инструмент'].append(instrument_2)
                text += f' радильное биение {str(d['биение радиальное']).replace('.', ',')} и торцевое биение {str(d['биение торцевое']).replace('.', ',')}'
            elif d['биение радиальное'] > 0:
                instrument = self.instrument_manager.add('СИ Индикатор ИРБ ГОСТ 5584-75')
                result['инструмент'].append(instrument)
                text += f' радильное биение {str(d['биение радиальное']).replace('.', ',')}'
            elif d['биение торцевое'] > 0:
                instrument = self.instrument_manager.add('СИ Индикатор ИРТ ГОСТ 5584-75')
                result['инструмент'].append(instrument)
                text += f' торцевое биение {str(d['биение торцевое']).replace('.', ',')}'

            if d['по базе']:
                if len(d['по базе']) < 2:
                    text += f' относительно базы {d['по базе']}'
                else:
                    text += f' относительно баз {self.counter_base(d['по базе'])}'
            else:
                text += f' относительно диаметра {str(self.format_num(d['по диаметру'])).replace('.', ',')}'
            text += f', закрепить, снять после обработки'
        else:
            text = f'Установить за {str(diameter_yst).replace('.', ',')}, закрепить, снять после обработки'
        result['описание'] = text

        if patron:
            result['инструмент'].append(patron)
        return result

    def podrezka(self, d) -> dict:
        result = {'описание': '', 'инструмент': []}

        rezets = self.instrument_manager.add('РИ Резец 32x25 2112-0017 ВК8 ГОСТ 18880-73')
        if rezets: result['инструмент'].append(rezets)

        text = 'Подрезать торец'
        if d['длина']:
            text += f', контролировать L={str(self.format_num(d['длина'])).replace('.', ',')}'

            if d['квалитет']: text += d['квалитет'].strip()
            if d['допуск_1']: text += f' {self.format_dopusk(d["допуск_1"])}'
            if d['допуск_2']: text += f' {self.format_dopusk(d["допуск_2"])}'
            shtangel = self.instrument_manager.get_shtangencirkul(d['длина'])
            if shtangel: result['инструмент'].append(shtangel)
        else:
            text += ' как чисто'
        if d['шероховатость']:
            text += f', контролировать шероховатость поверхности Ra {str(d['шероховатость']).replace('.', ',')}'
            i = self.instrument_manager.add('СИ Набор образцов шероховатости 0,8-12,5 Т ГОСТ 9378-93')
            if i: result['инструмент'].append(i)
        result['описание'] = text
        return result

    def tochenie(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        rezets = self.instrument_manager.add('РИ Резец 12x12 2100-0559 ГОСТ 18869-73')
        if rezets: result['инструмент'].append(rezets)

        diameter_str = str(self.format_num(d['диаметр'])).replace('.', ',')
        text = f'Точить {diameter_str}'

        if d['квалитет_д']:
            text += d['квалитет_д'].strip()

        # Подбор измерительного инструмента
        instr = self.find_shtangel_for_precision(d['диаметр'], d['квалитет_д'], d['допуск_д_1'], d['допуск_д_2'])
        if instr: result['инструмент'].append(instr)

        # Допуски диаметра
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d["допуск_д_1"])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d["допуск_д_2"])}'

        # Длина
        if d['длина']:
            length_str = str(self.format_num(d['длина'])).replace('.', ',')
            text += f' на L={length_str}'

            if d['квалитет_дл']: text += d['квалитет_дл'].strip()
            if d['допуск_дл_1']: text += f' {self.format_dopusk(d["допуск_дл_1"])}'
            if d['допуск_дл_2']: text += f' {self.format_dopusk(d["допуск_дл_2"])}'

            shtangel = self.instrument_manager.get_shtangencirkul(d['длина'])
            if shtangel: result['инструмент'].append(shtangel)
        else:
            text += ' до кулачков'

        if d['шероховатость'] or d['шероховатость_торцевая']:
            if d['шероховатость'] != 0:
                text += f', контролировать шероховатость радиальной поверхности Ra {str(d["шероховатость"]).replace('.', ',')}'
            if d['шероховатость_торцевая'] != 0:
                text += f', контролировать шероховатость торцевой поверхности Ra {str(d["шероховатость_торцевая"]).replace('.', ',')}'
            nabor_sh = self.instrument_manager.add('СИ Набор образцов шероховатости 0,8-12,5 Т ГОСТ 9378-93')
            if nabor_sh: result['инструмент'].append(nabor_sh)

        if d['биение_радиальное'] or d['биение_торцевое']:
            if d['биение_радиальное']:
                text += f', контролировать радиальное биение со значением {str(d["биение_радиальное"]).replace('.', ',')}'
                if d['база_радиальная']:
                    if len(d['база_радиальная']) < 2:
                        text += f' относительно базы {d['база_радиальная']}'
                    else:
                        text += f' относительно баз {self.counter_base(d['база_радиальная'])}'
                indicator = 'СИ Индикатор ИРБ ГОСТ 5584-75'
                ind = self.instrument_manager.add(indicator)
                if ind: result['инструмент'].append(ind)
            if d['биение_торцевое']:
                text += f', контролировать торцевое биение со значением {str(d["биение_торцевое"]).replace('.', ',')}'
                if d['база_торцевая']:
                    if len(d['база_торцевая']) < 2:
                        text += f' относительно базы {d['база_торцевая']}'
                    else:
                        text += f' относительно баз {self.counter_base(d['база_торцевая'])}'
                indicator = 'СИ Индикатор ИРТ ГОСТ 5584-75'
                ind = self.instrument_manager.add(indicator)
                if ind: result['инструмент'].append(ind)

        result['описание'] = text
        return result

    def rastachivanie(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        rezets = self.instrument_manager.add('РИ Резец 16х16 2140-0504 ГОСТ 18872-73')
        if rezets: result['инструмент'].append(rezets)

        diameter_str = str(self.format_num(d['диаметр'])).replace('.', ',')
        text = f'Расточить {diameter_str}'

        if d['квалитет_д']:
            text += d['квалитет_д'].strip()

        # Подбор Нутромера/Микрометра
        is_h7_h8 = d['квалитет_д'] in ('h7', 'h8')
        is_tight_dopusk = (0.01 <= abs(d['допуск_д_1']) <= 0.1) or (0.01 <= abs(d['допуск_д_2']) <= 0.1)

        if is_h7_h8 or is_tight_dopusk:
            instr = self.instrument_manager.get_nutromer(d['диаметр'])
        else:
            instr = self.instrument_manager.get_shtangencirkul(d['диаметр'])
        if instr: result['инструмент'].append(instr)

        if d['допуск_д_1']: text += f' {self.format_dopusk(d["допуск_д_1"])}'
        if d['допуск_д_2']: text += f' {self.format_dopusk(d["допуск_д_2"])}'

        if d['длина']:
            length_str = str(self.format_num(d['длина'])).replace('.', ',')
            text += f' на L={length_str}'

            if d['квалитет_дл']: text += d['квалитет_дл']
            if d['допуск_дл_1']: text += f' {self.format_dopusk(d["допуск_дл_1"])}'
            if d['допуск_дл_2']: text+= f' {self.format_dopusk(d["допуск_дл_2"])}'

            shtangel = self.instrument_manager.get_shtangencirkul(d['длина'])
            if shtangel: result['инструмент'].append(shtangel)
        else:
            text += ' напроход'

        if d['шероховатость'] or d['шероховатость_торцевая']:
            if d['шероховатость']:
                text += f', контролировать шероховатость радиальной поверхности Ra {str(d["шероховатость"]).replace('.', ',')}'

            if d['шероховатость_торцевая']:
                text += f', контролировать шероховатость торцевой поверхности Ra {str(d["шероховатость_торцевая"]).replace('.', ',')}'

            nabor_sh = self.instrument_manager.add('СИ Набор образцов шероховатости 0,8-12,5 Т ГОСТ 9378-93')
            if nabor_sh: result['инструмент'].append(nabor_sh)

        #Текст биения
        if d['биение_радиальное'] or d['биение_торцевое']:
            if d['биение_радиальное']:
                text += f', контролировать радиальное биение со значением {str(d["биение_радиальное"]).replace('.', ',')}'
                if d['база_радиальная']:
                    if len(d['база_радиальная']) < 2:
                        text += f' относительно базы {d['база_радиальная']}'
                    else:
                        text += f' относительно баз {self.counter_base(d['база_радиальная'])}'
                indicator = 'СИ Индикатор ИРБ ГОСТ 5584-75'
                ind = self.instrument_manager.add(indicator)
                if ind: result['инструмент'].append(ind)
            if d['биение_торцевое']:
                text += f', контролировать торцевое биение со значением {str(d["биение_торцевое"]).replace('.', ',')}'
                if d['база_торцевая']:
                    if len(d['база_торцевая']) < 2:
                        text += f' относительно базы {d['база_торцевая']}'
                    else:
                        text += f' относительно баз {self.counter_base(d['база_торцевая'])}'
                indicator = 'СИ Индикатор ИРТ ГОСТ 5584-75'
                ind = self.instrument_manager.add(indicator)
                if ind: result['инструмент'].append(ind)


        result['описание'] = text
        return result

    def sverlenie(self, diameter: float, length: float) -> dict:
        new_diameter = self.format_num(diameter)
        new_length = self.format_num(length)

        text = f'Сверлить сквозное отверстие {str(new_diameter).replace('.', ',')}' if length == 0 else f'Сверлить отверстие {str(new_diameter).replace('.', ',')} на L={str(new_length).replace('.', ',')}'

        result = {'описание': text, 'инструмент': []}
        sverlo = self.instrument_manager.add(self.dict_sverla[diameter])
        if sverlo: result['инструмент'].append(sverlo)
        return result

    def rezba(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        rezets = self.instrument_manager.add('РИ Резец 16x10 2660-0501 0,5-2,5 ГОСТ 18876-73')
        if rezets: result['инструмент'].append(rezets)

        length = self.format_num(d['длина'])
        type_txt = 'внутреннюю' if d['расположение'] == 'внутренняя' else 'наружную'
        curs_txt = 'правым' if d['направление'] == 'правым' else 'левым'

        text = f'Нарезать {type_txt} резьбу {d["диаметр"]} с {curs_txt} направлением витков на L={str(length).replace('.', ',')} с шагом {d["шаг"]} и допуском {d["допуск"]}'
        result['описание'] = text
        if d['расположение'] == 'внешняя':
            i = self.instrument_manager.get_kolco_rezba(float(d['диаметр'][1:]), float(d['шаг']))
            if i:
                result['инструмент'].append(i)
                i = self.instrument_manager.get_kolco_rezba_neprohod(float(d['диаметр'][1:]), float(d['шаг']))
                if i:
                    result['инструмент'].append(i)
            else:
                i = self.instrument_manager.get_mikrometer_with_rezba(float(d['диаметр'][1:]))
                if i:
                    result['инструмент'].append(i)
        elif d['расположение'] == 'внутренняя':
            i = self.instrument_manager.get_probka_rezba(float(d['диаметр'][1:]), float(d['шаг']))
            if i:
                result['инструмент'].append(i)
        return result

    def faska(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        length = self.format_num(d['длина'])

        text = 'Точить' if d['расположение'] == 'внешняя' else 'Расточить'
        count = d['количество']
        if count == 1:
            text += f' фаску {str(length).replace('.', ',')}х{d["угол"]}'
        elif count < 5:
            text += f' {count} фаски {str(length).replace('.', ',')}х{d["угол"]}'
        else:
            text += f' {count} фасок {str(length).replace('.', ',')}х{d["угол"]}'
        result['описание'] = text

        rezets = 'РИ Резец 16х16 2140-0504 ГОСТ 18872-73' if d['расположение'] == 'внутренняя' else 'РИ Резец 12x12 2100-0559 ГОСТ 18869-73'
        r = self.instrument_manager.add(rezets)
        if r: result['инструмент'].append(r)

        # Исправлена ошибка оригинала: было <=, стало >=
        shtangel = self.instrument_manager.get_shtangencirkul(d['длина'])
        if shtangel: result['инструмент'].append(shtangel)

        yglomer = self.instrument_manager.add('СИ Угломер типа 1 ГОСТ 5378-88')
        if yglomer: result['инструмент'].append(yglomer)

        return result

    def angle(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        uglo = self.instrument_manager.add('СИ Угломер типа 1 ГОСТ 5378-88')
        if uglo: result['инструмент'].append(uglo)

        start = self.format_num(d['старт'])
        end = self.format_num(d['конец'])

        text = 'Точить' if d['расположение'] == 'внешний' else 'Расточить'
        text += f' угол {d["угол"]}'

        if d['допуск'] > 0:
            text += f'{d["допуск"]}'

        if start > 0 and end > 0:
            text += f' от {str(start).replace('.', ',')} до {str(end).replace('.', ',')}'
        elif start == 0 and end > 0:
            text += f' до {str(end).replace('.', ',')}'
        elif start > 0 and end == 0:
            text += f' от {str(start).replace('.', ',')}'

        result['описание'] = text
        return result

    # ================= ВСПОМОГАТЕЛЬНЫЕ =================
    def find_shtangel_for_precision(self, diameter: float, kvalitet: str, dopusk1: float,
                                     dopusk2: float) -> str | None:
        """Универсальная логика подбора Микрометра/Штангенциркуля для токарной/расточной."""
        is_h6_h7_h8 = kvalitet in ('h6', 'h7', 'h8')
        is_H6_H7_H8 = kvalitet in ('H6', 'H7', 'H8')
        is_tight_dopusk = (0.01 <= (abs(dopusk1) != 0) <= 0.1) or (0.01 <= (abs(dopusk2) != 0) <= 0.1)

        if is_h6_h7_h8 or is_tight_dopusk:
            return self.instrument_manager.get_mikrometer(diameter)
        if is_H6_H7_H8 or is_tight_dopusk:
            return self.instrument_manager.get_nutromer(diameter)
        return self.instrument_manager.get_shtangencirkul(diameter)

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

