import cv2
import numpy as np
import sys
import time
import pyautogui
import datetime
import os


#GLOBALS

sfondo_R = (200,250)
sfondo_G = (180,220)
sfondo_B = (180,230)

# Dimensione matrice
num_righe = 6
num_colonne = 5



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
 
    

#MAIN

nome_file_immagine = "Screen_bot.png"
immagine = cv2.imread(nome_file_immagine)

# Verifica che l'immagine sia stata caricata correttamente
if immagine is None:
    print("Errore nel caricamento dell'immagine.")
    sys.exit()

x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza] 
altezza, larghezza, canali = immagine.shape


#cv2.imshow("img" , immagine_ritagliata)
#cv2.waitKey(5000)


matrix_img = matrix_from_img(immagine_ritagliata , 500 , open_img = False)
matrix_item = [ [] , [] , [] , [] , [] , [] ]
matrix_number = [ [] , [] , [] , [] , [] , [] ]

for i in range(num_righe):
    for j in range(num_colonne):
        res = analizza_immagine(matrix_img[i][j] , debug=False)
        matrix_item[i].append(res)
        matrix_number[i].append(default_name[str(res)])


print_matrix(matrix_item)


    



"""
#Script finale
attesa = 10
for i in range(attesa):
    print(f"Starting bot in {attesa-i} seconds...")
    time.sleep(1)

consecutive_error = 0
while(consecutive_error < 100):
    #Cattura screenshot
    label = 'kz32'
    #take_screenshot(870,330,490,620, label)
    img_name = f"screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()
    
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
        consecutive_error_count=0
        #Ritorna il pulsante da cliccare
        #pulsante = algoritmoCri(matrix_number)
        # -> Clicca il pulsante
    else:
        consecutive_error+=1
"""
