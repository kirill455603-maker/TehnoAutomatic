from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager
import pyautogui


class Sborka(OperationBase):
    def __init__(self):
        super().__init__()
        self.instrument_manager = InstrumentManager()
        self.REGION_TABLE = (31, 226, 554, 673)

    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument


    def show_in_program(self):
        data = []
        for operation in self.operations_sborka:
            try:
                match = pyautogui.locateOnScreen(image=operation['кнопка'],
                                                 confidence=0.85,
                                                 region=self.REGION_TABLE)
                data.append(operation['операция'])
            except:
                continue
        return data

    def get_count_operations(self, name_operation):
        for operation in self.operations_sborka:
            if operation['операция'] == name_operation:
                try:
                    matches = pyautogui.locateAllOnScreen(image=operation['кнопка'],
                                                          confidence=0.85,
                                                          region=self.REGION_TABLE)
                    return len(list(matches))
                except:
                    return 0

    def termichka(self, d: dict, num: int):
        result = {'описание': '', 'инструмент': []}
        text = ''
        if num == 0:
            text = f'На поддон цеховой, в {d['положение']} положении, установить {d['деталь']} поз. {d['поз']}'
        elif num == 1:
            text = f'Нагреть до температуры {d['температура']}{d['допуск']}С'
        elif num == 2:
            text = f'Поддон цеховой {d['установка']}'

        result['описание'] = text
        r = self.instrument_manager.add('ВИ Перчатки защитные по ГОСТ 12.4.252-2013')
        result['инструмент'].append(r)
        r = self.instrument_manager.add('ПР Поддон цеховой')
        result['инструмент'].append(r)
        return result

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)


    def slesarnaya_meh(self, d:dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        text = f'Острые кромки притупить фаской {str(d['фаска']).replace('.', ',')}х{d['угол']}'
        result['описание'] = text

        r = self.instrument_manager.add('РИ Напильник 2820-0001 ГОСТ 1465-80')
        result['инструмент'].append(r)
        return result

    def slesarnaya_sborka_protirka(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}

        text = f'{d['положение']} поверхность {d['деталь']} поз. {d['позиция']} протереть {d['инструмент']}'
        result['описание'] = text

        r = self.instrument_manager.add('М Ветошь 501 (обтирочная) ГОСТ 4643-75')
        result['инструмент'].append(r)
        if d['инструмент'] == 'спиртом':
            r = self.instrument_manager.add('М Спирт этиловый технический марки А ГОСТ 17299-78')
            result['инструмент'].append(r)
        elif d['инструмент'] == 'уайт-спиритом':
            r = self.instrument_manager.add('М Уайт-спирит (нефрас-С4-155/200) ГОСТ 3134-78')
            result['инструмент'].append(r)
        return result

    def sborka(self, d):
        result = {'описание': '', 'инструмент': []}
        result['описание'] = d['текст']
        return result

    def slesarnaya_svarka_zachistka_and_obez(self, d: dict, text_zag):
        result = {'описание': '', 'инструмент': []}

        text = text_zag
        for key, value in d['детали'].items():
            text += f' {key} поз. {value}'
            text += ' ,'
        text = text[:-1]
        if text_zag == 'Зачистить':
            text += f'в местах сварки и прилегающие и контактирующие поверхности на ширину от {d['ширина_от']} до {d['ширина_до']} мм'
        elif text_zag == 'Обезжирить':
            text += f'в местах сварки, с двух сторон прилегающие и контактирующие поверхности на ширину от {d['ширина_от']} до {d['ширина_до']} мм'
            r = self.instrument_manager.add('М Уайт-спирит (нефрас-С4-155/200) ГОСТ 3134-78')
            result['инструмент'].append(r)
            r = self.instrument_manager.add('М Ветошь 501 (обтирочная) ГОСТ 4643-75')
            result['инструмент'].append(r)
        result['описание'] = text
        r = self.instrument_manager.add('ПР Машинка прямошлифовальная цеховая')
        result['инструмент'].append(r)
        r = self.instrument_manager.add('ВИ Щетка металлическая типа Makita  (проволока - нержавеющая)')
        result['инструмент'].append(r)
        return result

    def svarka_start(self, d: dict):
        result = {'описание': '', 'инструмент': []}

        text = f'{d['положение']} стягивающее приспособление'
        result['описание'] = text
        r = self.instrument_manager.add('ПР Прижимающее приспособление цеховое')
        result['инструмент'].append(r)

        return result

    def svarka_zach_shvov(self, d: dict) -> dict:
        result = {'описание': '', 'инструмент': []}
        result['описание'] = 'Зачистить сварные швы от цветов побежалости'
        r = self.instrument_manager.add('ПР Машинка прямошлифовальная цеховая')
        result['инструмент'].append(r)
        r = self.instrument_manager.add('ВИ Щетка металлическая типа Makita  (проволока - нержавеющая)')
        result['инструмент'].append(r)
        return result

    def save_result_markirovanie(self, d:dict) -> dict:
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

    def save_result_promivka(self):
        result = {'описание': '', 'инструмент': []}

        text = 'Промыть деталь, соблюдая требования технологической инструкции 0601.25000.00041'
        inst = self.instrument_manager.add('М Ветошь 501 (обтирочная) ГОСТ 4643-75')
        result['описание'] = text
        result['инструмент'].append(inst)

        return result

