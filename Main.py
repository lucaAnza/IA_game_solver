import cv2
import numpy as np
import sys
import time
import datetime
import os
from colorama import Fore, Style
import pyfiglet
from Package import *



#Setting
os.system("color") #abilita i colori nella shell

#Globals
num_righe = solverBot.num_righe      
num_colonne = solverBot.num_colonne   


@decoratori.timestamp_decorator
def fill_Item_Matrix(string_matrix , int_matrix):
    found_unknown_item = False
    for i in range(num_righe):
        for j in range(num_colonne):
            res = analyseBot.analizza_immagine(matrix_img[i][j] , debug=False)
            int_matrix[i].append(analyseBot.default_name[str(res)])
            if(int(analyseBot.default_name[str(res)]) == 0):
                found_unknown_item = True
                break
        if(found_unknown_item):
            break
    
    return found_unknown_item


    
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
general_counter = 0
old_product = 0
while(consecutive_error < 100):
    found_unknown_item = False
    print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}")
    start_time = datetime.datetime.now()  #debugging tempo

    #screenBot.take_screenshot(870,330,490,620, label)
    #Ritaglio immagine, per adattarla al secondo taglio
    #x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
    #immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]


    #Cattura screenshot
    label = 'kz32'
    screenBot.take_screenshot(870,330,490,620, label)
    img_name = f"Screenshot/screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()
    
    #Ritaglio
    x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
    immagine = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]
    #Crea la matrice di item e numeri
    matrix_img = solverBot.matrix_from_img(immagine , 200 , open_img = False)
    matrix_item = [ [] , [] , [] , [] , [] , [] ]
    matrix_number = [ [] , [] , [] , [] , [] , [] ]
    found_unknown_item = fill_Item_Matrix(matrix_item , matrix_number)


    """OPTION2

    #Cattura screenshot
    label = 'kz32'
    screenBot.take_screenshot(886,360,455,546, label)
    img_name = f"Screenshot/screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()
    
    #Crea la matrice di item e numeri
    matrix_img = solverBot.matrix_from_img(immagine , 200 , open_img = False)
    matrix_item = [ [] , [] , [] , [] , [] , [] ]
    matrix_number = [ [] , [] , [] , [] , [] , [] ]
    found_unknown_item = fill_Item_Matrix(matrix_item , matrix_number)

    """
    

    if(not(found_unknown_item)):     #Se almeno un elemento non l'ha riconosciuto [ prod == 0] non entra.
        #Debug analisi
        print(f"\n{Fore.YELLOW}Matrix id_item: ")
        analyseBot.print_matrix(matrix_number)
        print(f"{Style.RESET_ALL}\n")
        
        product = analyseBot.checkMatrixProduct(matrix_number)   # ritorna il prodotto di tutti gli elementi della matrice
        
        if(product):   
            print(f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')
            consecutive_error=0
            solverBot.scan_matrice(matrix_number)
            if( old_product == product):   # check per evitare di essere bloccato in una stessa pagina
                consecutive_error+=1
            else:
                old_product = product
        else:
            print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
            consecutive_error+=1
    else:
        print(f"\n{Fore.YELLOW}Parzial Matrix id_item:\n{matrix_number}")
        print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
        consecutive_error+=1

    

    end_time = datetime.datetime.now()
    exe_time = end_time-start_time
    print(f"{Fore.CYAN}Tempo esecuzione WHILE : {exe_time}{Style.RESET_ALL}")
    print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}\n\n")
    general_counter+=1



