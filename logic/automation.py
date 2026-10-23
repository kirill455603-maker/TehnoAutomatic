# logic/automation.py
import time
import pyautogui
import keyboard
import pyperclip
import pyscreeze



class TechnoproAutomation:
    # Все магические координаты собраны в одном месте
    REGION_TABLE = (31, 226, 554, 673)
    REGION_ADD_OP = (31, 226, 554, 673)
    REGION_MOVING_DETAL = (862, 452, 418, 195)
    REGION_MOVING_SBORKA = (843, 396, 508, 196)
    REGION_ARROW_SBORKA = (821, 272, 267, 135)
    IMAGE_FIND = 'logic/image_find/tok_find.PNG'
    IMAGE_ADD_OP = 'logic/image_find/find_add_operation.PNG'
    IMAGE_MOVING = 'logic/image_find/add_moving_position.png'
    IMAGE_ADD_MOVING_TWO = 'logic/image_find/add_moving_position_2.png'
    IMAGE_BUTTON_TEXT_SBORKA = 'logic/image_find/button_text_sborka.png'


    def take_value_matches(self, image_find) -> int:
        try:
            matches = len(list(pyautogui.locateAllOnScreen(
                image=image_find, region=self.REGION_TABLE, confidence=0.9)))
            return matches
        except (pyautogui.ImageNotFoundException, pyscreeze.ImageNotFoundException):
            return 0

    def _find_and_click(self, image, region, offset_x=0, offset_y=0, image_two=None):
        try:
            btn = pyautogui.locateOnScreen(image, confidence=0.8, region=region)
            cx, cy = pyautogui.center(btn)
            pyautogui.click(cx + offset_x, cy + offset_y)
            time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print(f'ОШИБКА | Кнопка {image} не найдена.')



    def _find_and_click_add_instrument(self, image, image_two, region, offset_x=0, offset_y=0):
        try:
            btn = pyautogui.locateOnScreen(image, confidence=0.8, region=region)
        except pyautogui.ImageNotFoundException:
            btn = pyautogui.locateOnScreen(image_two, confidence=0.8, region=region)
        cx, cy = pyautogui.center(btn)
        pyautogui.click(cx + offset_x, cy + offset_y)
        time.sleep(2)
        pyautogui.click(cx + offset_x, cy + offset_y)


    def start(self, operations: dict, index: int, image_find):
        #Нашли кнопку
        matches = list(pyautogui.locateAllOnScreen(
            image=image_find, region=self.REGION_TABLE, confidence=0.9))
        if not matches:
            return

        for key in operations:
            if 'описание' not in operations[key]:
                continue

            x, y = pyautogui.center(matches[index])
            pyautogui.click(x, y)
            keyboard.press('enter')
            time.sleep(3.5)

            pyautogui.click(x, y, button='right')
            time.sleep(2)
            self._find_and_click(self.IMAGE_ADD_OP, self.REGION_ADD_OP)
        #Понимаем, сборка перед нами или деталь
            try:
                match = pyautogui.locateOnScreen(image='logic/find_operations/find_button_sborka.PNG', confidence=0.8, region=self.REGION_ARROW_SBORKA)
                print('Это сборочная деталь')
                pyautogui.click(x=1189, y=348)
                time.sleep(0.5)
                pyautogui.click(x=947, y=221)
                time.sleep(0.5)

                pyperclip.copy(operations[key]['описание'].text())
                time.sleep(0.5)
                keyboard.press_and_release('ctrl+v')
                time.sleep(0.5)
                try:
                    if operations[key]['инструмент']:
                        for value in operations[key]['инструмент'].text().split('\n'):
                            self._find_and_click_add_instrument(
                                self.IMAGE_MOVING, self.IMAGE_ADD_MOVING_TWO, self.REGION_MOVING_SBORKA,
                                offset_x=100, offset_y=5
                            )
                            pyperclip.copy(value)
                            time.sleep(1)
                            keyboard.press_and_release('ctrl+v')
                            pyautogui.click(x=744, y=250)
                            time.sleep(1)
                except:
                    pyautogui.click(x, y)
                    time.sleep(1)
                    keyboard.press('enter')
                pyautogui.click(x, y)
                time.sleep(1)
                keyboard.press('enter')
            except:
                print('Это не сборочная деталь')
                pyautogui.click(1216, 305)
                pyautogui.click(1216 + 150, 305)
                time.sleep(0.5)

                pyperclip.copy(operations[key]['описание'].text())
                time.sleep(0.5)
                keyboard.press_and_release('ctrl+v')

                if operations[key]['инструмент']:
                    for value in operations[key]['инструмент'].text().split('\n'):
                        self._find_and_click_add_instrument(
                            self.IMAGE_MOVING, self.IMAGE_ADD_MOVING_TWO, self.REGION_MOVING_DETAL,
                            offset_x=100, offset_y=5
                        )
                        pyperclip.copy(value)
                        time.sleep(1)
                        keyboard.press_and_release('ctrl+v')
                        pyautogui.click(x=744, y=250)
                        time.sleep(1)

                pyautogui.click(x, y)
                time.sleep(1)
                keyboard.press('enter')







