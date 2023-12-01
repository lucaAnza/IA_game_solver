import pyautogui
import time

print("avvio sleep timer...")
time.sleep(5)

comandi = ["up", "right", "down", "left"]
for i in range(30):
    print("esecuzione n.", i+1)
    for _ in comandi:
        print(f'Exex {_}')
        pyautogui.press(_)

    print("end of iteration")
