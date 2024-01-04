import cv2
import numpy as np
import sys
import time
import datetime
import os
from colorama import Fore, Style
import pyfiglet
from Package import *
import tracemalloc
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyautogui

chri_webhook = "https://discord.com/api/webhooks/1184788603470090320/jqkYHRC-y7P920AYLdB1e08g1WPLWzIcelEssk1tG23VXXE2kvgsNUQUhg5q7fYZ86hU"
luke_webhook = "https://discord.com/api/webhooks/1184915602431823944/3HyIjU1u40NnJUVpzzfBAEOAHZ9EZkiUwEeViffQLOxUwLpU25-dRR0-LJlx2snXbdsH"

game_iteration = 8000 + 10

# Coordinate Luke
x_global = 5
y_global = 20
side_global = 93

"""
# Coordinate Chrii
x_global = 6
y_global = 23
side_global = 94
"""

    

def webhook_print( url , title , description , img_name = None , color = 'ff0000' , author = None , trofei_screen = False):
    pc_user = "Luke-Laptop"
    
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=title,
                         description=description, color=color)
    embed.set_timestamp()
    embed.set_footer(text = pc_user)
    webhook.add_embed(embed)

    if(trofei_screen):
        if(img_name != None):
            #screenBot.take_screenshot(870, 290, 490, 200, label='_dd_termination')  # Trofei screen
            screenBot.take_screenshot(830, 60, 570, 960, label='_dd_termination')   # Full App screen
            with open("./Screenshot/screenshot_dd_termination.png", "rb") as f:
                webhook.add_file(file=f.read(), filename=img_name)
    else:
        if(img_name != None):
            screenBot.take_screenshot(830, 60, 570, 960, label='_dd_termination')   # Full App screen
            with open("./Screenshot/screenshot_dd_termination.png", "rb") as f: 
                webhook.add_file(file=f.read(), filename=img_name)
    response = webhook.execute()   # Invio webhook



def failed_game_wh():
    webhook_print(chri_webhook , "Error" , "Partita non avviata per eccezione, script terminato" , color = 'ff0000')
    


def game_started_successfully():
    webhook_print(chri_webhook , "Success" , "Partita avviata correttamente" , color = '00ff00')


def check_error():
    print_coloured.print_cyan_ts("Possibile conflitto trovato... going to sleep")
    webhook_print(chri_webhook , "Intervento" , "Situazione di stallo, going to sleep" , color = 'ff0000')
    time.sleep(8)
    command = 'alt+3'  # Clicca il pulsante "continua a giocare"
    solverBot.send_input_gui(command)

def stall_fixed():
    print_coloured.print_cyan_ts("Conflitto superato... continuo a giocare")
    webhook_print(chri_webhook , "Intervento" , "Conflitto superato... continuo a giocare! " , color = '00ff00')
    


def create_new_game():
    webhook_print(chri_webhook , "Iterazioni raggiunte" , "Chiusura partita attuale" , color = 'ff0000')
    
    #Logica per riavere la matrice funzionale 
    time.sleep(20)
    command = 'alt+3'  # Clicca il pulsante
    solverBot.send_input_gui(command)
    time.sleep(2)

    label = f'kz32'
    screenBot.take_screenshot(870, 330, 490, 620, label)
    img_name = f"Screenshot/screenshot{label}.png"
    immagine = cv2.imread(img_name)
    if immagine is None:
        print("Errore nel caricamento dell'immagine.")
        sys.exit()

    matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = x_global , y = y_global , side = side_global)  
   
    counter = 0
    slide_salagiochi = "alt+5"  # Imposta clicca "Spostati con la rotellina in giù"
    play_new_game = "alt+6"    # Imposta clicca  "Avvia nuovo gioco"
    start_game = "alt+7"     # Imposta clicca "Avvia partita"
    l_istruzioni = [slide_salagiochi, play_new_game, start_game]

    analyseBot.print_matrix(matrix_number)
    # press 'a' fino a quando la matrice risulta leggibile -> tempo da bruciare
    while (analyseBot.checkMatrixProduct(matrix_number) != 0):
        label = f'kz32'
        screenBot.take_screenshot(870, 330, 490, 620, label)
        img_name = f"Screenshot/screenshot{label}.png"
        immagine = cv2.imread(img_name)
        if immagine is None:
            print("Errore nel caricamento dell'immagine.")
            sys.exit()
        matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = x_global , y = y_global , side = side_global)   

        if counter % 10 == 0:      # Debug
            print_coloured.print_green_ts("Partita in chiusura... attendere")
        
        solverBot.send_input_gui('a+')    # Esegue una mossa
        time.sleep(4)
        counter += 1
        
    # tempo esaurito, iniziare nuova partita
    print_coloured.print_green_ts("partita terminata! currently in the end game menu")
    time.sleep(5)
    pyautogui.click(x=1110,y=939)   # Clicca il pulsante "Torna alla sala giochi"
    time.sleep(0.5)
    pyautogui.click(x=1110,y=939)   # Clicca il pulsante "Torna alla sala giochi"  [fatto 2 volte per problemi con l'APP]
    
    for i in range(len(l_istruzioni)):
        time.sleep(5)
        if i == 0:   # Caso in cui ci troviamo in Sala Giochi
            webhook_print(luke_webhook , "Update" , "🏆 Trofei 🏆" , color = '03b2f8' , img_name = "screenshot_update_trofei.png" , trofei_screen= True)
        solverBot.send_input_gui(l_istruzioni[i])


