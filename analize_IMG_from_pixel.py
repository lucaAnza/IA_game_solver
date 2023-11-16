import cv2
import numpy as np
import sys

# Ricorda per chiudere il processo : kill -9 $(pgrep -n "python")


def analizza_immagine(immagine):
    

    # Esempio di operazioni di analisi dei dati dell'immagine
    altezza, larghezza, canali = immagine.shape
    numero_pixel = altezza * larghezza

    # Calcola la media dei valori dei pixel per ogni canale
    media_canale1 = np.mean(immagine[:, :, 0])
    media_canale2 = np.mean(immagine[:, :, 1])
    media_canale3 = np.mean(immagine[:, :, 2])

    
    # Accedi a un pixel specifico
    pixel_valore = immagine[100, 50]

    # Stampa i risultati
    print(f"Altezza: {altezza} pixel")
    print(f"Larghezza: {larghezza} pixel")
    print(f"Numero di pixel: {numero_pixel}")
    print(f"Media del canale 1: {media_canale1}")
    print(f"Media del canale 2: {media_canale2}")
    print(f"Media del canale 3: {media_canale3}")
    print(f"Valore del pixel alla posizione (100, 50): {pixel_valore}")


    



nome_file_immagine = "Screen.png"
# Carica l'immagine
immagine = cv2.imread(nome_file_immagine)

# Verifica che l'immagine sia stata caricata correttamente
if immagine is None:
    print("Errore nel caricamento dell'immagine.")
    sys.exit()
    
# Specifica le coordinate del rettangolo da ritagliare
x_inizio, y_inizio, larghezza, altezza = 0, 0, 100, 100

# Esegui il ritaglio dell'immagine
immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]

# Visualizza l'immagine originale e l'immagine ritagliata
cv2.imshow("Immagine originale", immagine)
cv2.imshow("Immagine ritagliata", immagine_ritagliata)
cv2.waitKey(0)
cv2.destroyAllWindows()



analizza_immagine(immagine)






