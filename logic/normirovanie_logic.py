from logic.operation_base import OperationBase
from math import pi, ceil
import pyautogui

class NormirovanieLogic(OperationBase):
    def __init__(self):
        super().__init__()
        self.Ty = 2 #Время на установку, мин
        self.Tv = 2 #Время на вспомогательные ходы, мин
        self.Kobs = 0.98 # Обслуживание станка
        self.Kot = 0.98 # Отдых

        self.l_exit = 3 #Выход сверловка
        self.l_perebeg = 4#Перебег сверловка

    def cutting(self, d:dict) -> int:
        #F=(pi * D**2)/(4 * 100)
        Q = self.rezhimi[d['материал']]['отрезная']
        D = d['диаметр']
        F = (pi * D ** 2) / (4 * 100)
        return ceil((((F / Q) + self.Ty + self.Tv) / self.Kobs) / self.Kot)

    def find_operations(self, image):
        region = (31, 226, 554, 673)
        try:
            matches = pyautogui.locateOnScreen(image, region=region, confidence=0.9)
            if matches:
                return True
        except:
            return False

    def turnining_prodolnoe(self, d, material):
        #Тшт = Ту + Tв + Tм
        L = d['длина']
        Dstart = d['диаметр заготовки']
        Dend = d['диаметр детали']
        A = (Dstart - Dend) / 2 #Общий припуск
        t = d['глубина']
        i = ceil(A / t) #Количество проходов
        S = self.rezhimi[material]['токарная']['точение']['подача']
        V = self.rezhimi[material]['токарная']['точение']['скорость']
        Tm = 0
        for i in range(1, i):
            Tm += (L * pi * Dstart) / (1000 * S * V)
            Dstart -= t * 2

        return ceil(((Tm + self.Ty + self.Tv) / self.Kobs) / self.Kot)

    def turning_kanavka(self, d, material):
        Svrez = self.rezhimi[material]['токарная']['канавка']['подача'] #врезание
        V = self.rezhimi[material]['токарная']['канавка']['скорость']
        Sprod = self.rezhimi[material]['токарная']['точение']['подача'] #продольное
        Tm = 0
        t = d['глубина']
        b = d['ширина']
        b0 = d['резец']
        k = d['количество']
        if b > b0:
            Tm = ((t / Svrez) + ((b - b0) / Sprod)) + (k * self.Tv)
        else:
            Tm = (t / Svrez) + (k * self.Tv)

        return ceil(((Tm + self.Ty) / self.Kobs) / self.Kot)

    def turning_podrezka(self, d, material):
        S = self.rezhimi[material]['токарная']['подрезка']['подача']  # врезание
        V = self.rezhimi[material]['токарная']['подрезка']['скорость']
        Dstart = d['диаметр начальный']
        Dend = d['диаметр конечный']
        Linput = 2 #Подвод
        Loutput = 2 #Отвод
        Dsr = (Dstart + Dend) / 2
        L = ((Dstart - Dend) / 2) + Linput + Loutput
        Tm = ((L * pi * Dsr) / (1000 * S * V))

        return ceil(((Tm + self.Ty) / self.Kobs) / self.Kot)

    def sverlenie(self, d:dict):
        diameter = d['диаметр']
        material = d['материал']
        l = d['длина']
        k = d['количество']

        S = 0
        V = self.rezhimi_sverlenie['скорость'][material]
        for key in self.rezhimi_sverlenie['подача']:
            if key[0] <= diameter <= key[1]:
                S = self.rezhimi_sverlenie['подача'][key][material]

        if l > 3 * diameter:
            S = S - (S * 0.3)

        l_vrez = 0.3 * diameter + 3
        l_full = l + l_vrez + self.l_exit + self.l_perebeg
        n = (1000 * V) / (pi * diameter)

        v_f = S * n
        T_m1 = l_full/v_f

        Tm = T_m1 * (k * self.Tv)
        if l > 3 * diameter:
            exit_stryzhka = 1 # К каждому отверстию еще добавляем вывод стружки
            return ceil(Tm + self.Ty * 1.5 + self.Tv * 1.5 + (exit_stryzhka * k))
        return ceil(Tm + self.Ty * 1.5)

    def shlifovka(self, d:dict):
        diameter = d['диаметр']
        material = d['материал']
        l = d['длина'] + 63 * 2
        a = d['припуск'] / 2
        a_chern = a * 0.7 #припуск черновой
        a_chist = a - a_chern #припуск чистовой

        s = self.rezhimi_shlifovka[material]['подача']
        v = self.rezhimi_shlifovka[material]['скорость']

        t_chern = 0.02  # Глубина резания черновая
        t_chist = 0.01  # Глубина резания чистовая

        if material == 'Легированные и улучшаемые стали':
            t_chern = 0.01 #Глубина резания черновая
            t_chist = 0.007 #Глубина резания чистовая
        elif material == 'Нержавеющие и жаропрочные стали':
            t_chern = 0.008
            t_chist = 0.005
        elif material == 'Титан и титановые сплавы':
            t_chern = 0.005
            t_chist = 0.002

        i_chern = ceil(a_chern / t_chern) #проходы черновые
        i_chist = ceil(a_chist / t_chist) #проходы чистовые
        i_full = i_chern + i_chist + 5

        n = (1000 * v)/(pi * diameter)

        Tm = (l * i_full)/(s * n)

        return ceil(Tm + self.Ty + self.Tv)

