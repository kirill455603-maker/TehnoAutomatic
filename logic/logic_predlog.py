from datetime import date, datetime
import os

class LogicPredlog:
    def save_result(self, d):
        file_name = f'{date.today()}'
        now_date = datetime.now()
        os.makedirs('my_folder',exist_ok=True)
        with open(f'my_folder/{file_name}.txt', 'a', encoding='utf-8') as f:
            f.write(f'\n{'-' * 9} {d['тема'].upper()} {'-' * 9}')
            f.write(f'\nДата и время отправки: {now_date}')
            f.write(f'\nОт: {d['имя'].title()}')
            f.write(f'\nПредложение: {d['предложение']}')
            f.write(f'\n')
