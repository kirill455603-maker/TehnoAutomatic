import json

file_path = 'operations.json'
def add_operation():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Если файл пустой или не существует, создаем пустой список
    while True:
        s = input()
        if s == 'стоп':
            break

        d = {'операция': input('Операция: '),
             'кнопка': input('Кнопка: '),
             'иот': {'текст_иот': input('текст_ИОТ: '),
                     'изображение_иот': input('изображение_ИОТ: ')},
             'оборудование': [(input('Оборудование_текст: '), input('Оборудование_изображние: '))],
             'оборудование_полученное': None,
             }
        data.append(d)

    # 3. Перезаписываем файл
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_instrument():
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        s = input('Название операции: ')
        d = [input('Название оборудования: '), input('Ссылка на изображение оборудования: ')]
        for item in data:
            if item['операция'].lower() == s.lower():
                item['оборудование'].append(d)
                break

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_key():
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            item['оборудование_полученное'] = None
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_operation_sborka():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []  # Если файл пустой или не существует, создаем пустой список
    while True:
        s = input()
        if s == 'стоп':
            break

        d = {'операция': input('Операция: '),
             'кнопка': input('Кнопка: '),
             }
        data.append(d)

    # 3. Перезаписываем файл
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def add_word_with_form():
    try:
        with open('details.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        data = {}
    while True:
        s = input('Слово или "стоп": ')
        if s == 'стоп':
            break
        data[s] = {'именительный': input('именительный (Кто? Что?): '),
                                  'родительный': input('родительный (Кого? Чего?): '),
                                  'дательный': input('дательный (Кому? Чему?): '),
                                  'винительный': input('винительный (Кого? Что?): '),
                                  'творительный': input('творительный (Кем? Чем?): '),
                                  'предложный': input('предложный (О ком? О чем?): ')
                                  }
    with open('details.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

add_instrument()