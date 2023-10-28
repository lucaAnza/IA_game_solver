import cv2
import time
import pytesseract
from PIL import Image

img = Image.open("vodafone-modified.jpeg")

larghezza_immagine, altezza_immagine = img.size

larghezza_cella = larghezza_immagine / 4
altezza_cella = altezza_immagine / 4

coordinate_celle = []
numeri_celle = []

for riga in range(4):
    # Scorrere le colonne
    for colonna in range(4):
        # Calcola le coordinate della cella corrente
        x1 = colonna * larghezza_cella + larghezza_cella * 0.1
        y1 = riga * altezza_cella + altezza_cella * 0.1
        x2 = x1 + larghezza_cella * 0.7
        y2 = y1 + altezza_cella * 0.7
        # Aggiungi le coordinate alla lista
        coordinate_celle.append((x1, y1, x2, y2))

        cell_img = img.crop((x1,y1,x2,y2))
        cell_img.show()
        time.sleep(2)
        testo_cell = pytesseract.image_to_string(cell_img,config='--psm 6',lang='eng')
        try:
            numero = int(testo_cell)
            print("Numero trovato: ",numero)
            numeri_celle.append(numero)
        except:
            print("failed - traduzione in 8 di: ", testo_cell,)
            numero = 8
            numeri_celle.append(numero)
            
        


print(numeri_celle)