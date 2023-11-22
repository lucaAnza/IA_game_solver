import cv2
import numpy as np
import sys

# Ricorda per chiudere il processo : kill -9 $(pgrep -n "python")


# DATI

# Immagine[i,j] ritorna un array di 3  ( B , G , R)
# Lo sfondo sta in un range di R = {237,250}   G = {208,211}   B = {210,216}

"""sfondo_R = (237,250)
sfondo_G = (208,211)
sfondo_B = (210,216)"""

sfondo_R = (200,250)
sfondo_G = (180,220)
sfondo_B = (180,230)

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
    
    print(channel_type + ":")
    print(sum/len(array))


def analizza_immagine(immagine):
    

    # Esempio di operazioni di analisi dei dati dell'immagine
    altezza, larghezza, canali = immagine.shape
    numero_pixel = altezza * larghezza

    # Calcola la media dei valori dei pixel per ogni canale
    media_canale1 = np.mean(immagine[:, :, 0])
    media_canale2 = np.mean(immagine[:, :, 1])
    media_canale3 = np.mean(immagine[:, :, 2])

    
    # Accedi a un pixel specifico
    #pixel_valore = immagine[30, 30]

    # Stampa i risultati
    print(f"Altezza: {altezza} pixel")
    print(f"Larghezza: {larghezza} pixel")
    print(f"Numero di pixel: {numero_pixel}")
    print(f"Media del canale 1: {media_canale1}")
    print(f"Media del canale 2: {media_canale2}")
    print(f"Media del canale 3: {media_canale3}")
    #print(f"Valore del pixel alla posizione (100, 50): {pixel_valore}")
    
    arr = []
    for i in range(larghezza):
        for j in range(larghezza):
            arr.append(immagine[i,j])

    avg_channel(arr , "B")
    avg_channel(arr , "G")
    avg_channel(arr , "R")


    



nome_file_immagine = "Screen.png"
# Carica l'immagine
immagine = cv2.imread(nome_file_immagine)

# Verifica che l'immagine sia stata caricata correttamente
if immagine is None:
    print("Errore nel caricamento dell'immagine.")
    sys.exit()
    
# Specifica le coordinate del rettangolo da ritagliare
x_inizio, y_inizio, larghezza, altezza = 15, 265, 80, 80
#170 CAP2
#85 LAT1
#250 PIZZA
#333 SKATE
# Esegui il ritaglio dell'immagine
immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]

# Visualizza l'immagine originale e l'immagine ritagliata
#cv2.imshow("Immagine originale", immagine)
cv2.imshow("Immagine ritagliata", immagine_ritagliata)
analizza_immagine(immagine_ritagliata)
cv2.waitKey(0)
cv2.destroyAllWindows()




#SKATE 30,35
#PIZZA 27,25
#CAPPELLO 42,44