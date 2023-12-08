import datetime
from colorama import Fore, Style


def print_red_ts(stringa):
    print(
        f"{Fore.RED}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} {stringa}{Style.RESET_ALL}")


def print_green_ts(stringa):
    print(
        f"{Fore.GREEN}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} {stringa} {Style.RESET_ALL}"
    )


def print_cyan_ts(stringa):
    print(
        f"{Fore.LIGHTBLUE_EX}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} {stringa} {Style.RESET_ALL}"
    )


def print_magenta_ts(stringa):
    print(
        f"{Fore.MAGENTA}{datetime.datetime.now().strftime('%H:%M:%S:%f')[:-3]} {stringa} {Style.RESET_ALL}"
    )
