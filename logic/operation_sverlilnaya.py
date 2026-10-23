from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager

class Sverlilnaya(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/image_find/sverlilnaya_find.PNG'

        self.instrument_manager = InstrumentManager()

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def start(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        d['допуск'] = self.format_dopusk(d['допуск'])
        hole_word = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))
        hole_type = 'глухое' if d['глубина'] > 0 else 'сквозное'
        if hole_type == 'глухое':
            word = self.pluralize_ru(count=d['количество'], forms=('глухое', 'глухих', 'глухих'))
        else:
            word = self.pluralize_ru(d['количество'], ('сквозное', 'сквозных', 'сквозных'))
        d['глубина'] = self.format_num(d['глубина'])
        d['диаметр'] = self.format_num(d['диаметр'])
        d['расположение'] = self.format_num(d['расположение'])
        word_razmetka = 'размеченных местах' if d['количество'] > 1 else 'размеченном месте'

        text = f'Сверлить {d['количество']} {word} {hole_word} {str(d['диаметр']).replace('.', ',')} {str(d['допуск']).replace('.', ',')} в {word_razmetka}'
        if d['расположение'] != 0:
            text += f' по диаметру {str(d['расположение']).replace('.', ',')}'
        if hole_type == 'глухое' and d['глубина'] != 0:
            text += f' на глубину L={str(d['глубина']).replace('.', ',')}'

        result['описание'] = text
        r = self.instrument_manager.add(self.dict_sverla[float(d['диаметр'])])
        result['инструмент'].append(r)
        return result

    def expanding(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        word1 = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))
        diameter_start = self.format_num(d['отверстие'])
        d_sverlo = self.format_num(d['сверло'])
        d_position = self.format_num(d['расположение'])

        text = f'Рассверлить {d['количество']} {word1} {str(diameter_start).replace('.', ',')} до {str(d_sverlo).replace('.', ',')}'
        if d_position != 0:
            text += f' по {str(d_position).replace('.', ',')}'
        if d['глубина'] > 0:
            d['глубина'] = self.format_num(d['глубина'])
            text += f' на глубину L={str(d['глубина']).replace('.', ',')}'
            shtangel = self.instrument_manager.get_shtangencirkul(d['глубина'])
            if shtangel: result['инструмент'].append(shtangel)

        result['описание'] = text
        r = self.instrument_manager.add(self.dict_sverla[d['сверло']])

        result['инструмент'].append(r)
        return result

    def chistovaya(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        n_d = self.format_num(d['номинальный диаметр'])
        t_d = self.format_num(d['текущий диаметр'])
        d_r = self.format_num(d['расположение'])
        l = self.format_num(d['длина'])
        word = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))

        text = f'Развернуть {d['количество']} {word} {str(t_d).replace('.', ',')} до {str(n_d).replace('.', ',')}{d['допуск']} с шероховатостью поверхности {d['шероховатость']}'
        if d_r != 0:
            text += f' по {str(d_r).replace('.', ',')}'
        if l > 0:
            text += f' на глубину L={str(l).replace('.', ',')}'
        result['описание'] = text
        instrument = self.dict_razvetki[d['номинальный диаметр']]
        if d['допуск'] == 'H8':
            instrument = instrument.replace('H7', 'H8')
        r = self.instrument_manager.add(instrument)
        if r:
            result['инструмент'].append(r)
        return result

    def rezba(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        rezba = self.format_num(d['резьба'])
        step = self.format_num(d['шаг'])
        position = self.format_num(d['расположение'])
        depth = self.format_num(d['глубина'])
        word = self.pluralize_ru(d['количество'], ('отверстии', 'отверстиях', 'отверстиях'))

        text = f'Нарезать резьбу М{str(rezba).replace('.', ',')}х{str(step).replace('.', ',')}-{d['допуск']} в {d['количество']} {word}'
        if position != 0:
            text += f' по {str(position).replace('.', ',')}'
        if depth > 0:
            text += f' на глубину L={str(depth).replace('.', ',')}'
        result['описание'] = text
        instrument = self.instrument_manager.get_metchik(diameter=rezba,step=step)
        if instrument: result['инструмент'].append(instrument)
        i = self.instrument_manager.get_probka_rezba(float(rezba), float(step))
        if i:
            result['инструмент'].append(i)
        return result

    def faska(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        position = self.format_num(d['расположение'])
        l = self.format_num(d['длина'])
        text_count = 'фаски' if d['количество'] > 1 else 'фаску'
        word_count = self.pluralize_ru(d['количество'], ('отверстии', 'отверстиях', 'отверстиях'))
        text = f'Зенковать {text_count} {str(l).replace('.', ',')}х{d['угол']} в {d['количество']} {word_count}'
        if position != 0:
            text += f' по {str(position).replace('.', ',')}'
        result['описание'] = text
        instrument = self.instrument_manager.get_zenkovka(float(diameter))
        if instrument: result['инструмент'].append(instrument)
        return result


    def pluralize_ru(self, count: int, forms: tuple) -> str:
        """
        Универсальная функция склонения для русского языка.
        forms: кортеж из 3 строк (форма для 1, форма для 2, форма для 5).
        Пример forms для 'отверстие': ("отверстие", "отверстия", "отверстий")
        """
        count = abs(int(count))

        if count % 10 == 1 and count % 100 != 11:
            idx = 0
        elif 2 <= count % 10 <= 4 and not (12 <= count % 100 <= 14):
            idx = 1
        else:
            idx = 2

        return f"{forms[idx]}"

    # Использование:
    # forms = ("отверстие", "отверстия", "отверстий")
    # print(pluralize_ru(24, forms))  # Выведет: 24 отверстия

    def find_shtangel_for_precision(self, diameter: float, kvalitet: str, dopusk1: float,
                                    dopusk2: float) -> str | None:
        """Универсальная логика подбора Микрометра/Штангенциркуля для токарной/расточной."""
        is_h7_h8 = kvalitet in ('h7', 'h8')
        is_tight_dopusk = (0.01 <= abs(dopusk1) <= 0.1) or (0.01 <= abs(dopusk2) <= 0.1)

        if is_h7_h8 or is_tight_dopusk:
            return self.instrument_manager.get_mikrometer(diameter)
        return self.instrument_manager.get_shtangencirkul(diameter)

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

