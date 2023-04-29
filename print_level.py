from colorama import Fore

def print_success(message: str, color=Fore.GREEN, stop=Fore.RESET):
    print(color + message + stop)

def print_red(message: str, color=Fore.RED, stop=Fore.RESET):
    print(color + message + stop)
