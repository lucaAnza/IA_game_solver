import pyautogui
from colorama import Fore, Style
import os
import cv2
import time

if __name__ == "__main__" or __name__ == 'solverBot':
    import decoratori
    import print_coloured as p
    import solverBot
else:
    from Package import decoratori
    from Package import print_coloured as p
    from Package import solverBot


# Setting
os.system("color")  # abilita i colori nella shell



# Clicca lo schermo ogni <interval> secondi. Eseguendo la <macro>
def click_same_point(interval = 3 , macro = 'alt+2' , max_iteration = 1000 ):

    print(f"\n--------------------------------")
    print(f"Avvio cliccatore automatico...")
    print(f'Macro set : {macro}')
    print(f'Time set : {interval}s')
    print(f"--------------------------------")

    for i in range(max_iteration):
        solverBot.send_input_gui(macro)
        time.sleep(interval)


def click_continue_game():
    print("Clicco 'Continua il gioco' ")
    macro = 'alt+9'
    solverBot.send_input_gui(macro)


  
# MAIN
if (__name__ == '__main__'):
    
    attesa = 3
    for i in range(attesa):
        print(f"Screen tra {attesa-i} secondi...")
        time.sleep(1)

    click_same_point()