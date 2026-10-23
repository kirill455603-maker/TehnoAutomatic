# logic/constants.py
import csv
import json

# --- СПРАВОЧНИКИ ИНСТРУМЕНТОВ ---
PATRONS = {
    250: 'ПР Патрон 7102-0078-1-2 ГОСТ 24351-80 (D250)',
    400: 'ПР Патрон 7102-0086-1-2 ГОСТ 24351-80 (D400)',
    500: 'ПР Патрон 7102-0091-1-2 ГОСТ 24351-80 (D500)',
    630: 'ПР Патрон 7100-0019 ГОСТ 2675-80 (D630)'
}

SHTANGENCIRKULI = {
    125: 'СИ Штангенциркуль ШЦ-I-125-0,05 ГОСТ 166-89',
    200: 'СИ Штангенциркуль ШЦ-I-200-0,05 ГОСТ 166-89',
    400: 'СИ Штангенциркуль ШЦ-I-400-0,1 ГОСТ 166-89',
    500: 'СИ Штангенциркуль ШЦ-I-500-0,05 ГОСТ 166-89',
    1250: 'СИ Штангенциркуль ШЦ-I-500-1250-0,1 ГОСТ 166-89',
}

MIKROMETRY = {
    (0, 25): 'СИ Микрометр МК Н25 ГОСТ 6507-90',
    (25, 50): 'СИ Микрометр МК Н50 ГОСТ 6507-90',
    (50, 75): 'СИ Микрометр МК Н75 ГОСТ 6507-90',
    (75, 100): 'СИ Микрометр МК Н100 ГОСТ 6507-90',
    (100, 125): 'СИ Микрометр МК Н125 ГОСТ 6507-90',
    (125, 150): 'СИ Микрометр МК Н150 ГОСТ 6507-90',
    (150, 175): 'СИ Микрометр МК Н175 ГОСТ 6507-90',
    (175, 200): 'СИ Микрометр МК Н200 ГОСТ 6507-90',
    (200, 225): 'СИ Микрометр МК Н225 ГОСТ 6507-90',
    (225, 250): 'СИ Микрометр МК Н250 ГОСТ 6507-90',
    (250, 275): 'СИ Микрометр МК Н275 ГОСТ 6507-90',
    (275, 300): 'СИ Микрометр МК Н300 ГОСТ 6507-90',
    (300, 400): 'СИ Микрометр МК400-2 ГОСТ 6507-90',
    (400, 500): 'СИ Микрометр МК500 ГОСТ 6507-90',
    (500, 600): 'СИ Микрометр МК600 ГОСТ 6507-90',
}
MIKROMETRY_WITH_REZBA = {
    (0, 25): 'СИ Микрометр МВМ-0-25 ГОСТ 4380-86',
    (25, 50): 'СИ Микрометр МВМ-25-50 ГОСТ 4380-86',
    (50, 75): 'СИ Микрометр МВМ-50-75 ГОСТ 4380-86',
    (75, 100): 'СИ Микрометр МВМ 75-100 ГОСТ 4380-86',
    (100, 125): 'СИ Микрометр МВМ-100-125 ГОСТ 4380-86',
    (125, 150): 'СИ Микрометр МВМ-125-150 ГОСТ 4380-86',
    (150, 175): 'СИ Микрометр МВМ-150-175 ГОСТ 4380-86',
}

NUTROMERY = {
    (10, 18): 'СИ Нутромер НИ 10-18 ГОСТ 868-82',
    (18, 50): 'СИ Нутромер НИ 18-50 ГОСТ 868-82',
    (50, 100): 'СИ Нутромер НИ 50-100-1 ГОСТ 868-82',
    (100, 160): 'СИ Нутромер НИ 100-160 ГОСТ 868-82',
    (160, 250): 'СИ Нутромер НИ 160-250-1 ГОСТ 868-82',
    (250, 450): 'СИ Нутромер НИ 250-450 ГОСТ 868-82',
    (450, 700): 'СИ Нутромер НИ 450-700 ГОСТ 868-82',
    (700, 1000): 'СИ Нутромер НИ 700-1000 ГОСТ 868-82',
}

