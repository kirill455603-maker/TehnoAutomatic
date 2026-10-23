from logic.instrument_manager import InstrumentManager
from logic.automation import TechnoproAutomation
from logic import constants

class OperationBase:
    def __init__(self):
        self.operations = {}
        self.count = 0
        self.index = 0

        # Делегирование обязанностей

        self.automation = TechnoproAutomation()

        # Справочники
        self.dict_sverla = constants.SVERTLA
        self.list_d_rezba = constants.D_REZBA
        self.metric_thread_pitches = constants.METRIC_THREAD_PITCHES
        self.thread_tolerances = constants.THREAD_TOLERANCES
        self.instrument_razmetka = constants.INSTRUMENT_RAZMETKA
        self.dopusk_razvertka = constants.RAZVERTKA_KVALITET
        self.dopusk_surf = constants.QUALLITY_SURF
        self.dict_razvetki = constants.RAZVERTKI
        self.metchiki = constants.METCHIKI
        self.zenkovki = constants.ZENKOVKI
        self.operations_tehno = constants.OPERATIONS
        self.operations_sborka = constants.OPERATIONS_SBORKA
        self.details = constants.DETAILS
        self.deistviya = constants.DEISTVIYA
        self.probki_gladkie = constants.PROBKI_GLADKIE
        self.rezhimi = constants.REZHIMI
        self.rezhimi_sverlenie = constants.REZHIMI_SVERLENIE
        self.rezhimi_shlifovka = constants.REZHIMI_SHLIFOVKA



    def format_num(self, num: float):
        """Убирает .0 у целых чисел для красивого вывода."""
        return int(num) if num == int(num) else str(num)

    def format_dopusk(self, dopusk: float) -> str:
        """Добавляет + к положительному допуску и меняет точку на запятую."""
        sign = '+' if dopusk > 0 else ''
        return f"{sign}{dopusk}".replace('.', ',')

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

    def counter_base(self, text:str):
        base:str = text.replace(' ', '')
        text_output = ''
        for i, letter in enumerate(base):
            if text_output:
                if len(base) - i == 1:
                    text_output += ' и '
                elif len(base) - i > 1:
                    text_output += ', '
            text_output += letter
        return text_output


    def run_automatica(self, index: int):
        self.automation.run_automatica(self.operations, index, image_find='logic/image_find/tok_find.PNG')

    def run_automatica_sborka(self, index: int):
        self.automation.run_automatica_sborka(self.operations, index, image_find='logic/image_find/tok_find.PNG')



    def clear_all(self):
        self.count = 0
        self.index = 0
        self.operations.clear()