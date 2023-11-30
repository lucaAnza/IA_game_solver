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


#GLOBALS

sfondo_R = (200,250)
sfondo_G = (180,220)
sfondo_B = (180,230)

# Dimensione matrice
num_righe = 6
num_colonne = 5
offset = 100
delay_key = 0.3



#Struttura dati che tiene i dati di check ( Green , Red )
defalt_pixel = { 
    'hat' : (42,41) ,
    'iced_hat' : (47,61) ,
    'skate' : (29,33) ,
    'iced_skate' : (32,41) ,
    'pizza' : (26,21) ,
    'iced_pizza' : (25,45) ,
    'can' : (39,18) ,
    'iced_can' : (28,56) ,
    'star' : (20,11) }

default_name = {
    'hat' : 1 ,
    'iced_hat' : 1 ,
    'skate' : 2 ,
    'iced_skate' : 2 ,
    'pizza' : 3 ,
    'iced_pizza' : 3 ,
    'can' : 4 ,
    'iced_can' : 4 ,
    'star' : 5 ,
    'Unknown_Item' : 0
}

dizionario_movimenti = {
    # R0
    'M[0][0] basso': 'a+',
    'M[0][0] dx': 'b+',
    'M[0][1] sx': 'c+',
    'M[0][1] basso': 'd+',
    'M[0][1] dx': 'e+',
    'M[0][2] sx': 'f+',
    'M[0][2] basso': 'g+',
    'M[0][2] dx': 'h+',
    'M[0][3] sx': 'i+',
    'M[0][3] basso': 'j+',
    'M[0][3] dx': 'k+',
    'M[0][4] sx': 'l+',
    'M[0][4] basso': 'm+',
    # R1
    'M[1][0] basso': 'n+',
    'M[1][0] dx': 'o+',
    'M[1][0] alto': 'p+',
    'M[1][1] sx': 'q+',
    'M[1][1] basso': 'r+',
    'M[1][1] dx': 's+',
    'M[1][1] alto': 't+',
    'M[1][2] sx': 'u+',
    'M[1][2] basso': 'v+',
    'M[1][2] dx': 'x+',
    'M[1][2] alto': 'y+',
    'M[1][3] sx': 'z+',
    'M[1][3] basso': 'w+',
    'M[1][3] dx': '1+',
    'M[1][3] alto': '2+',
    'M[1][4] sx': '3+',
    'M[1][4] basso': '4+',
    'M[1][4] alto': '5+',
    # R2
    'M[2][0] basso': '6+',
    'M[2][0] dx': '7+',
    'M[2][0] alto': '8+',
    'M[2][1] sx': '9+',
    'M[2][1] basso': 'ctrl+a',
    'M[2][1] dx': 'ctrl+b',
    'M[2][1] alto': 'ctrl+c',
    'M[2][2] sx': 'ctrl+d',
    'M[2][2] basso': 'ctrl+e',
    'M[2][2] dx': 'ctrl+f',
    'M[2][2] alto': 'ctrl+g',
    'M[2][3] sx': 'ctrl+h',
    'M[2][3] basso': 'ctrl+i',
    'M[2][3] dx': 'ctrl+j',
    'M[2][3] alto': 'ctrl+k',
    'M[2][4] sx': 'ctrl+l',
    'M[2][4] basso': 'ctrl+m',
    'M[2][4] alto': 'ctrl+n',
    # R3
    'M[3][0] basso': 'ctrl+o',
    'M[3][0] dx': 'ctrl+p',
    'M[3][0] alto': 'ctrl+q',
    'M[3][1] sx': 'ctrl+r',
    'M[3][1] basso': 'ctrl+s',
    'M[3][1] dx': 'ctrl+t',
    'M[3][1] alto': 'ctrl+u',
    'M[3][2] sx': 'ctrl+v',
    'M[3][2] basso': 'ctrl+x',
    'M[3][2] dx': 'ctrl+y',
    'M[3][2] alto': 'ctrl+z',
    'M[3][3] sx': 'ctrl+0',
    'M[3][3] basso': 'ctrl+1',
    'M[3][3] dx': 'ctrl+2',
    'M[3][3] alto': 'ctrl+3',
    'M[3][4] sx': 'ctrl+4',
    'M[3][4] basso': 'ctrl+5',
    'M[3][4] alto': 'ctrl+6',

    # R4
    'M[4][0] basso': 'ctrl+7',
    'M[4][0] dx': 'ctrl+8',
    'M[4][0] alto': 'ctrl+9',
    'M[4][1] sx': 'alt+a',
    'M[4][1] basso': 'alt+b',
    'M[4][1] dx': 'alt+c',
    'M[4][1] alto': 'alt+d',
    'M[4][2] sx': 'alt+e',
    'M[4][2] basso': 'alt+f',
    'M[4][2] dx': 'alt+g',
    'M[4][2] alto': 'alt+h',
    'M[4][3] sx': 'alt+i',
    'M[4][3] basso': 'alt+j',
    'M[4][3] dx': 'alt+k',
    'M[4][3] alto': 'alt+l',
    'M[4][4] sx': 'alt+m',
    'M[4][4] basso': 'alt+n',
    'M[4][4] alto': 'alt+o',
    # R5
    'M[5][0] dx': 'alt+p',
    'M[5][0] alto': 'alt+q',
    'M[5][1] sx': 'alt+r',
    'M[5][1] dx': 'alt+s',
    'M[5][1] alto': 'alt+t',
    'M[5][2] sx': 'alt+u',
    'M[5][2] dx': 'alt+v',
    'M[5][2] alto': 'alt+w',
    'M[5][3] sx': 'alt+x',
    'M[5][3] dx': 'alt+y',
    'M[5][3] alto': 'alt+z',
    'M[5][4] sx': 'alt+1',
    'M[5][4] alto': 'alt+2',
}



