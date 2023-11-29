import cv2
import numpy as np
import sys
import time

# Ricorda per chiudere il processo : kill -9 $(pgrep -n "python")


# DATI

# Immagine[i,j] ritorna un array di 3  ( B , G , R)
# Lo sfondo sta in un range di R = {237,250}   G = {208,211}   B = {210,216}

"""sfondo_R = (237,250)
sfondo_G = (208,211)
sfondo_B = (210,216)"""


#GLOBALS

sfondo_R = (200,250)
sfondo_G = (180,220)
sfondo_B = (180,230)

# Dimensione matrice
num_righe = 6
num_colonne = 5



#Struttura dati che tiene i dati di check ( Green , Red )
defalt_pixel = { 
    'hat' : (42,44) ,
    'iced_hat' : (56,62) ,
    'skate' : (30,35) ,
    'iced_skate' : (39,42) ,
    'pizza' : (27,25) ,
    'iced_pizza' : (0,0) ,
    'can' : (39,28) ,
    'iced_can' : (0,0) ,
    'star' : (22,22) }

default_name = {
    'hat' : 1 ,
    'iced_hat' : 2 ,
    'skate' : 3 ,
    'iced_skate' : 4 ,
    'pizza' : 5 ,
    'iced_pizza' : 6 ,
    'can' : 7 ,
    'iced_can' : 8 ,
    'star' : 9 
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
            
        return "Unknown Item"
        
        
    
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
    for i in range(larghezza):
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
    else:
        print(output_analysis.getItemType())
        


    


# Funzione che passata un img aperta con opencv2, restituisce una matrice di immagini ritagliate
def matrix_from_img(img):
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

    cont = 1
    for i in range(num_righe):
        for j in range(num_colonne):
            cv2.imshow(f"Immagine {cont}",
                    matrice_immagini[i][j])
            cv2.waitKey(50)
            cont += 1
    cv2.destroyAllWindows()

    return matrice_immagini

    


    


    



nome_file_immagine = "Screen.png"
# Carica l'immagine
immagine = cv2.imread(nome_file_immagine)

# Verifica che l'immagine sia stata caricata correttamente
if immagine is None:
    print("Errore nel caricamento dell'immagine.")
    sys.exit()

matrix = matrix_from_img(immagine)

for i in range(num_righe):
    for j in range(num_colonne):
        analizza_immagine(matrix[i][j] , True)

    
"""
scelta = input("Immagine originale? (y/n) : ")
#scelta = 'y'
if(scelta == 'y' or scelta == 'yes'):
    cv2.imshow("Immagine originale", immagine)
    analizza_immagine(immagine)
else:
    # Ritaglio
    x_inizio, y_inizio, larghezza, altezza = 15, 433, 80, 80
    immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]  
    cv2.imshow("Immagine ritagliata", immagine_ritagliata)
    analizza_immagine(immagine_ritagliata)



time.sleep(1)             # In questa fase premi invio -> Per problemi di buffering
while True:
    key = cv2.waitKeyEx(0)
    if(chr(key) == 'q'):
        print(f"Fine sessione [ tasto premuto = {chr(key)} ] ")
        break
cv2.destroyAllWindows()"""



# Green,Red
#SKATE 30,35
#PIZZA 27,25
#CAPPELLO 42,44