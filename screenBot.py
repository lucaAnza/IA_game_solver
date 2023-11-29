import pyautogui
import time
import pyautogui
import datetime
import os

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






def take_screenshot():
    # Ottieni le dimensioni dello schermo
    width, height = pyautogui.size()

    # Cattura lo screenshot
    #screenshot = pyautogui.screenshot()
    x = 100
    y = 100
    width = 500
    height = 300
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Specifica il percorso e il nome del file per salvare lo screenshot
    #timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    current_directory = os.path.abspath(__file__)
    file_path = str(current_directory[:-12].replace('\\' , '/')) + str("test.png")    # 12 rappresenta la lunghezza del nome dello script -> screen.py


    # Salva lo screenshot
    screenshot.save(file_path)

    
    
    print(f"Screenshot salvato in: {file_path}")


# Chiama la funzione per catturare lo screenshot
take_screenshot()


