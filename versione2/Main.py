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

webhook_url = "https://discord.com/api/webhooks/1184788603470090320/jqkYHRC-y7P920AYLdB1e08g1WPLWzIcelEssk1tG23VXXE2kvgsNUQUhg5q7fYZ86hU"


try:
    # Setting
    os.system("color")  # abilita i colori nella shell

    # Globals
    num_righe = solverBot.num_righe
    num_colonne = solverBot.num_colonne



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


    # MAIN
    print("\n\n")
    testo = "Game Solver"
    fig = pyfiglet.Figlet()
    ascii_art = fig.renderText(testo)
    print(f"{Fore.GREEN} {ascii_art} {Style.RESET_ALL}", end='')
    # print(f"{Fore.GREEN}Developed by lanza & manillin !{Style.RESET_ALL}")
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


        time.sleep(0.8)  # Ossigeno al processore

        # Cattura screenshot
        label = f'kz32'
        
        screenBot.take_screenshot(870, 330, 490, 620, label)      

        img_name = f"Screenshot/screenshot{label}.png"
        immagine = cv2.imread(img_name)
        if immagine is None:
            print("Errore nel caricamento dell'immagine.")
            sys.exit()
        
        
        #matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = 5 , y = 20 , side = 93)   # Lucas-pc
        matrix_number = analyseBot.get_matrix_item(immagine , type="Number" , x = 6 , y = 23 , side = 94)   # Chris-pc 

        
        # Se almeno un elemento non l'ha riconosciuto [ prod == 0] non entra.
        if (analyseBot.checkMatrixProduct(matrix_number) != 0):
            
            # Debug analisi
            print(f"\n{Fore.YELLOW}Matrix : ")
            analyseBot.print_matrix(matrix_number)
            print(f"{Style.RESET_ALL}\n")

            print(
                f'{Fore.GREEN}Check della matrice andato a buon fine!{Style.RESET_ALL}')
            consecutive_error = 0
            solverBot.scan_matrice(matrix_number)     # Esegue una mossa in base alla matrice di item dati in input
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
        
        if (general_counter % 500 == 0):     # Controllo memoria 
            memory_stats("Print")



    memory_stats("Stop")
except Exception as e:
    print(f"Errore{e}")
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="Errore durante l'esecuzione", description=f'Error: {e}', color='ff0000')
    embed.set_author(name="Il bro Ferretty")
    embed.set_footer(text="TCP?")
    embed.set_timestamp()
    webhook.add_embed(embed)
    webhook.execute()
    # Termina lo script
    sys.exit(1)

#webhook in caso di terminazione / soluzione momentanea 
webhook = DiscordWebhook(url=webhook_url)
embed = DiscordEmbed(title="Checkpoint",
                     description="Script terminated... check terminal", color="03b2f8")
embed.set_author(name="Il bro Ferretty")
embed.set_footer(text="TCP?")
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()


#ctrl+h