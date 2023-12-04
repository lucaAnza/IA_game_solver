import pyautogui
import time
import pyautogui
import datetime
import os
import time


# Funzione che esegue uno screenshot
def take_screenshot(x=0, y=0, width=500, height=500, label="", debug=False, fullScreen=False):
    script_name = 'screenBot.py'

    if (fullScreen):
        screenshot = pyautogui.screenshot()
    else:
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

    current_directory = os.path.abspath(__file__)
    path_from_current_dir = f"../Screenshot/screenshot{label}.png"
    file_path = str(current_directory[:-len(script_name)
                                      ].replace('\\', '/')) + str(path_from_current_dir)
    screenshot.save(file_path)
    if (debug):
        print(f"Screenshot salvato in: {file_path}")
        if (fullScreen):
            print(f"Eseguito fullscreen!")
        else:
            print(f"Screen [x={x},y={y}] , Size(H,W) = {height,width}")
    return file_path


# Funzione che salva tante immgini in modo tale da capire la più adatta
def analysis_screenshot():

    x = 1
    y = 1
    moltiplicatore = 300
    for i in range(3):
        for j in range(3):
            x = moltiplicatore * i
            y = moltiplicatore * j
            print(f"screen x = {x}, y = {y} : {i}{j}")
            take_screenshot(x, y, label=f'{i}{j}')


if (__name__ == '__main__'):        # Controlla se è eseguita direttamente

    attesa = 5
    for i in range(attesa):
        print(f"Screen tra {attesa-i} secondi...")
        time.sleep(1)

    take_screenshot(870, 330, 490, 620, debug=True)
