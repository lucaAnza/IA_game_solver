import pyautogui
import time

# Funzione per automatizzare la scrittura di testo con PyAutoGUI
def scrivi_testo(testo, intervallo=0.1):
    time.sleep(10)  # Aggiungi un ritardo per passare il focus all'applicazione di destinazione (se necessario)
    pyautogui.typewrite(testo, interval=intervallo)

'''# Funzione per simulare la pressione di un tasto speciale
def premi_tasto_speciale(tasto):
    pyautogui.press(tasto)

# Funzione per simulare una combinazione di tasti
def combina_tasti(tasti):
    pyautogui.hotkey(*tasti)

# Esempio di utilizzo
if __name__ == "__main__":
    # Scrivi del testo
    scrivi_testo("Hello, World!")

    # Premi il tasto "Invio"
    premi_tasto_speciale('enter')

    # Esegui una combinazione di tasti (Ctrl+C)
    combina_tasti(['ctrl', 'c'])
'''

testo = input("Inserire il testo : ")
scrivi_testo(testo)