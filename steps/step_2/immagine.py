import cv2
import pytesseract
from PIL import Image

img = Image.open("img4.png")

larghezza_immagine, altezza_immagine = img.size

print(larghezza_immagine," - ",altezza_immagine)