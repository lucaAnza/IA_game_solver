from PIL import Image

import pytesseract

print(pytesseract.image_to_string(Image.open('im1.png')))
print(pytesseract.image_to_string(Image.open('im2.png')))

print(pytesseract.image_to_string(Image.open('im4.png')))

print(pytesseract.image_to_string(Image.open('im5.png')))

print(pytesseract.image_to_string(Image.open('im16.png')))

print(pytesseract.image_to_string(Image.open('im18.png')))

print(pytesseract.image_to_string(Image.open('im15.png')))
