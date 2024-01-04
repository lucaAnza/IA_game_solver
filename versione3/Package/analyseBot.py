import cv2
import numpy as np
import sys
import time
import os

if __name__ == "__main__":
    import solverBot
    import decoratori
    import screenBot
else:
    from Package import solverBot
    from Package import decoratori
    from Package import screenBot

# GLOBALS

sfondo_R = (200, 250)
sfondo_G = (180, 220)
sfondo_B = (180, 230)

# Dimensione matrice
num_righe = solverBot.num_righe
num_colonne = solverBot.num_colonne


default_name = {
    'hat': 1,
    'iced_hat': 1,
    'skate': 2,
    'iced_skate': 2,
    'pizza': 3,
    'iced_pizza': 3,
    'can': 4,
    'iced_can': 4,
    'star': 5,
    'Unknown_Item': 0
}


# Stampa una matrice di numrighe,numcolonne elementi
def print_matrix(matrix):

    for i in range(num_righe):
        for j in range(num_colonne):
            print(str(matrix[i][j]), end=" ")
        print()



# True -> matrice senza unknown elements   False -> matrice con elementi sconosciuti
def checkMatrixProduct(matrix):

    prod = 1
    for i in range(num_righe):
        for j in range(num_colonne):
            prod *= int(matrix[i][j])

    return prod

# Data un immagine restituisce la matrice degli item
@decoratori.timestamp_decorator
def get_matrix_item(immagine , type = "String" ,debug = False, x=5, y=20, side=93):

    m_string = [ [] , [] , [] , [] , [] , [] ]
    m_number = [ [] , [] , [] , [] , [] , [] ]
    
    m_string = screenBot.set_grill(immagine , (x,y) , square_side=side , matrix=True)
    
    #cv2.imwrite("Screenshot/output_paint.png" , immagine)   Stampa la matrice con la griglia

    if(debug):
        # Mostra l'immagine e imposta la funzione di callback del mouse
        altezza, larghezza, _ = immagine.shape
        print(f'height : {altezza} , width : {larghezza}')
        cv2.imshow('Immagine', immagine)
        cv2.setMouseCallback('Immagine', screenBot.click_event)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

    if(type == "String"):
        return m_string
    elif(type == 'Number'):
        for i in range(num_righe):
            for j in range(num_colonne):
                m_number[i].append(default_name[m_string[i][j]])
        return m_number
    else:
        print("Error type on function [get_item_matrix]")





# MAIN
if (__name__ == "__main__"):

    inizio = time.time()


    nome_file_immagine = "./Screenshot/screenshotkz32.png"
    immagine = cv2.imread(nome_file_immagine)

    # Verifica che l'immagine sia stata caricata correttamente
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        current_directory = os.path.abspath(__file__)
        print(f'Directory corrente : {current_directory}')
        sys.exit()
        
    
    #matrix_number = get_matrix_item(immagine , type="Number" , x = 5 , y = 20 , side = 93)   # Lucas-pc
    #matrix_number = get_matrix_item(immagine , type="Number" , x = 9 , y = 23 , side = 94)   # Chris-pc
    
    matrix_number = get_matrix_item(immagine , type="Number" , x = 5 , y = 20 , side = 93)  # Used for test
    print_matrix(matrix_number)

    script_name = sys.argv[0]
    fine = time.time()
    tempo_esecuzione = fine - inizio
    print(
        f"La funzione '{script_name}' ha impiegato {tempo_esecuzione:.4f} secondi.")
