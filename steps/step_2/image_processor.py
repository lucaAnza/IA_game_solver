import cv2
import pytesseract

# Carica l'immagine con OpenCV
img_cv2 = cv2.imread("numero2.png")

#Conversione dell'immagine in scala di grigi (facilita riconoscimento)
#img_grayscale = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(img_cv2, config="--psm 6")
print("\nnumero riconosciuto:", text)
