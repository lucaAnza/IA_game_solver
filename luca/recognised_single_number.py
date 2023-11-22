import cv2
import pytesseract
from PIL import Image

# Carica l'immagine con OpenCV
img = Image.open("8.png")

#Conversione dell'immagine in scala di grigi (facilita riconoscimento)
text = pytesseract.image_to_string(img, config="--psm 1")
print("\nnumero riconosciuto:", text)
