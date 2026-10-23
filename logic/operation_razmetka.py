# logic/operation_tokarnaya.py
from logic.instrument_manager import InstrumentManager
from logic.operation_base import OperationBase


class Razmetka(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/image_find/razmetka.PNG'


        self.instrument_manager = InstrumentManager()

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def razmetka(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр разметки'])
        for instrument in self.instrument_razmetka:
            r = self.instrument_manager.add(instrument)
            if r: result['инструмент'].append(r)

        if d['без резьбы'] > 0:
            d['без резьбы'] = self.format_num(d['без резьбы'])

        hole = d['резьба'] if d['резьба'] != '' else f'{d['без резьбы']}'
        hole_text = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))
        text = f'Разметить {d['количество']} {hole_text} {str(hole).replace('.', ',')} по {str(diameter).replace('.', ',')}'
        if d['угол'] != 0 and d['допуск'] != 0:
            text += f', контролировать осевое смещение {d['угол']} и допуск позиционирования {str(d['допуск']).replace('.', ',')} относительно базы {d['база']}'
        elif d['угол'] != 0 and d['допуск'] == 0:
            text += f', контролировать осевое смещение {d['угол']}'
        elif d['угол'] == 0 and d['допуск'] != 0:
            text += f', контролировать допуск позиционирования {str(d['допуск']).replace('.', ',')} относительно базы {d['база']}'

        result['описание'] = text
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

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

