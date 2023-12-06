import time
import datetime
from colorama import Fore, Style


def func():
    start_time = datetime.datetime.now()
    print(
        f"{Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} PRINT1 {Style.RESET_ALL}")
    print(
        f"{Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} PRINT2 {Style.RESET_ALL}")
    print(
        f"{Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} PRINT3 {Style.RESET_ALL}")
    end_time = datetime.datetime.now()
    print()
    print(
        f"{Fore.RED}{time.strftime('%H:%M:%S:%f')[:-3]} Tempo esecuzione {end_time-start_time} {Style.RESET_ALL}")


print("Starting...")
time.sleep(0.8)
func()