# --- СПРАВОЧНИКИ РЕЗЬБ И СВЕРЛ ---
SVERTLA = {
}
with open('files/sverla.csv', 'r', encoding='utf-8') as sverla_csv:
    rows = csv.DictReader(sverla_csv)
    for r in rows:
        key = r['Диаметр']
        SVERTLA[float(key)] = r['Наименование']
RAZVERTKI = {
}
with open('files/razvertki.csv', 'r', encoding='utf-8') as razvertki_csv:
    rows = csv.DictReader(razvertki_csv)
    for r in rows:
        key = r['Диаметр']
        RAZVERTKI[float(key)] = r['Наименование']

METCHIKI = [
]

with open('files/metchiki.csv', 'r', encoding='utf-8') as metchiki_csv:
    rows = csv.reader(metchiki_csv)
    for row in rows:
        METCHIKI.append(row[0])

ZENKOVKI = {
}
with open('files/zenkovki.csv', 'r', encoding='utf-8') as zenkovki_csv:
    rows = csv.DictReader(zenkovki_csv)
    for r in rows:
        key = r['Диаметр']
        ZENKOVKI[float(key)] = r['Описание']

D_REZBA = [
    '1', '1.2', '1.4', '1.6', '2', '2.5', '3', '4', '5', '6',
    '8', '10', '12', '14', '16', '18', '20', '22', '24', '27',
    '30', '33', '36', '39', '42', '45', '48.0', '52', '56', '60',
    '64', '68', '72', '76', '80', '85', '90', '95'
]

METRIC_THREAD_PITCHES = {
    1.0:  ['0.25'],
    1.2:  ['0.25'],
    1.4:  ['0.3'],
    1.6:  ['0.35'],
    2.0:  ['0.4'],
    2.5:  ['0.45'],
    3.0:  ['0.5', '0.35'],
    4.0:  ['0.7', '0.5'],
    5.0:  ['0.8', '0.5'],
    6.0:  ['1.0', '0.75'],
    8.0:  ['1.25', '1.0', '0.75'],
    10.0: ['1.5', '1.25', '1.0'],
    12.0: ['1.75', '1.5', '1.25', '1.0'],
    14.0: ['2.0', '1.5', '1.0'],
    16.0: ['2.0', '1.5'],
    18.0: ['2.5', '2.0', '1.5'],
    20.0: ['2.5', '2.0', '1.5'],
    22.0: ['2.5', '2.0', '1.5'],
    24.0: ['3.0', '2.0', '1.5'],
    27.0: ['3.0', '2.0', '1.5'],
    30.0: ['3.5', '2.0', '1.5'],
    33.0: ['3.5', '2.0', '1.5'],
    36.0: ['4.0', '3.0', '2.0'],
    39.0: ['4.0', '3.0', '2.0'],
    42.0: ['4.5', '3.0', '2.0'],
    45.0: ['4.5', '3.0', '2.0'],
    48.0: ['5.0', '3.0', '2.0'],
    52.0: ['5.0', '4.0', '3.0'],
    56.0: ['5.5', '4.0', '3.0', '2.0', '1.5'],
    60.0: ['5.5', '4.0', '3.0', '2.0', '1.5'],
    64.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    68.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    72.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    76.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    80.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    85.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    90.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
    95.0: ['6.0', '4.0', '3.0', '2.0', '1.5'],
}

THREAD_TOLERANCES = {
    "внешняя": ["4h", "5h", "5g", "6e", "6f", "6g", "6h", "7g", "7h", "8e", "8g"],
    "внутренняя": ["4H", "5H", "6G", "6H", "7G", "7H"]
}
RAZVERTKA_KVALITET = ['H7', 'H8']
QUALLITY_SURF = ['Ra 0,8', 'Ra 1,6', 'Ra 3,2', 'Ra 6,3', 'Ra 12,5']

