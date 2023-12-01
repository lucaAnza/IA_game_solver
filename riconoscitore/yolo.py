# NON FUNZIONA SENZA PESI E CONFIG FILES
# ESTREMAMENTE PESANTE E CPU DEPENDANT
# LASCIATO IL CODICE SOLO PER LEGACY

import cv2
import numpy as np

classFile = 'coco.names'
whT = 320

classNames = []

with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

modelConfiguration = 'yolov3-320.cfg'
modelWeights = 'yolov3.weights'

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

img = cv2.imread("pizza.png")

blob = cv2.dnn.blobFromImage(img, 1/255, (whT, whT), [0, 0, 0], 1, crop=False)
net.setInput(blob)

layerNames = net.getLayerNames()
outputNames = [layerNames[i[0] - 1] if isinstance(
    i, list) else layerNames[i - 1] for i in net.getUnconnectedOutLayers()]

# Lista per memorizzare i nomi degli oggetti rilevati
detected_objects = []

outputs = net.forward(outputNames)

# Ottieni le dimensioni dell'immagine
height, width, _ = img.shape

# Elabora le uscite per ottenere il riconoscimento
for out in outputs:
    for detection in out:
        scores = detection[5:]
        classId = np.argmax(scores)
        confidence = scores[classId]

        if confidence > 0.1:  # Imposta una soglia di confidenza
            w, h = int(detection[2] * width), int(detection[3] * height)
            x, y = int((detection[0] * width) - w /
                       2), int((detection[1] * height) - h/2)

            # Aggiungi il nome dell'oggetto rilevato alla lista
            detected_objects.append(classNames[classId].upper())

# Unisci i nomi degli oggetti in una stringa
result_string = ', '.join(detected_objects)

# Stampa la stringa prima di terminare lo script
print(result_string)
