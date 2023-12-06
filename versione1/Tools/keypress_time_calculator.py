import time
import pyautogui
from colorama import Fore, Style


start_time = time.time()
c1 = 'ctrl'
c2 = 'v'
c3 = 'a'
# pyautogui.hotkey(c1, c2, interval=0.01)
pyautogui.press(c3, interval=0.04)
end_time = time.time()
print(f"{Fore.YELLOW}Tempo impiegato: {end_time - start_time} secondi{Style.RESET_ALL}")

print("merge")
