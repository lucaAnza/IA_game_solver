import cv2
import pytesseract
from PIL import Image

# Carica l'immagine con OpenCV
img_cv2 = cv2.imread("16.png")
img = Image.open("64.png")

#Conversione dell'immagine in scala di grigi (facilita riconoscimento)
#img_grayscale = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(img_cv2, config="--psm 7")
text2 = pytesseract.image_to_string(img, config="--psm 7")

print("\nnumero riconosciuto:", text)
print("\nnumero riconosciuto:", text2)

