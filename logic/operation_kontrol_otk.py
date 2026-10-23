from logic.operation_base import OperationBase
from logic.instrument_manager import InstrumentManager

class KontrolOtk(OperationBase):
    def __init__(self):
        super().__init__()
        self.image = 'logic/find_operations/control_otk_find.PNG'
        self.instrument_manager = InstrumentManager()
        self.operations = {}


    @property
    def all_instrument(self):
        return self.instrument_manager.all_instrument

    def find_and_delete_from_all_instrument(self, instruments: list):
        self.instrument_manager.remove(instruments)

    def take_value_matches(self) -> int:
        return self.automation.take_value_matches(self.image)

    def diameter(self, d):
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        text = f'Контролировать {str(diameter).replace('.', ',')}'

        if d['квалитет']:
            text += d['квалитет']

        # Объединяем обработку допуск_1 и допуск_2 в цикл
        for key in ('допуск_1', 'допуск_2'):
            if d[key] != 0:
                dopusk = self.format_dopusk(d[key])
                text += f' {dopusk}'

                if abs(d[key]) < 0.01:
                    if d['тип'] == 'вал':
                        i = self.instrument_manager.get_mikrometer(diameter)
                    elif d['тип'] == 'отверстие':
                        i = self.instrument_manager.get_nutromer(diameter)
                    else:
                        i = None

                    if i:
                        result['инструмент'].append(i)

        # Проверка квалитета (для строк if d['квалитет'] равносильно != '')
        if d['квалитет']:
            if d['квалитет'] in ('H7', 'H8', 'H6'):
                i = self.instrument_manager.get_nutromer(d['диаметр'])
                if i:
                    result['инструмент'].append(i)
            elif d['квалитет'] in ('h7', 'h8', 'h6'):
                i = self.instrument_manager.get_mikrometer(d['диаметр'])
                if i:
                    result['инструмент'].append(i)
            else:
                i = self.instrument_manager.get_shtangencirkul(float(d['диаметр']))
                if i:
                    result['инструмент'].append(i)
        else:
            i = self.instrument_manager.get_shtangencirkul(float(d['диаметр']))
            if i:
                result['инструмент'].append(i)



        # Исправлен приоритет операторов (добавлены скобки) и убраны лишние abs()
        if (d['допуск_1'] != 0 or d['допуск_2'] != 0) and d['тип'] in ('вал', 'отверстие'):
            if abs(d['допуск_1'] - d['допуск_2']) <= 0.01:
                if d['тип'] == 'вал':
                    i = self.instrument_manager.get_mikrometer(diameter)
                else:
                    i = self.instrument_manager.get_nutromer(diameter)

                if i:
                    result['инструмент'].append(i)

        result['описание'] = text
        return result

    def length(self, d):
        result = {'описание': '', 'инструмент': []}
        length = self.format_num(d['длина'])
        text = f'Контролировать L={str(length).replace('.', ',')}'
        if d['квалитет'] != '':
            text += d['квалитет']
        if d['допуск_1']:
            dopusk = self.format_dopusk(d['допуск_1'])
            text += f' {dopusk}'
        if d['допуск_2']:
            dopusk = self.format_dopusk(d['допуск_2'])
            text += f' {dopusk}'
        i = self.instrument_manager.get_shtangencirkul(float(length))
        if i:
            result['инструмент'].append(i)
        result['описание'] = text
        return result

    def hole_gladkoe(self, d):
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        count = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))
        if d['количество'] < 5:
            counts = {
                1: 'одно',
                2: 'два',
                3: 'три',
                4: 'четыре'
            }
            text = f'Контролировать {counts[d['количество']]} {count} {str(diameter).replace('.', ',')}'
        else:
            text = f'Контролировать {d['количество']} {count} {str(diameter).replace('.', ',')}'
        if d['квалитет']:
            text += d['квалитет']
        if d['допуск_1'] != 0:
            text += f' {self.format_dopusk(d['допуск_1'])}'
        if d['допуск_2'] != 0:
            text += f' {self.format_dopusk(d['допуск_2'])}'

        if d['статус глубины']:
            text += f' и L={self.format_num(d['глубина'])}'
            if d['квалитет глубины']:
                text += d['квалитет глубины']
            if d['допуск_гл_1'] != 0:
                text += f' {self.format_dopusk(d['допуск_гл_1'])}'
            if d['допуск_гл_2'] != 0:
                text += f' {self.format_dopusk(d['допуск_гл_2'])}'

        result['описание'] = text

        i = self.instrument_manager.get_probka_gladkaya(float(d['диаметр']))
        if i:
            result['инструмент'].append(i)
        else:
            i = self.instrument_manager.get_shtangencirkul(float(d['диаметр']))
            if i:
                result['инструмент'].append(i)

        return result

    def hole_rezba(self, d):
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(d['диаметр'])
        d['шаг'] = self.format_num(d['шаг'])
        count = self.pluralize_ru(d['количество'], ('отверстие', 'отверстия', 'отверстий'))
        rezba = self.pluralize_ru(d['количество'], ('резьбовое', 'резьбовых', 'резьбовых'))
        if d['количество'] < 5:
            counts = {
                1: 'одно',
                2: 'два',
                3: 'три',
                4: 'четыре'
            }
            text = f'Контролировать {counts[d['количество']]}'
        else:
            text = f'Контролировать {d['количество']}'

        text += f' {rezba} {count} М{str(diameter).replace('.', ',')}х{str(d['шаг']).replace('.', ',')}'
        if d['допуск']:
            text += f'-{d['допуск']}'

        if d['статус глубины']:
            text += f', L={str(self.format_num(d['глубина'])).replace('.', ',')}'
            if d['квалитет глубины']:
                text += d['квалитет глубины']
            if d['допуск_гл_1'] != 0:
                text += f' {self.format_dopusk(d['допуск_гл_1'])}'
            if d['допуск_гл_2'] != 0:
                text += f' {self.format_dopusk(d['допуск_гл_2'])}'
            text += f' и L={str(self.format_num(d['глубина резьбы'])).replace('.', ',')}'
            if d['допуск_дл_резьба_1'] != 0:
                text += f' {self.format_dopusk(d['допуск_дл_резьба_1'])}'
            if d['допуск_дл_резьба_2'] != 0:
                text += f' {self.format_dopusk(d['допуск_дл_резьба_2'])}'

        result['описание'] = text

        i = self.instrument_manager.get_probka_rezba(
            diameter=float(d['диаметр']),
            step=float(d['шаг'])
        )

        if i:
            result['инструмент'].append(i)
        else:
            i = self.instrument_manager.get_shtangencirkul(d['диаметр'])
            if i:
                result['инструмент'].append(i)

        return result

    def diameter_rezba(self, d):
        result = {'описание': '', 'инструмент': []}
        diameter = self.format_num(float(d['диаметр'][1:]))
        step = self.format_num(float(d['шаг']))

        text = f'Контролировать'
        if d['тип резьбы'] == 'внутренняя':
            text += ' внутреннюю'
        elif d['тип резьбы'] == 'внешняя':
            text += ' внешнюю'
        text += f' резьбу М{str(diameter).replace('.', ',')}х{str(step).replace('.', ',')}'
        if d['допуск']:
            text += f'-{d['допуск']}'
        result['описание'] = text

        if d['тип резьбы'] == 'внутренняя':
            i = self.instrument_manager.get_probka_rezba(float(diameter), float(step))
            if i:
                result['инструмент'].append(i)
        elif d['тип резьбы'] == 'внешняя':
            i = self.instrument_manager.get_kolco_rezba(float(diameter), float(step))
            if i:
                result['инструмент'].append(i)
            i = self.instrument_manager.get_kolco_rezba_neprohod(float(diameter), float(step))
            if i:
                result['инструмент'].append(i)
        return result

