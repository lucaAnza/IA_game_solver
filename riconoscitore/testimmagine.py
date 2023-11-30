import cv2
import numpy as np

# Leggi l'immagine con OpenCV
img = cv2.imread("Screen.png")

# Verifica se l'immagine è stata letta correttamente
if img is not None:
    # Ottieni le dimensioni dell'immagine
    altezza_immagine, larghezza_immagine, _ = img.shape

    # Calcola le dimensioni della cella (adatta questi valori alle tue esigenze)
    larghezza_cella = larghezza_immagine // 5
    altezza_cella = altezza_immagine // 6

    # ... (il resto del tuo codice)
else:
    print("Errore: impossibile leggere l'immagine.")
