from PIL import Image
import pyautogui
import cv2
import pytesseract
import numpy as np

#riconoscitore con mask e trasformazioni di colore
#tengo solo in caso serva complicare il codice per riconoscere
#immagini sotto una certa tonalità

#Lettura immagine
img_cv2 = cv2.imread("numero.png")

# Cvt to hsv
hsv = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2HSV)

# Get binary-mask
msk = cv2.inRange(hsv, np.array([0, 0, 175]), np.array([179, 255, 255]))
krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
dlt = cv2.dilate(msk, krn, iterations=1)
thr = 255 - cv2.bitwise_and(dlt, msk)

# OCR
d = pytesseract.image_to_string(thr, config="--psm 10")
print("alo",d)
