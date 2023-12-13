import pyautogui
import time
import pyautogui
import os
import time
import cv2

if __name__ == "__main__" or __name__ == 'screenBot':
    import decoratori
else:
    from Package import decoratori


# Item : (x,y) , (b , g , r)        ->  rosso =  (130,106,237)     , grigio = (130,106,237)
dict_item = {
    'star': ( (5,-3) , (74,205,247) ) ,
    'hat': ( (-16,21) , (130,106,237) ) ,
    'iced_hat': ( (-18,18) , (186,150,189) ) ,
    'skate': ( (-10,10) , (173,147,170) ) ,
    'iced_skate': ( (-10,7) , (210,172,155) ) ,
    'pizza': ( (-10,7) , (255,255,255) ) ,
    'iced_pizza': ( (-10,7) , (246,225,205) ) ,
    'can': ( (5,-3) , (130,106,237) ) ,
    'iced_can': ( (19,3) , (228,207,184) ) ,
    'Unknown_Item': ( (1,1) , (0,0,0) ) 
}




# Funzione che esegue uno screenshot
@decoratori.timestamp_decorator
def take_screenshot(x=0, y=0, width=500, height=500, label="", debug=False, fullScreen=False):
    script_name = 'screenBot.py'

    if (fullScreen):
        screenshot = pyautogui.screenshot()
    else:
        screenshot = pyautogui.screenshot(region=(x, y, width, height))

    current_directory = os.path.abspath(__file__)
    path_from_current_dir = f"../Screenshot/screenshot{label}.png"
    file_path = str(current_directory[:-len(script_name)
                                      ].replace('\\', '/')) + str(path_from_current_dir)
    screenshot.save(file_path)
    if (debug):
        print(f"Screenshot salvato in: {file_path}")
        if (fullScreen):
            print(f"Eseguito fullscreen!")
        else:
            print(f"Screen [x={x},y={y}] , Size(H,W) = {height,width}")
    return file_path



# Ritorna le coordinate del pixel cliccato
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'\nCoordinate del pixel: ({x}, {y})')



# Funzione che dato un pixel ti dice che item rappresenta
def which_object( immagine ,  x = 0 , y = 0):

    # Key = hat,pizza,...       Item = (x,y) (b,g,r)
    for key, value in dict_item.items():
        x_try = x + value[0][0]
        y_try = y + value[0][1]
        pixel = immagine[y_try , x_try]

        if(pixel[0] == value[1][0] and pixel[1] == value[1][1] and pixel[2] == value[1][2]):
            #print(key , " pixel = " , pixel , " value = " , value)
            return key
    
    return "Unknown_Item"


#Funzione che crea una grigliata formata di quadrati con lato "square_side". Se gli viene passata una matrice ritorna una matrice
# con ogni elemento uguale ai colori RGB del centro di ogni sotto-quadrato.
def set_grill(immagine , top_left = (0,0) , square_side = 40 , righe = 6 , colonne = 5 , matrix  = False):
    
    if(matrix == True) :     # Caso in cui ti aspetti che torna una matrice di item
        matrix = [ [] , [] , [] , [] , [] , [] ]
        color_square = (0, 0, 255)  # Colore in formato BGR (rosso)
        color_dot = ( 255 , 0 , 0)
        thickness_square = 2
        thickness_dot = 1

        # Creazione griglia
        top_lx = top_left
        bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )
        x_centro = (top_lx[0] + bot_rx[0]) // 2
        y_centro = (top_lx[1] + bot_rx[1]) // 2
        for i in range(righe):
            for j in range(colonne):
                cv2.rectangle(immagine, top_lx, bot_rx, color_square, thickness_square)
                cv2.rectangle(immagine, (x_centro, y_centro) , (x_centro, y_centro), color_dot  , thickness_dot)
        
                matrix[i].append(which_object(immagine , x_centro , y_centro))
                
                top_lx = (top_lx[0]+square_side , top_lx[1] )    # slide top_left  x ----> x2 -----> xn
                bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )   # adattamento bottom_right
                x_centro = (top_lx[0] + bot_rx[0]) // 2
                y_centro = (top_lx[1] + bot_rx[1]) // 2
                
            top_lx = (top_left[0] , top_lx[1]+square_side )           # slide top_left   y 
            bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )      # adattamento bottom_right
            x_centro = (top_lx[0] + bot_rx[0]) // 2
            y_centro = (top_lx[1] + bot_rx[1]) // 2
        
        
        return matrix
    else:
        print("Matrice non settata! [ Debug mode active ]")
        color_square = (0, 0, 255)  # Colore in formato BGR (rosso)
        color_dot = ( 255 , 0 , 0)
        thickness_square = 2
        thickness_dot = 1

        # Creazione griglia
        top_lx = top_left
        bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )
        x_centro = (top_lx[0] + bot_rx[0]) // 2
        y_centro = (top_lx[1] + bot_rx[1]) // 2
        for i in range(righe):
            for j in range(colonne):
                cv2.rectangle(immagine, top_lx, bot_rx, color_square, thickness_square)
                print(f'point pixel -> [{i,j}] - [x={x_centro},y={y_centro}] {immagine[y_centro,x_centro]}')
                cv2.rectangle(immagine, (x_centro, y_centro) , (x_centro, y_centro),color_dot  , thickness_dot)
                top_lx = (top_lx[0]+square_side , top_lx[1] )    # slide top_left  x ----> x2 -----> xn
                bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )   # adattamento bottom_right
                x_centro = (top_lx[0] + bot_rx[0]) // 2
                y_centro = (top_lx[1] + bot_rx[1]) // 2
            
            top_lx = (top_left[0] , top_lx[1]+square_side )           # slide top_left   y 
            bot_rx = (top_lx[0] + square_side , top_lx[1] + square_side )      # adattamento bottom_right
            x_centro = (top_lx[0] + bot_rx[0]) // 2
            y_centro = (top_lx[1] + bot_rx[1]) // 2
    




#Script che esegue n screen, tra uno screen e l'altro attende k secondi.
if (__name__ == '__main__'):        

    attesa = 5
    for i in range(attesa):
        print(f"Screen tra {attesa-i} secondi...")
        time.sleep(1)

    
    for j in range(1):
        time.sleep(2)
        take_screenshot(870, 330, 490, 620,label=f'-{j}cut-')
        
