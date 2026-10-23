import pyautogui
import math

def find_region():
    print('Наведите на левый верхний угол')
    input()
    x, y = pyautogui.position()
    print('Левый угол:', x, y )
    print('Наведите на правый нижний угол')
    input()
    x2, y2 = pyautogui.position()
    print('Правый нижний угол:', x2, y2 )
    width = x2 - x
    height = y2 - y
    print(f'region=({x}, {y}, {width}, {height})')


num = 'Н11.696.01.000'

print(num.isalnum())