def memory_stats(action="None"):

        MB = 1048576

        if (action == "Start"):
            tracemalloc.start()
        if (action == "Stop"):
            tracemalloc.stop()
        if (action == "Print"):
            current, peak = tracemalloc.get_traced_memory()
            print(
                f"Istantanea = {int(current/MB)}Mb  ( {current}B )\n-----Picco = {int(peak/MB)}Mb  ( {peak}B )")



try:
    # Setting
    os.system("color")  # abilita i colori nella shell

    # Globals
    num_righe = solverBot.num_righe
    num_colonne = solverBot.num_colonne

    # MAIN
    print("\n\n")
    testo = "Game Solver"
    fig = pyfiglet.Figlet()
    ascii_art = fig.renderText(testo)
    print(f"{Fore.GREEN} {ascii_art} {Style.RESET_ALL}", end='')
    print(f"{Fore.GREEN}Developed by lucaAnza & Manillin !{Style.RESET_ALL}")
    print("\n\n")
    print(f"{Fore.GREEN}Press S to start! {Style.RESET_ALL}", end='')
    fuck_it_we_ball = input("")
    if fuck_it_we_ball != 's':
        print(f"{Fore.RED}Script terminated...{Style.RESET_ALL}")
        sys.exit(1)
    print("Starting...")
    time.sleep(2)

    memory_stats("Start")
    consecutive_error = 0
    general_counter = 0
    old_product = 0
    while (consecutive_error < 100):

        print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}")
        start_time = datetime.datetime.now()  # debugging tempo

        # logica per new_game:
        if general_counter == game_iteration:
            try:
                asc = fig.renderText("TERMINAZIONE GAME")
                print_coloured.print_red_ts("")
                print(f"{Fore.RED}{asc}{Style.RESET_ALL}")
                create_new_game()
                #Ripristino variabili ciclo
                consecutive_error = 0
                general_counter = 0
                old_product = 0
                game_started_successfully()
                time.sleep(2)
                webhook_print(chri_webhook , "Update" , "Inizio partita" , color = '03b2f8' , img_name="screenshot_partita_nuova.png")
            except Exception as e:
                print_coloured.print_red_ts(e)
                time.sleep(5)
                failed_game_wh()
                sys.exit()
                

        # potenziale fix when stuck
        if consecutive_error == 80:
            check_error()

        time.sleep(0.8)  # Ossigeno al processore

        # Cattura screenshot
        label = f'kz32'
        screenBot.take_screenshot(870, 330, 490, 620, label)
        #screenBot.take_screenshot(870, 330, 490, 620, f"{label}-FULLSCREENCHRIS", fullScreen=True) per salvare fullscreen
        img_name = f"Screenshot/screenshot{label}.png"
        immagine = cv2.imread(img_name)
        if immagine is None:
            print("Errore nel caricamento dell'immagine.")
            sys.exit()

        matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = x_global , y = y_global , side = side_global)  

        # Se almeno un elemento non l'ha riconosciuto [ prod == 0] non entra.
        if (analyseBot.checkMatrixProduct(matrix_number) != 0):

            # Debug analisi
            print(f"\n{Fore.YELLOW}Matrix : ")
            analyseBot.print_matrix(matrix_number)
            print(f"{Style.RESET_ALL}\n")

            print(
                f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')

            if consecutive_error == 80:    # Se entra cui significa che è riuscito a risolvere lo stallo
                stall_fixed()
            consecutive_error = 0   
            solverBot.scan_matrice(matrix_number)  # Esegue una mossa in base alla matrice di item dati in input
        else:
            print(f'{Fore.RED}Error {consecutive_error} {Style.RESET_ALL}')
            # Debug analisi
            print(f"\n{Fore.YELLOW}Matrix : ")
            analyseBot.print_matrix(matrix_number)
            print(f"{Style.RESET_ALL}\n")
            consecutive_error += 1

        end_time = datetime.datetime.now()
        exe_time = end_time-start_time
        print(f"{Fore.CYAN}Tempo esecuzione WHILE : {exe_time}{Style.RESET_ALL}")
        print(f"\n{Fore.MAGENTA}------------------Iterazione({general_counter})------------------{Style.RESET_ALL}\n\n")
        general_counter += 1

        # Controlli ogni tot cicli
        how_much = 2000
        if (general_counter % how_much == 0):
            # Controllo memoria
            memory_stats("Print")
            
            # Update bot discord
            webhook_print(luke_webhook , "Update" , f"⬤ Complimenti hai raggiunto {general_counter} iterazioni!" , color = '03b2f8' , img_name=f'screenshot_{general_counter}_iterazioni.png')
            webhookL = DiscordWebhook(url=luke_webhook)
            print_coloured.print_green_ts("Webhook sent!")
    memory_stats("Stop")


except Exception as e:
    print(f"Errore{e}")
    webhook_print(chri_webhook , "Errore durante l'esecuzione" , "Error: {e}" , color = 'ff0000' )
    # Termina lo script
    sys.exit(1)

# webhook in caso di terminazione
webhook_print(chri_webhook , "Checkpoint" , "Script terminated... check terminal" , color = '03b2f8' )
webhook_print(luke_webhook , "Update" , "TERMINAZIONE" , color = '03b2f8' , img_name='screenshot_dd_termination.png')

