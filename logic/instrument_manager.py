from logic.constants import (SHTANGENCIRKULI,
                             MIKROMETRY,
                             NUTROMERY,
                             PATRONS,
                             PROBKI_GLADKIE,
                             PROBKI_REZBA,
                             KOLCA_REZBA,
                             ZENKOVKI,
                             METCHIKI,
                             MIKROMETRY_WITH_REZBA,
                             KOLCA_REZBA_NEPROHOD)

class InstrumentManager:
    def __init__(self):
        self.all_instrument = []

    def add(self, instrument_name: str) -> str | None:
        if instrument_name and instrument_name not in self.all_instrument:
            self.all_instrument.append(instrument_name)
            return instrument_name
        return ''

    def remove(self, instruments: list):
        for inst in instruments:
            if inst in self.all_instrument:
                self.all_instrument.remove(inst)

    def get_patron(self, diameter: float) -> str | None:
        for key in sorted(PATRONS.keys()):
            if key >= diameter:
                return self.add(PATRONS[key])
        return ''

    def get_shtangencirkul(self, max_value: float) -> str | None:
        for key in sorted(SHTANGENCIRKULI.keys()):
            if key >= max_value:
                return self.add(SHTANGENCIRKULI[key])
        return ''

    def get_mikrometer(self, diameter: float) -> str | None:
        for (min_d, max_d), name in MIKROMETRY.items():
            if min_d <= diameter <= max_d:
                return self.add(name)
        return ''

    def get_mikrometer_with_rezba(self, diameter):
        for (min_d, max_d), name in MIKROMETRY_WITH_REZBA.items():
            if min_d <= diameter <= max_d:
                return self.add(name)
        return ''

    def get_nutromer(self, diameter: float) -> str | None:
        for (min_d, max_d), name in NUTROMERY.items():
            if min_d <= diameter <= max_d:
                return self.add(name)
        return ''

    def get_probka_gladkaya(self, diameter: float) -> str | None:
        for key in sorted(PROBKI_GLADKIE.keys()):
            if diameter == key:
                return self.add(PROBKI_GLADKIE[key])
        return ''

    def get_probka_rezba(self, diameter: float, step: float) -> str | None:
        for el in PROBKI_REZBA:
            text = el[el.index('М') + 1:]
            text = text[:text.find(' ')]
            diam = float(text[:text.find('x')].replace(',', '.'))
            s = float(text[text.find('x') + 1:].replace(',', '.'))
            if diameter == diam and abs(step - s) <= 0.05:
                return self.add(el)
        return ''

    def get_kolco_rezba(self, diameter:float, step: float) -> str | None:
        diameter = self.format_num(diameter)
        step = self.format_num(step)
        text_find = f'{diameter} x {step}'.replace('.', ',')
        for el in KOLCA_REZBA:
            if text_find in el or text_find.replace('x', 'х') in el:
                return self.add(el)
        return ''

    def get_kolco_rezba_neprohod(self, diameter:float, step:float) -> str | None:
        diameter = self.format_num(diameter)
        step = self.format_num(step)
        text_find = f'{diameter} x {step}'.replace('.', ',')
        for el in KOLCA_REZBA_NEPROHOD:
            if text_find in el or text_find.replace('x', 'х') in el:
                return self.add(el)
        return ''

    def get_metchik(self, diameter:float, step:float) -> str:
        step = str(step).replace('.', ',')
        diameter = str(diameter).replace('.', ',')
        find_text = f'{diameter}х{step}'
        for metchik in METCHIKI:
            if find_text in metchik or find_text.replace('х', 'x') in metchik:
                return self.add(metchik)
        return ''

    def get_zenkovka(self, diameter:float) -> str:
        for key, value in ZENKOVKI.items():
            r = diameter - key
            if r < 4:
                return self.add(value)
        return ''

    def format_num(self, num: float):
        """Убирает .0 у целых чисел для красивого вывода."""
        return int(num) if num == int(num) else str(num)
