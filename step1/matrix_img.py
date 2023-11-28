import cv2
import numpy as np

# Carico immagine e controllo per debug
img = cv2.imread("Screen.png")


# Dimnensione immagine
altezza_immagine, larghezza_immagine, _ = img.shape


# Dimensione matrice
num_righe = 6
num_colonne = 5

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
        cv2.waitKey(800)
        cont += 1
cv2.destroyAllWindows()
