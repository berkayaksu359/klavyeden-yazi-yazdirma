import pyautogui
import time

def press_keys():
    pyautogui.press('win')
    pyautogui.typewrite('opera')
    pyautogui.press('enter')

opera_acan = input("Opera GX i açmak istiyorsanız (opera gx) yazın: ")

if opera_acan.lower() == "opera gx":
    press_keys()