#Classe per gli oggetti
class item:
    def __init__(self, green, red , nome = "General_item"):
        self.nome = nome
        self.green = green
        self.red = red
        self.sum = green+red
    
    def getItemType(self , debug = False):
        
        #Hat
        for incertezza in range (2,4) : 
            if self.__isInIntervall('hat',incertezza,debug):
                return "hat"
            elif self.__isInIntervall('skate',incertezza,debug):
                return "skate"
            elif self.__isInIntervall('pizza',incertezza,debug):
                return "pizza"
            elif self.__isInIntervall('can',incertezza,debug):
                return "can"
            elif self.__isInIntervall('star',incertezza,debug):
                return "star"
            elif self.__isInIntervall('iced_hat',incertezza,debug):
                return "iced_hat"
            elif self.__isInIntervall('iced_skate',incertezza,debug):
                return "iced_skate"
            elif self.__isInIntervall('iced_pizza',incertezza,debug):
                return "iced_pizza"
            elif self.__isInIntervall('iced_can',incertezza,debug):
                return "iced_can"
            
        return "Unknown_Item"
        
        
    
    def __isInIntervall(self  , type , incertezza ,debug = False):
        default_green = defalt_pixel[type][0]
        default_red = defalt_pixel[type][1]
        default_sum = default_green + default_red
        valutation = (  (abs(self.sum-default_sum) <= incertezza*2 ) and
                 (  (abs(self.green-default_green) <= incertezza) and (abs(self.red-default_red) <= incertezza) ) )
        if(debug):
            print(f"Type : {type}--------------")
            print(f"Incertezza : {incertezza}\nSum : {self.sum}\nDefault_sum = {default_sum}\nGreen/Default : {self.green}/{default_green}\nRed/Default : {self.red}/{default_red}" )
        """return   (  (abs(self.sum-default_sum) < incertezza*2 ) and
                 (  (abs(self.green-default_green) < incertezza) and (abs(self.red-default_red) < incertezza) ) )"""
            
        return valutation
            