INSTRUMENT_RAZMETKA = ['РИ Кернер 7843-0031  Н12.Х1 ГОСТ 7213-72',
                       'ВИ Разметочный циркуль ГОСТ 24472-80',
                       'ВИ Чертилка 7840-1011 ГОСТ 24473-80',
                       'СИ Линейка - 1000 ГОСТ 427-75']

OPERATIONS = []

with open('files/operations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        OPERATIONS.append(item)

OPERATIONS_SBORKA = []
with open('files/operations_sborka.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for item in data:
        OPERATIONS_SBORKA.append(item)

DETAILS = {}
with open('files/details.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    data = dict(sorted(data.items()))
    DETAILS = data

DEISTVIYA = []
with open('files/deistvia.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for r in rows:
        DEISTVIYA.append(r[0])

PROBKI_GLADKIE = {}
with open('files/probki-gladkie.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    for r in rows:
        key = r['Диаметр']
        PROBKI_GLADKIE[float(key)] = r['Описание']
PROBKI_REZBA = []
with open('files/probki-rezba.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for key in rows:
        PROBKI_REZBA.append(key[0])
KOLCA_REZBA = []
with open('files/kolca_rezba.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for key in rows:
        KOLCA_REZBA.append(key[0])
KOLCA_REZBA_NEPROHOD = []
with open('files/kolca_rezba_neprohod.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    for key in rows:
        KOLCA_REZBA_NEPROHOD.append(key[0])

REZHIMI = {}
with open('files/rezhimi.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    for r in rows:
        REZHIMI[r['Материалы']] = {'отрезная': float(r['Отрезная']),
                                   'токарная': {'точение': {'скорость': float(r['Токарная_скорость_точение']),
                                                            'подача': float(r['Токарная_подача_точение'])
                                                            },
                                                'канавка': {'скорость': float(r['Токарная_скорость_канавка']),
                                                            'подача': float(r['Токарная_подача_канавка'])
                                                            },
                                                'подрезка': {'скорость': float(r['Токарная_скорость_подрезка']),
                                                             'подача': float(r['Токарная_подача_подрезка'])}
                                                }
                                   }
REZHIMI_SVERLENIE = {}
with open('files/rezhimi_sverlenie_podacha.csv', 'r', encoding='utf-8') as file, open('files/rezhimi.csv', 'r', encoding='utf-8') as file_2:
    rows = csv.DictReader(file)
    REZHIMI_SVERLENIE = {'подача': {}, 'скорость': {}}
    for r in rows:
        diameters = tuple(map(int, r['Диаметр'].split('–')))
        REZHIMI_SVERLENIE['подача'][diameters] = {'Конструкционные стали':float(r['Конструкционные стали']),
                                           'Легированные и улучшаемые стали': float(r['Легированные и улучшаемые стали']),
                                           'Нержавеющие и жаропрочные стали': float(r['Нержавеющие и жаропрочные стали']),
                                           'Чугун': float(r['Чугун']),
                                           'Алюминиевые сплавы': float(r['Алюминиевые сплавы']),
                                           'Цветные металлы': float(r['Цветные металлы'])}
    rows = csv.DictReader(file_2)
    for r in rows:
        REZHIMI_SVERLENIE['скорость'][r['Материалы']] = float(r['Сверлильная_скорость'])

REZHIMI_SHLIFOVKA = {}
with open('files/rezhimi.csv', 'r', encoding='utf-8') as file:
    rows = csv.DictReader(file)
    for r in rows:
        REZHIMI_SHLIFOVKA[r['Материалы']] = {'скорость': float(r['Шлифовальная_скорость']),
                                             'подача': float(r['Шлифовальная_подача'])}
