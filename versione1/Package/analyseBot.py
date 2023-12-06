import cv2
import numpy as np
import sys
import time

if __name__ == "__main__":
    import solverBot
    import decoratori
else:
    from Package import solverBot
    from Package import decoratori

# GLOBALS

sfondo_R = (200, 250)
sfondo_G = (180, 220)
sfondo_B = (180, 230)

# Dimensione matrice
num_righe = solverBot.num_righe
num_colonne = solverBot.num_colonne


# Struttura dati che tiene i dati di check ( Green , Red )
defalt_pixel = {
    'hat': (42, 41),
    'iced_hat': (47, 61),
    'skate': (29, 33),
    'iced_skate': (32, 41),
    'pizza': (26, 21),
    'iced_pizza': (25, 45),
    'can': (39, 18),
    'iced_can': (28, 56),
    'star': (20, 11)}

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


# Classe per gli oggetti
class item:
    def __init__(self, green, red, nome="General_item"):
        self.nome = nome
        self.green = green
        self.red = red
        self.sum = green+red

    def getItemType(self, debug=False):

        # Hat
        for incertezza in range(2, 4):
            if self.__isInIntervall('hat', incertezza, debug):
                return "hat"
            elif self.__isInIntervall('skate', incertezza, debug):
                return "skate"
            elif self.__isInIntervall('pizza', incertezza, debug):
                return "pizza"
            elif self.__isInIntervall('can', incertezza, debug):
                return "can"
            elif self.__isInIntervall('star', incertezza, debug):
                return "star"
            elif self.__isInIntervall('iced_hat', incertezza, debug):
                return "iced_hat"
            elif self.__isInIntervall('iced_skate', incertezza, debug):
                return "iced_skate"
            elif self.__isInIntervall('iced_pizza', incertezza, debug):
                return "iced_pizza"
            elif self.__isInIntervall('iced_can', incertezza, debug):
                return "iced_can"

        return "Unknown_Item"

    def __isInIntervall(self, type, incertezza, debug=False):
        default_green = defalt_pixel[type][0]
        default_red = defalt_pixel[type][1]
        default_sum = default_green + default_red
        valutation = ((abs(self.sum-default_sum) <= incertezza*2) and
                      ((abs(self.green-default_green) <= incertezza) and (abs(self.red-default_red) <= incertezza)))
        if (debug):
            print(f"Type : {type}--------------")
            print(f"Incertezza : {incertezza}\nSum : {self.sum}\nDefault_sum = {default_sum}\nGreen/Default : {self.green}/{default_green}\nRed/Default : {self.red}/{default_red}")
            """return   (  (abs(self.sum-default_sum) < incertezza*2 ) and
                 (  (abs(self.green-default_green) < incertezza) and (abs(self.red-default_red) < incertezza) ) )"""

        return valutation


# Dato l'array dei pixel, scarta i pixel di sfondo e fa una media degli altri
def avg_channel(array, channel_type='R'):
    sum = 0
    if (channel_type == 'R'):
        indice = 2
        for i in array:
            elem = i[indice]
            # In questo modo scarta i pixel di sfondo
            if (not (elem >= sfondo_R[0] and elem <= sfondo_R[1])):
                sum = sum + elem
    elif (channel_type == 'G'):
        indice = 1
        for i in array:
            elem = i[indice]
            # In questo modo scarta i pixel di sfondo
            if (not (elem >= sfondo_G[0] and elem <= sfondo_G[1])):
                sum = sum + elem
    else:
        indice = 0
        for i in array:
            elem = i[indice]
            # In questo modo scarta i pixel di sfondo
            if (not (elem >= sfondo_B[0] and elem <= sfondo_B[1])):
                sum = sum + elem

    return sum/len(array)


# Data un immagine restituisce alcune informazioni sull'immagine
def analizza_immagine(immagine, debug=False):

    # Esempio di operazioni di analisi dei dati dell'immagine
    altezza, larghezza, canali = immagine.shape

    # Crea un array di pixel ( ogni pixel è un array di 3 )
    arr = []
    for i in range(altezza):
        for j in range(larghezza):
            arr.append(immagine[i, j])

    green = int(avg_channel(arr, "G"))
    red = int(avg_channel(arr, "R"))
    output_analysis = item(green, red)

    # Debug
    if (debug):
        numero_pixel = altezza * larghezza
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

    return (output_analysis.getItemType())


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


# MAIN

if (__name__ == "__main__"):

    inizio = time.time()


    nome_file_immagine = "Screenshot/Screenshot.png"
    nome_file_immagine = "Screenshot/screenshot[HELP].png"
    
    
    immagine = cv2.imread(nome_file_immagine)

    # Verifica che l'immagine sia stata caricata correttamente
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()

    x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
    immagine_ritagliata = immagine[y_inizio:y_inizio +
                                   altezza, x_inizio:x_inizio + larghezza]

    matrix_img = solverBot.matrix_from_img(
        immagine_ritagliata, 500, open_img=False)
    matrix_item = [[], [], [], [], [], []]
    matrix_number = [[], [], [], [], [], []]

    for i in range(num_righe):
        for j in range(num_colonne):
            res = analizza_immagine(matrix_img[i][j], debug=False)
            matrix_item[i].append(res)
            matrix_number[i].append(default_name[str(res)])

    print_matrix(matrix_item)

    script_name = sys.argv[0]
    fine = time.time()
    tempo_esecuzione = fine - inizio
    print(
        f"La funzione '{script_name}' ha impiegato {tempo_esecuzione:.4f} secondi.")
