import time

import keyboard
import pyperclip

from logic.operation_base import OperationBase
from logic.automation import TechnoproAutomation
import pyautogui


class TehnoIot(OperationBase):
    def __init__(self):
        super().__init__()
        self.tehno = TechnoproAutomation()
        self.region_instruments = (844, 299, 686, 185)
        self.ADD_INSTRUMENT_BUTTON_STAR = 'logic/find_operations/add_moving_position.png'
        self.ADD_INSTRUMENT_BUTTON_ARROW = 'logic/find_operations/add_instrument_arrow.png'
        self.BUTTON_CLOSE = 'logic/find_operations/button_close.png'


    def find_operation(self):
        data = []
        for operation in self.operations_tehno:
            d = {'описание': '', 'иот': '', 'оборудование': None}
            try:
                matches = pyautogui.locateAllOnScreen(image=operation['кнопка'], confidence=0.9, region=self.tehno.REGION_TABLE)
                print('---------')
                print(f'{operation['операция']} - {len(list(matches))} шт.')
                if matches:
                    d['описание'] = operation['операция']
                    d['иот'] = operation['иот']
                    d['оборудование'] = operation['оборудование']
                    data.append(d)
            except:
                continue
        return data

    def start(self, d:dict, no_find:list, status:bool):
        delete_old_element = status
        time.sleep(1)
        data = self.operations_tehno
        for item in data:
            for key, value in d.items():
                if item['операция'] == key:
                    item['оборудование_полученное'] = value

        for item in data:
            if item['операция'] in no_find:
                continue
            try:
                matches = pyautogui.locateAllOnScreen(image=item['кнопка'],
                                                      confidence=0.9,
                                                      region=self.tehno.REGION_TABLE
                                                      )

                for match in matches:
                    count = 0
                    center_x, center_y = pyautogui.center(match)
                    pyautogui.click(center_x, center_y)
                    time.sleep(1.5)
                    iot = self.find_and_click(image=item['иот']['изображение_иот'])
                    if iot == 0:
                        self.click_add_instrument(text_input=item['иот']['текст_иот'])
                    if delete_old_element:
                        for img in item['оборудование']:
                            point = self.find_and_click(image=img[1], is_delete=delete_old_element)
                            if point == 0:
                                self.click_add_instrument(text_input=item['оборудование_полученное'])
                                break
                    else:
                        for img in item['оборудование']:
                            point = self.find_and_click(image=img[1])
                            count += point
                        if count == 0:
                            self.click_add_instrument(text_input=item['оборудование_полученное'])
                    pyautogui.click(center_x + 100, center_y)
                    keyboard.press('enter')
                    time.sleep(0.5)

            except:
                continue
    def find_and_click(self, image, is_delete:bool=False):
        try:
            img = pyautogui.locateOnScreen(image=image,
                                           confidence=0.75,
                                           region=self.region_instruments,
                                           )
            if is_delete:
                pyautogui.click(pyautogui.center(img))
                arrow_instrument_old = pyautogui.locateOnScreen(image=self.ADD_INSTRUMENT_BUTTON_ARROW,
                                                                confidence=0.75,
                                                                region=self.region_instruments)
                time.sleep(0.5)
                pyautogui.click(pyautogui.center(arrow_instrument_old))
                keyboard.press('delete')
                time.sleep(0.5)
                keyboard.press('enter')
                time.sleep(0.5)
                return 0
            time.sleep(1)
            return 1
        except:
            return 0


    def click_add_instrument(self, text_input):
        try:
            button_add = pyautogui.locateOnScreen(image=self.ADD_INSTRUMENT_BUTTON_STAR,
                                                  confidence=0.75,
                                                  region=self.region_instruments,
                                                  )
            time.sleep(1)
            center_x, center_y = pyautogui.center(button_add)
            pyautogui.click(center_x + 100, center_y)
            time.sleep(0.5)
            pyperclip.copy(text_input)
            print(f'Добавляю - {text_input}')
            time.sleep(0.5)
            keyboard.press_and_release('ctrl+v')
            time.sleep(0.8)
            return
        except:
            button_add_arrow = pyautogui.locateOnScreen(image=self.ADD_INSTRUMENT_BUTTON_ARROW,
                                                        confidence=0.75,
                                                        region=self.region_instruments,
                                                        )
            time.sleep(1)
            center_x, center_y = pyautogui.center(button_add_arrow)
            pyautogui.click(center_x + 100, center_y)
            time.sleep(0.5)
            pyperclip.copy(text_input)
            print(f'Добавляю - {text_input}')
            time.sleep(0.5)
            keyboard.press_and_release('ctrl+v')
            time.sleep(0.8)
            return



