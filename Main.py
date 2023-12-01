import cv2
import numpy as np
import sys
import time
import pyautogui
import datetime
import os
import pyautogui
from colorama import Fore, Style
import pyfiglet
from Package import *



#Setting
os.system("color") #abilita i colori nella shell

#Globals
num_righe = solverBot.num_righe      
num_colonne = solverBot.num_colonne   

#Decoratore
def tempo_di_esecuzione(funzione):
    def wrapper(*args, **kwargs):
        inizio = time.time()
        risultato = funzione(*args, **kwargs)
        fine = time.time()
        tempo_esecuzione = fine - inizio
        print(f"La funzione '{funzione.__name__}' ha impiegato {tempo_esecuzione:.4f} secondi.")
        return risultato
    return wrapper

    


#MAIN 
print("\n\n")
testo = "Game Solver"
fig = pyfiglet.Figlet()
ascii_art = fig.renderText(testo)
print(f"{Fore.GREEN} {ascii_art} {Style.RESET_ALL}", end='')
# print(f"{Fore.GREEN}Developed by lanza & manillin !{Style.RESET_ALL}")
print("\n\n")
print(f"{Fore.GREEN}Press S to start! {Style.RESET_ALL}", end='')
fuck_it_we_ball = input("")
if fuck_it_we_ball != 's':
    print(f"{Fore.RED}Script terminated...{Style.RESET_ALL}")
    sys.exit(1)
print("Starting...")
time.sleep(2)


consecutive_error = 0
while(consecutive_error < 100):
    time.sleep(0.1)
    #Cattura screenshot
    label = 'kz32'
    screenBot.take_screenshot(870,330,490,620, label)
    img_name = f"Screenshot/screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()
    #Ritaglio immagine, per adattarla al secondo taglio
    x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
    immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza] 
    
    #Crea la matrice di item e numeri
    matrix_img = solverBot.matrix_from_img(immagine_ritagliata , 200 , open_img = False)
    matrix_item = [ [] , [] , [] , [] , [] , [] ]
    matrix_number = [ [] , [] , [] , [] , [] , [] ]
    for i in range(num_righe):
        for j in range(num_colonne):
            res = analyseBot.analizza_immagine(matrix_img[i][j] , debug=False)
            matrix_item[i].append(res)
            matrix_number[i].append(analyseBot.default_name[str(res)])
    
    if(analyseBot.checkMatrix(matrix_number)):
        print(f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')
        consecutive_error_count=0
        solverBot.scan_matrice(matrix_number)
    else:
        print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
        consecutive_error+=1

