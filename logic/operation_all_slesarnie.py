from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager

class AllSlesarnie(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/find_operations/mark_find.PNG'
        self.instrument_manager = InstrumentManager()

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

    def markirovanie(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        if d['метод'] == 'ударный':
            result['описание'] = f'Маркировать обозначение чертежа {d['объект']} ударным способом согласно п. {d['номер']} ТТ чертежа {d['чертеж']}'
            r = self.instrument_manager.add('ВИ Молоток 7850-0101 ГОСТ 2310-77')
            result['инструмент'].append(r)
            r = self.instrument_manager.add('РИ Клеймо 7858-0054 ВК8-Х1Н12 ГОСТ 25726-83')
            result['инструмент'].append(r)
            r = self.instrument_manager.add('РИ Клеймо 7858-0074 ВК8-Х1Н12 ГОСТ 25726-83')
            result['инструмент'].append(r)
        elif d['метод'] == 'маркерный':
            result['описание'] = f'Маркировать обозначение чертежа {d['объект']} согласно п. {d['номер']} ТТ чертежа {d['чертеж']}'
            r = self.instrument_manager.add('ВИ Тушь черная ТУ 6-15-458-86 или маркер')
            result['инструмент'].append(r)

        return result