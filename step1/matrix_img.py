import cv2
import numpy as np

# Carico IMG con CV2
img = cv2.imread("Screen2.png")

# Dimnensione immagine
altezza_immagine, larghezza_immagine, _ = img.shape

# Verifica immagine oringiale sia aperta correttamente
cv2.imshow("immagine", img)

# Dimensione matrice
num_righe = 6
num_colonne = 5

# Calcola le dimensioni delle celle nella tua nuova griglia
larghezza_cella = larghezza_immagine // num_colonne
altezza_cella = altezza_immagine // num_righe

coordinate_celle = []


for riga in range(num_righe):
    # Scorrere le colonne
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
        cv2.imshow("Cella Ritagliata", cell_img)
        cv2.waitKey(2000)

cv2.destroyAllWindows()
