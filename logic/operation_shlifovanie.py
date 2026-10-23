from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager

class OperationShlifovanie(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/find_operations/shlif_find.PNG'
        self.instrument_manager = InstrumentManager()

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

    def start_center(self, d):
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['зажим'])
        vistavlenie = self.format_num(d['выставление'])
        d_shlif = self.format_num(d['диаметр шлифовки'])
        text = (f'Установить деталь в передний и задний центры станка, зажим выполнить за поверхность {str(diameter).replace('.', ',')}.\n'
                f'Выставить деталь по поверхности {str(vistavlenie).replace('.', ',')} относительно оси центров с радиальным биением не более 0,01 мм, контроль выполнить индикатором часового типа.\n'
                f'Закрепите деталь, убедитесь в надежности передачи крутящего момента и отсутстсвии осевого заклинивания.\n'
                f'Проверьте радиальное биение шлифуемой поверхности {str(d_shlif).replace('.', ',')}, биение не более {str(self.format_dopusk(d['биение']))} мм.')
        result['описание'] = text

        indicator = 'СИ Индикатор ИРБ ГОСТ 5584-75'
        ind = self.instrument_manager.add(indicator)
        if ind: result['инструмент'].append(ind)

        patron = self.instrument_manager.add('ПР Патрон 6152-0173 ГОСТ 13334-67')
        if patron: result['инструмент'].append(patron)

        center = self.instrument_manager.add('ПР Центр 7032-0113 -Морзе5 ПТ ГОСТ 2575-79')
        if center: result['инструмент'].append(center)
        return result

    def start_patron(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['зажим'])
        length = self.format_num(d['длина зажима'])
        shlif = self.format_num(d['диаметр шлифовки'])
        vist = self.format_num(d['выставление'])
        bienie = self.format_dopusk(d['биение'])

        text = (f'Установите деталь в трёхкулачковый патрон, зажим выполнить за наружную поверхность {str(diameter).replace('.', ',')} на длину {str(length).replace('.', ',')} мм.\n'
                f'Выставьте деталь по наружной поверхности {str(vist).replace('.', ',')} с радиальный биением не более 0,01 мм и по торцу с торцевым биением не более 0,01 мм.\n'
                f'Закрепите деталь, обеспечив усилие зажима, исключающее деформацию тонкостенной стенки.\n'
                f'Проверьте биение обрабатываемого отверстия {str(shlif).replace('.', ',')} относительно оси шпинделя не более {bienie} мм.')

        result['описание'] = text

        indicator = 'СИ Индикатор ИРБ ГОСТ 5584-75'
        ind = self.instrument_manager.add(indicator)
        if ind: result['инструмент'].append(ind)

        indicator_2 = 'СИ Индикатор ИРТ ГОСТ 5584-75'
        ind_2 = self.instrument_manager.add(indicator_2)
        if ind_2: result['инструмент'].append(ind_2)

        patron = self.instrument_manager.get_patron(diameter)
        if patron: result['инструмент'].append(patron)

        return result

    def start_opravka(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['установочное отверстие'])

        text = f'Установите оправку'
        if d['оправка']:
            text += f' {d['оправка']}'
        else:
            text += ' цеховую'

        text += (f' в патрон станка, проверьте биение установочных поверхностей оправки: не более 0,005 мм.\n'
                 f'Установите деталь на оправку за отверстие {str(diameter).replace('.', ',')}, фиксацию выполните гайкой.\n'
                 f'Выставьте деталь по опорному торцу оправки, биение шлифуемой поверхности не более 0,005 мм.\n'
                 f'Закрепите деталь на оправке, исключив перекос и замятие кромки отверстия.')

        result['описание'] = text

        indicator = 'СИ Индикатор ИРБ ГОСТ 5584-75'
        ind = self.instrument_manager.add(indicator)
        if ind: result['инструмент'].append(ind)

        indicator_2 = 'СИ Индикатор ИРТ ГОСТ 5584-75'
        ind_2 = self.instrument_manager.add(indicator_2)
        if ind_2: result['инструмент'].append(ind_2)


        if not d['оправка']:
            opravka = self.instrument_manager.add('ПР Оправка  цеховая')
            if opravka: result['инструмент'].append(opravka)


        return result

    def osnovnoe_step_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])

        text = f'Выполнить черновое круговое продольное шлифование поверхности {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += f' на L={str(length).replace('.', ',')}'
        if d['квалитет_длина']:
            text += d['квалитет_диаметер']
        if d['допуск_дл_1']:
            text += f' {self.format_dopusk(d['допуск_дл_1'])}'
        if d['допуск_дл_2']:
            text += f' {self.format_dopusk(d['допуск_дл_2'])}'
        text += ', снять 0,3 мм. на диаметр и оставив 0,1 мм. на диаметр на чистовое шлифование.'
        result['описание'] = text

        circle = self.instrument_manager.add('РИ Круг 1 600x80x305 25A F40 К 6 V 35 м/с А 1 кл. ГОСТ Р 52781-2007')
        if circle: result['инструмент'].append(circle)

        return result

    def osnovnoe_step_2(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        text = (f'Остановить вращение детали, отвести шлифовальный круг от поверхности.\n'
                f'Измерить промежуточный размер {str(diameter + 0.1).replace('.', ',')}, проверив диаметр в двух сечениях и в двух взаимно перпендекулярных направлениях.\n')
        result['описание'] = text

        inst = self.instrument_manager.get_mikrometer(diameter)
        if inst:
            result['инструмент'].append(inst)

        return result

    def osnovnoe_step_3(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])

        text = f'Выполнить чистовое шлифование поверхности {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += f' на L={str(length).replace('.', ',')}'
        if d['квалитет_длина']:
            text += d['квалитет_диаметер']
        if d['допуск_дл_1']:
            text += f' {self.format_dopusk(d['допуск_дл_1'])}'
        if d['допуск_дл_2']:
            text += f' {self.format_dopusk(d['допуск_дл_2'])}'
        text += '.'

        result['описание'] = text

        return result
    def osnovnoe_step_4(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        text = (f'Остановить вращение детали, отвести шлифовальный круг от поверхности.\n'
                f'Дать детали остыть до температуры измерительного помещения.\n')
        result['описание'] = text

        inst = self.instrument_manager.get_mikrometer(diameter)
        if inst:
            result['инструмент'].append(inst)

        return result


    def osnovnoe_step_5(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])

        text = f'Измерить финальный размер {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += (' в начале, середине и конце обработанной длины.\n'
                 'Проверить овальность и конусность поверхности - не более 0,005 мм.\n'
                 f'Сравнить шероховатость {d['шероховатость']} с образцом шероховатости')
        result['описание'] = text
        inst = self.instrument_manager.add('СИ Набор образцов шероховатости 0,2-6,3 ШЦ ГОСТ 9378-93')
        if inst:
            result['инструмент'].append(inst)
        return result

    def osnovnoe_step_1_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])


        text = f'Выполнить черновое внутреннее круговое продольное шлифование отверстия {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += f' на L={str(length).replace('.', ',')}'
        if d['квалитет_длина']:
            text += d['квалитет_диаметер']
        if d['допуск_дл_1']:
            text += f' {self.format_dopusk(d['допуск_дл_1'])}'
        if d['допуск_дл_2']:
            text += f' {self.format_dopusk(d['допуск_дл_2'])}'
        text += ', снять 0,3 мм. на диаметр и оставив 0,1 мм. на диаметр на чистовое шлифование.'
        result['описание'] = text

        circle = self.instrument_manager.add('РИ Круг 5 20x6x40 25A F40 К 6 V 35 м/с А 1 кл. ГОСТ Р 52781-2007')
        if circle: result['инструмент'].append(circle)

        return result

    def osnovnoe_step_2_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        text = (f'Остановить продольную подачу, вывести шлифовальный круг из отверстия, остановить вращение детали.\n'
                f'Измерить промежуточный размер {str(diameter - 0.1).replace('.', ',')}, проверив диаметр в двух сечениях и в двух взаимно перпендекулярных направлениях.\n')
        result['описание'] = text

        inst = self.instrument_manager.get_nutromer(diameter)
        if inst:
            result['инструмент'].append(inst)

        return result

    def osnovnoe_step_3_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])

        text = f'Выполнить чистовое внутреннее шлифование поверхности {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += f' на L={str(length).replace('.', ',')}'
        if d['квалитет_длина']:
            text += d['квалитет_диаметер']
        if d['допуск_дл_1']:
            text += f' {self.format_dopusk(d['допуск_дл_1'])}'
        if d['допуск_дл_2']:
            text += f' {self.format_dopusk(d['допуск_дл_2'])}'
        text += '.'

        result['описание'] = text

        return result

    def osnovnoe_step_4_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        text = (f'Вывести шлифовальный круг из отверстия, остановить вращение детали.\n'
                f'Промыть и продуть отверстие, удалить абразивные частицы из кольцевых канавок и кромок.\n'
                f'Дать детали остыть до температуры измерительного помещения.')
        result['описание'] = text

        inst = self.instrument_manager.get_mikrometer(diameter)
        if inst:
            result['инструмент'].append(inst)

        return result

    def osnovnoe_step_5_1(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        length = self.format_num(d['длина'])

        text = f'Измерить финальный размер {str(diameter).replace('.', ',')}'
        if d['квалитет_диаметер']:
            text += d['квалитет_диаметер']
        if d['допуск_д_1']:
            text += f' {self.format_dopusk(d['допуск_д_1'])}'
        if d['допуск_д_2']:
            text += f' {self.format_dopusk(d['допуск_д_2'])}'
        text += (' в начале, середине и конце обработанной длины.\n'
                 f'Проверить овальность и бочкообразность отверстия - не более 0,005 мм.\n'
                 f'Сравнить шероховатость {d['шероховатость']} с образцом шероховатости')
        result['описание'] = text
        inst = self.instrument_manager.add('СИ Набор образцов шероховатости 0,2-6,3 ШЦ ГОСТ 9378-93')
        if inst:
            result['инструмент'].append(inst)
        return result