#Funzione che esegue uno screenshot
def take_screenshot( x = 0 , y = 0 , width = 500 , height = 500 , label = "" , debug = False , name_script = "Main.py"):

    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    current_directory = os.path.abspath(__file__)
    name_script = "Main.py"
    file_path = str(current_directory[:-len(name_script)].replace('\\' , '/')) + str(f"screenshot{label}.png")     # 9 rappresenta la lunghezza del nome dello script -> screen.py
    screenshot.save(file_path)
    if(debug):
        print(f"Screenshot salvato in: {file_path}")


#Dato l'array dei pixel, scarta i pixel di sfondo e fa una media degli altri
def avg_channel(array , channel_type = 'R'):
    sum = 0
    if(channel_type == 'R'):
        indice = 2
        for i in array:
            elem = i[indice]
            if( not(elem >= sfondo_R[0] and elem <= sfondo_R[1] ) ):    # In questo modo scarta i pixel di sfondo
                sum = sum + elem
    elif(channel_type == 'G'):
        indice = 1
        for i in array:
            elem = i[indice]
            if( not(elem >= sfondo_G[0] and elem <= sfondo_G[1] ) ):    # In questo modo scarta i pixel di sfondo
                sum = sum + elem
    else:
        indice = 0
        for i in array:
            elem = i[indice]
            if( not(elem >= sfondo_B[0] and elem <= sfondo_B[1] ) ):    # In questo modo scarta i pixel di sfondo
                sum = sum + elem
    
    return sum/len(array)


#Data un immagine restituisce alcune informazioni sull'immagine
def analizza_immagine(immagine , debug = False):
    

    # Esempio di operazioni di analisi dei dati dell'immagine
    altezza, larghezza, canali = immagine.shape
    numero_pixel = altezza * larghezza

    # Calcola la media dei valori dei pixel per ogni canale
    media_canale1 = np.mean(immagine[:, :, 0])
    media_canale2 = np.mean(immagine[:, :, 1])
    media_canale3 = np.mean(immagine[:, :, 2])
    
    #Crea un array di pixel ( ogni pixel è un array di 3 )
    arr = []
    for i in range(altezza):
        for j in range(larghezza):
            arr.append(immagine[i,j])

    
    green = int(avg_channel(arr , "G"))
    red = int(avg_channel(arr , "R"))
    output_analysis = item(green , red)

    #Debug
    if(debug) : 
        print("\n")
        print(f"Altezza: {altezza} pixel")
        print(f"Larghezza: {larghezza} pixel")
        print(f"Numero di pixel: {numero_pixel}")
        print("-----------------------------------")
        print(output_analysis.getItemType(debug=True))
        time.sleep(1)
        print("-----------------------------------")
        print(f'Green : {green}')
        print(f'Red : {red}')
        print("\n")

    return(output_analysis.getItemType())
        


# Funzione che passata un img aperta con opencv2, restituisce una matrice di immagini ritagliate
def matrix_from_img(img, delay = 200 , open_img = False):
    # Dimnensione immagine
    altezza_immagine, larghezza_immagine, _ = img.shape


    # Calcola le dimensioni delle celle nella tua nuova griglia
    larghezza_cella = larghezza_immagine // num_colonne
    altezza_cella = altezza_immagine // num_righe

    coordinate_celle = []

    matrice_immagini = [
        [],
        [],
        [],
        [],
        [],
        []
    ]


    for riga in range(num_righe):
        for colonna in range(num_colonne):
            # Calcola le coordinate della cella corrente
            x1 = colonna * larghezza_cella
            y1 = riga * altezza_cella
            x2 = x1 + larghezza_cella
            y2 = y1 + altezza_cella

            # Aggiungi le coordinate alla lista
            coordinate_celle.append((x1, y1, x2, y2))

            # Ritaglia la cella dall'immagine
            cell_img = img[y1:y2, x1:x2]
            # cv2.imshow("Cella Ritagliata", cell_img)
            # cv2.waitKey(2000)
            matrice_immagini[riga].append(cell_img)

    if ( open_img ):
        cont = 1
        for i in range(num_righe):
            for j in range(num_colonne):
                cv2.imshow(f"Immagine {cont}",
                        matrice_immagini[i][j])
                cv2.waitKey(delay)
                cont += 1
        cv2.destroyAllWindows()

    return matrice_immagini

    
