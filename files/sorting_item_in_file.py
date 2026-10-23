import csv
def start_sorting(file_name:str, file_name_sort):
    with open(file_name, 'r', encoding='utf-8') as file_r, open(file_name_sort, 'w', encoding='utf-8', newline='') as file_w:
        reader = list(csv.DictReader(file_r))
        result = sorted(reader, key=lambda x: float(x['Диаметр']))
        print(result)

        writer = csv.writer(file_w)
        columns = ['Диаметр', 'Наименование']
        data = []
        for r in result:
            temp = [r['Диаметр'], r['Наименование']]
            data.append(temp)
        writer.writerow(columns)
        for row in data:
            writer.writerow(row)
start_sorting('sverla.csv', 'sort_sverla.csv')