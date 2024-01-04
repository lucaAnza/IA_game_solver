import pyautogui
import time
import pyautogui
import datetime
import os
import time
import cv2
import sys

# GRILL-LUCA ->  top_left = (5,20) , square_side = 93
# GRILL-CRI  ->  ...


# Funzione che esegue uno screenshot
def take_screenshot(x=0, y=0, width=500, height=500, label="", debug=False, fullScreen=False):
    script_name = 'screen_help.py'

    if (fullScreen):
        print("fatto Fullscreen!")
        screenshot = pyautogui.screenshot()
    else:
        print("fatto Screen parziale!")
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

    current_directory = os.path.abspath(__file__)
    path_from_current_dir = f"../Screenshot/screenshot{label}.png"
    file_path = str(current_directory[:-len(script_name)
                                      ].replace('\\', '/')) + str(path_from_current_dir)
    screenshot.save(file_path)
    if (debug):
        print(f"Screenshot salvato in: {file_path}")
    return file_path


#Funzione che stampa le coordinate del pixel cliccato
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'\nCoordinate del pixel: ({x}, {y})')


#Funzione che definisce una griglia su un immagine
def set_grill(immagine, top_left=(0, 0), square_side=40, righe=6, colonne=5):

    color_square = (0, 0, 255)  # Colore in formato BGR (rosso)
    color_dot = (255, 0, 0)
    thickness_square = 2
    thickness_dot = 1

    # Creazione griglia
    top_lx = top_left
    bot_rx = (top_lx[0] + square_side, top_lx[1] + square_side)
    x_centro = (top_lx[0] + bot_rx[0]) // 2
    y_centro = (top_lx[1] + bot_rx[1]) // 2
    for i in range(righe):
        for j in range(colonne):
            cv2.rectangle(immagine, top_lx, bot_rx,
                          color_square, thickness_square)
            cv2.rectangle(immagine, (x_centro, y_centro),
                          (x_centro, y_centro), color_dot, thickness_dot)
            print(
                f'point pixel -> [{i,j}] - [x={x_centro},y={y_centro}] {immagine[y_centro,x_centro]}')
            # slide top_left  x ----> x2 -----> xn
            top_lx = (top_lx[0]+square_side, top_lx[1])
            bot_rx = (top_lx[0] + square_side, top_lx[1] +
                      square_side)   # adattamento bottom_right
            x_centro = (top_lx[0] + bot_rx[0]) // 2
            y_centro = (top_lx[1] + bot_rx[1]) // 2

        # slide top_left   y
        top_lx = (top_left[0], top_lx[1]+square_side)
        bot_rx = (top_lx[0] + square_side, top_lx[1] +
                  square_side)      # adattamento bottom_right
        x_centro = (top_lx[0] + bot_rx[0]) // 2
        y_centro = (top_lx[1] + bot_rx[1]) // 2



# Controlla se è eseguita direttamente
if (__name__ == '__main__'):        

    
    str_menu = "\nMenu:\n1. Fullscreen screenshot\n2. Cut screenshot + Set grill\n3+. Exit\n-> "
    scelta = int(input(str_menu))
    attesa = 4   # tempo attesa per screenshot



    if(scelta == 1):      # Fullscreen
        for i in range(attesa):
            print(f"Screen tra {attesa-i} secondi...")
            time.sleep(1)

        path = take_screenshot(870, 330, 490, 620,fullScreen=True, label='Full')
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
    elif(scelta == 2):
        for i in range(attesa):
            print(f"Screen tra {attesa-i} secondi...")
            time.sleep(1)
            
        path = take_screenshot(870, 330, 490, 620,fullScreen=True, label='Full')
        immagine = cv2.imread(path)
        set_grill(immagine, (5, 20), square_side=93)    # cambiare in base al pc
        cv2.imwrite("output.png", immagine)
        # Verifica che l'immagine sia stata caricata correttamente
        if immagine is None:
            print("Errore nel caricamento dell'immagine.")
            sys.exit()

        # Mostra l'immagine e imposta la funzione di callback del mouse
        cv2.imshow('Immagine', immagine)
        cv2.setMouseCallback('Immagine', click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Exit...")
    

 
