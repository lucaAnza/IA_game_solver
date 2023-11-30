import pyautogui
import time

time.sleep(2)
# pyautogui.hotkey("command", "v", interval=0.25)
S = 'command+m'
c1, c2 = S.split('+')
pyautogui.hotkey(c1, c2, interval=0.25)
print()
