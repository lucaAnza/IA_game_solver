import time
import sys
import pyautogui
from colorama import Fore, Style
import pyfiglet


'''print(f"{Fore.GREEN}Questo testo è verde!{Style.RESET_ALL}")
print(f"{Fore.RED}Questo testo è rosso!{Style.RESET_ALL}")
print(f"{Fore.YELLOW}Questo testo è giallo!{Style.RESET_ALL}")'''


######################################
#                MAIN                #
######################################


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

# INIZIO:
pyautogui.hotkey('COMBO', 'INIZIO')

flag = True
while flag:
    # controllo errori

    pass
