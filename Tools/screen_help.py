import pyautogui
import time
import pyautogui
import datetime
import os
import time
import cv2
import sys


#Informazioni utili

# Pixel attuale : x = 870, y = 330, height = 490, width = 620
# Ritaglio : x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
#            immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza] 
# Pixel ipotetico x = 886 , y = 360 , height = 455 , width = 546 -> (886,360,455,546)


#Funzione che esegue uno screenshot
def take_screenshot( x = 0 , y = 0 , width = 500 , height = 500 , label = "" , debug = False  , fullScreen = False):
    script_name='screen_help.py'

    if(fullScreen):
        print("fatto Fullscreen!")
        screenshot = pyautogui.screenshot()
    else:
        print("fatto Screen parziale!")
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
    
    current_directory = os.path.abspath(__file__)
    path_from_current_dir = f"../Screenshot/screenshot{label}.png"
    file_path = str(current_directory[:-len(script_name)].replace('\\' , '/')) + str(path_from_current_dir)     
    screenshot.save(file_path)
    if(debug):
        print(f"Screenshot salvato in: {file_path}")
    return file_path


        
#Funzione che salva tante immgini in modo tale da capire la più adatta
def analysis_screenshot():
    
    x = 1
    y = 1
    moltiplicatore = 300
    for i in range(3):
        for j in range(3):
            x = moltiplicatore * i
            y = moltiplicatore * j
            print(f"screen x = {x}, y = {y} : {i}{j}")
            take_screenshot(x , y , label=f'{i}{j}')



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'\nCoordinate del pixel: ({x}, {y})')

  


 
if ( __name__ == '__main__'):        # Controlla se è eseguita direttamente

    attesa = 3
    for i in range(attesa):
        print(f"Screen tra {attesa-i} secondi...")
        time.sleep(1)
    #x = 870, y = 330, height s= 490, width = 620
    path = take_screenshot(866,333,501,627,debug=True,fullScreen=False, label='[HELP]')
    immagine = cv2.imread(path)

    # Verifica che l'immagine sia stata caricata correttamente
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()

    # Mostra l'immagine e imposta la funzione di callback del mouse
    cv2.imshow('Immagine', immagine)
    cv2.setMouseCallback('Immagine', click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 


