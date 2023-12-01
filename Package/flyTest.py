import time
import pyautogui

start_time = time.time()
c1 = 'ctrl'
c2 = 'v'
pyautogui.hotkey(c1, c2, interval=0.05)
end_time = time.time()

print(f"Tempo impiegato: {end_time - start_time} secondi")