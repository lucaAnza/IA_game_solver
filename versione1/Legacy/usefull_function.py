#USEFULL1
"""
scelta = input("Immagine originale? (y/n) : ")
#scelta = 'y'
if(scelta == 'y' or scelta == 'yes'):
    cv2.imshow("Immagine originale", immagine)
    analizza_immagine(immagine)
else:
    # Ritaglio
    x_inizio, y_inizio, larghezza, altezza = 15, 433, 80, 80
    immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]  
    cv2.imshow("Immagine ritagliata", immagine_ritagliata)
    analizza_immagine(immagine_ritagliata)



time.sleep(1)             # In questa fase premi invio -> Per problemi di buffering
while True:
    key = cv2.waitKeyEx(0)
    if(chr(key) == 'q'):
        print(f"Fine sessione [ tasto premuto = {chr(key)} ] ")
        break
cv2.destroyAllWindows()"""


#USEFULL SCREEN

# Ottieni le dimensioni dello schermo
    #width, height = pyautogui.size()

    # Specifica il percorso e il nome del file per salvare lo screenshot
    #timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# Specifica le coordinate e le dimensioni della regione desiderata

"""
# Cattura lo screenshot della regione specificata
screenshot = pyautogui.screenshot(region=(x, y, width, height))

# Converti l'immagine in formato OpenCV (BGR)
screenshot_np = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Salva l'immagine
cv2.imwrite('screenshot.png', screenshot_np)
cv2.imshow("Immagine screenshot", screenshot_np)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


#USEFULL Pressione pulsanti tester
"""
import time
import pyautogui

start_time = time.time()
c1 = 'ctrl'
c2 = 'v'
pyautogui.hotkey(c1, c2, interval=0.05)
end_time = time.time()

print(f"Tempo impiegato: {end_time - start_time} secondi")
"""



### Ritaglio immagine


#screenBot.take_screenshot(870,330,490,620, label)
#Ritaglio immagine, per adattarla al secondo taglio
#x_inizio, y_inizio, larghezza, altezza = 16, 30, 455, 546
#immagine_ritagliata = immagine[y_inizio:y_inizio + altezza, x_inizio:x_inizio + larghezza]


# Multi process
"""

from multiprocessing import Process
import time

def worker(process_id):
    for _ in range(5):
        time.sleep(1)
        print(f"Processo {process_id} in esecuzione")

if __name__ == "__main__":
    # Numero di processi da avviare
    num_processes = 3

    # Lista per mantenere riferimenti ai processi
    processes = []

    # Avvia i processi
    for i in range(num_processes):
        # Crea un nuovo processo con la funzione worker
        p = Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    # Attendi che tutti i processi completino l'esecuzione
    for p in processes:
        p.join()

    print("Fine dello script")

"""