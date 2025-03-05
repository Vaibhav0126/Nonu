import sys
import time
import os
from colorama import Fore, Style, init

init(autoreset=True)

def typewriter_effect(text, delay=0.1, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_rose():
    rose = [
        "      @@@    ",
        "     @@@@@   ",
        "      @@@    ",
        "       |     ",
        "       |     ",
        "     --|--   ",
        "       |     ",
        "       |     "
    ]
    for line in rose:
        print(Fore.RED + line)
        time.sleep(0.2)
    typewriter_effect("For my love 🌹", 0.1, Fore.RED)

def print_heart():
    heart = [
        "  *****     *****  ",
        "*******   ********* ",
        "*******************",
        "*******************",
        " ***************** ",
        "  ***************  ",
        "    ************    ",
        "      ********      ",
        "       *****       ",
        "        ***        ",
        "         *        "
    ]
    for line in heart:
        print(Fore.RED + line)
        time.sleep(0.2)
    typewriter_effect("And this heart… it belongs only to you ❤️", 0.1, Fore.RED)

def main():
    typewriter_effect("If I could, I’d give you a thousand flowers...", 0.1, Fore.MAGENTA)
    time.sleep(1)
    typewriter_effect("But I am a software engineer (living away from home (obv you Nonu)), so here’s a virtual one. 🌹", 0.1, Fore.MAGENTA)
    time.sleep(1)
    print_rose()
    time.sleep(1)

    typewriter_effect("And something even more precious...", 0.1, Fore.CYAN)
    time.sleep(1)
    print_heart()
    time.sleep(1)

    typewriter_effect("No matter the distance, my heart will always belong to you. 💕", 0.1, Fore.YELLOW)
    typewriter_effect("I love you Nonu ❤️", 0.1, Fore.MAGENTA)

if __name__ == "__main__":
    main()