#Stampa una matrice di numrighe,numcolonne elementi
def print_matrix(matrix):
    
    for i in range(num_righe):
        for j in range(num_colonne):  
            print(str(matrix[i][j]) , end = " ")
        print()

# True -> matrice senza unknown elements   False -> matrice con elementi sconosciuti
def checkMatrix(matrix):
    prod = 1
    for i in range(num_righe):
        for j in range(num_colonne):  
            prod*=int(matrix[i][j])
    
    if(prod == 0):
        return False
    else:
        return True
    

def send_input_gui(string):
    print(f"Contenuto di 'string': {string}")
    c1, c2 = string.split('+')
    if c2 != '':  # se si usa CTRL o ALT come opzione
        print(f'{Fore.GREEN} Pressed key = {c1} + {c2} {Style.RESET_ALL}')
        pyautogui.hotkey(c1, c2)
        time.sleep(float(delay_key))
    else:
        print(f'{Fore.GREEN} Pressed key = {c1} {Style.RESET_ALL}')
        pyautogui.press(c1)
        time.sleep(float(delay_key))


def check_adj_row(l):
    for i in range(len(l)):  # range 0-4
        '''print(
            f'check index {i} -> is M[{i}]-> {l[i]} == M[{i+1}]-> {l[i+1]}')'''
        if (i == 4):
            return -1
        elif l[i] == 5:  # stella
            return i+offset
        else:
            if l[i] == l[i+1]:
                return i


def check_adj_column(M, j):
    for i in range(6):
        if (i == 5):
            return -1
        else:
            if M[i][j] == M[i+1][j]:
                return i


# controlla che il range sia valido per controllo orizzontale (e verticale outofline)
def valid_bound(i, j):
    if ((i >= 0 and i <= 5) and (j >= 0 and j <= 4)):
        return True
    print(f"{Fore.RED}(((Elemento out of bounds))){Style.RESET_ALL}")
    return False


# controlla che il range sia valido per controllo verticale
def valid_col_bound(i):
    if (i >= 0 and i <= 5):
        return True
    print(f"{Fore.RED}(((Elemento out of bounds))){Style.RESET_ALL}")
    return False



def check_column_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i+1][j]

    # controllo sinistra
    if ((valid_bound(i-1, j-1)) and (matrice[i-1][j-1] == el1)):
        return (f"M[{i-1}][{j-1}] dx")

    elif ((valid_bound(i+2, j-1)) and (matrice[i+2][j-1] == el2)):
        return (f"M[{i+2}][{j-1}] dx")

    # controllo destra
    elif (valid_bound(i-1, j+1) and (matrice[i-1][j+1] == el1)):
        return (f"M[{i-1}][{j+1}] sx")

    elif (valid_bound(i+2, j+1) and (matrice[i+2][j+1] == el2)):
        return (f"M[{i+2}][{j+1}] sx")

    # Controllo in line alto - basso
    elif ((valid_col_bound(i+3)) and (matrice[i+3][j] == el2)):
        return (f"M[{i+3}][{j}] alto")

    elif ((valid_col_bound(i-2)) and (matrice[i-2][j] == el1)):
        return (f"M[{i-2}][{j}] basso")

    # nessuna possibile mossa trovata
    print(
        f"{Fore.RED} Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}{Style.RESET_ALL}\n")
    return False

# da eliminare i return true con gli indici dell'elemento da tradurre


