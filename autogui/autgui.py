import pyautogui
import time

# time.sleep(2)


def send_input_gui(string):
    c1, c2 = string.split('+')
    if c2 != '':
        pyautogui.hotkey(c1, c2)
    else:
        pyautogui.press(c1)
