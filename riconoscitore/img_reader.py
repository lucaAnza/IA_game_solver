import cv2
import pytesseract
from PIL import Image

# Carica l'immagine con OpenCV
img1 = cv2.imread("nocap1.png")
img2 = cv2.imread("nocap2.png")

img1_grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_grey = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Conversione dell'immagine in scala di grigi (facilita riconoscimento)
# img_grayscale = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
# Trasformare forme in grigio blocca la trasformazione

text = pytesseract.image_to_string(img1, config="--psm 7")
text2 = pytesseract.image_to_string(img2, config="--psm 7")


print("TRASFORMAZIONE IMMAGINE IN TESTO:")
print("\nImmagine  1:", text)
print("\nImmagine 2:", text2)
