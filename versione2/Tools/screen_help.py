import pyautogui
import time
import pyautogui
import datetime
import os
import time
import cv2
import sys

# SCREEN

""" PC LUCA """
# Pixel attuale : x = 870, y = 330, height = 490, width = 620
# Ritaglio : x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
#            immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]
""" PC CRISTIAN """
# screenBot.take_screenshot(866,333,501,627, label)
# Ritaglio : x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
#            immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]

""" PC Luca senza taglio """
# Pixel ipotetico x = 886 , y = 360 , height = 455 , width = 546 -> (886,360,455,546)

# GRILL1  ->     top_left = (5,20) , square_side = 94
# GRILL-LUCA ->     top_left = (5,20) , square_side = 93


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


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'\nCoordinate del pixel: ({x}, {y})')


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

    # Old version -> #cv2.circle(immagine, (x_centro, y_centro), thickness_dot, color_dot ,-1)


if (__name__ == '__main__'):        # Controlla se è eseguita direttamente

    attesa = 1
    for i in range(attesa):
        print(f"Screen tra {attesa-i} secondi...")
        time.sleep(1)

    # path = take_screenshot(866,333,501,627,debug=True,fullScreen=False, label='[HELP]')
    # immagine = cv2.imread(path)

    immagine = cv2.imread("./screenshotkz32.png")
    set_grill(immagine, (9, 23), square_side=94)    # cambiare per pc luca
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