def check_row_feasibility(i, j, matrice):
    el1 = matrice[i][j]
    el2 = matrice[i][j+1]
    # controllo inline dx e sx:
    if (valid_bound(i, j-2) and (matrice[i][j-2] == el1)):
        return (f"M[{i}][{j-2}] dx")

    elif (valid_bound(i, j+2) and (matrice[i][j+2] == el2)):
        return (f"M[{i}][{j+2}] sx")

    # controllo elementi di sinistra:
    elif (valid_bound(i-1, j-1) and (matrice[i-1][j-1] == el1)):
        print(f"M[{i-1}][{j-1}] basso")

    elif (valid_bound(i+1, j-1) and (matrice[i+1][j-1] == el1)):
        return (f"M[{i+1}][{j-1}] alto")

    # controllo elementi di dx:
    elif (valid_bound(i-1, j+2) and (matrice[i-1][j+2] == el2)):
        return (f"M[{i-1}][{j+2}] basso")

    elif (valid_bound(i+1, j+2) and (matrice[i+1][j+2] == el2)):
        return (f"M[{i+1}][{j+2}] alto")

    # nessuna possibile mossa trovata
    print(
        f"{Fore.RED}Nessuna mossa valida trovata per elemento M[{i}][{j}] -> {matrice[i][j]}\n{Style.RESET_ALL}")
    return False


def scan_matrice(matrice2):
    for i in range(6):  # controllo per righe
        c = check_adj_row(matrice2[i])
        if c >= 100:   # condizione 
            c = c-100
            send_input_gui(dizionario_movimenti[f'M[{i}][{c}] basso'])
            break
        elif c != -1:  # condizione di adiacenza
            print(
                f"{Fore.GREEN}Trovati due elementi simili nella riga {i} {Style.RESET_ALL}")
            print(f'c = {c}')
            print(f"Indici = [", c, ",", c+1, "] -> ",
                  matrice2[i][c], " ", matrice2[i][c+1], f"\t{Fore.GREEN}inizio controllo feasibility{Style.RESET_ALL}")
            move = check_row_feasibility(i, c, matrice2)
            if move:
                send_input_gui(dizionario_movimenti[move])
                break
            print()
            # [1, 2, 4, 4, 5]
        else:
            print(
                f"{Fore.RED} Nessun elemento adiacente nella riga: {i}\n{Style.RESET_ALL}")

    for j in range(5):  # controllo per colonne
        riga_index = check_adj_column(matrice2, j)
        if riga_index != -1:  # condizione di adiacenza
            print(
                f"{Fore.GREEN} Trovati due elementi simili nella colonna: {j}\n{Style.RESET_ALL}")
            print(
                f"{Fore.GREEN}Indici = [{riga_index},{riga_index+1}] -> {matrice2[riga_index][j]} {matrice2[riga_index][j]} {Style.RESET_ALL}")
            move2 = check_column_feasibility(riga_index, j, matrice2)
            if move2:
                send_input_gui(dizionario_movimenti[move2])
                break
            print()
        else:
            print(
                f"{Fore.RED} Nessun elemento adiacente nella colonna: {j}\n{Style.RESET_ALL}")



 




    
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
    take_screenshot(870,330,490,620, label , name_script='Main.py')
    img_name = f"screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()
    #Ritaglio immagine, per adattarla al secondo taglio
    x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
    immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza] 
    
    #Crea la matrice di item e numeri
    matrix_img = matrix_from_img(immagine_ritagliata , 200 , open_img = False)
    matrix_item = [ [] , [] , [] , [] , [] , [] ]
    matrix_number = [ [] , [] , [] , [] , [] , [] ]
    for i in range(num_righe):
        for j in range(num_colonne):
            res = analizza_immagine(matrix_img[i][j] , debug=False)
            matrix_item[i].append(res)
            matrix_number[i].append(default_name[str(res)])
    
    if(checkMatrix(matrix_number)):
        print(f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')
        consecutive_error_count=0
        scan_matrice(matrix_number)
    else:
        print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
        consecutive_error+=1

