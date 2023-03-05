import os
import re
import string
import sys
import hashlib

import requests
from colored import fg, attr


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f'{fg(255)}')
    print(f'{fg(196)}╔══════════════════════════════════════════════╗')
    print(f'{fg(196)}║████████╗██╗░░░██╗██╗███╗░░██╗░██████╗░██████╗░║')
    print(f'{fg(196)}║╚══██╔══╝██║░░░██║██║████╗░██║██╔════╝░██╔══██╗║')
    print(f'{fg(196)}║░░░██║░░░██║░░░██║██║██╔██╗██║██║░░██╗░██████╔╝║')
    print(f'{fg(196)}║░░░██║░░░██║░░░██║██║██║╚████║██║░░╚██╗██╔══██╗║')
    print(f'{fg(196)}║░░░██║░░░╚██████╔╝██║██║░╚███║╚██████╔╝██║░░██║║')
    print(f'{fg(196)}║░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝║')
    print(f'{fg(196)}╚══════════════════════════════════════════════╝')
    print(f'{fg(130)}       Made by MrShadowDev')
    print('')

def get_link():
    old_link = input(f'[{fg(118)}+{attr("reset")}] {fg(118)}Enter Linkvertise link: {attr("reset")}')
    url = "https://bypass.bot.nu/bypass2?url="
    response = requests.get(url + old_link)
    link = response.json()['destination']
    return link


def show_credits():
    clear_screen()
    print(f"{fg(118)}+-------------------------+")
    print(f"         Made by         ")
    print(f"   Credits:                ")
    print(f"     - MrShadowDev           ")
    print(f"+-------------------------+{attr('reset')}")
    input("Press Enter to continue...")


def change_theme():
    clear_screen()
    print(f"{fg(118)}+-------------------------+")
    print(f"   Choose a theme:         ")
    print(f"                           ")
    print(f"  1) Default              ")
    print(f"  2) Dark mode            ")
    print(f"  3) Light mode           ")
    print(f"                           ")
    print(f"+-------------------------+{attr('reset')}")
    option = input("Enter your choice (1/2/3): ")
    if option == "1":
        os.system("color")
    elif option == "2":
        os.system("color 0f")
    elif option == "3":
        os.system("color f0")
    input("Theme changed successfully. Press Enter to continue...")


def main():
    clear_screen()
    print(f"{fg(118)}+-------------------------+")
    print(f"   Welcome to TUINGR   ")
    print(f"                           ")
    print(f"  1) Bypasser             ")
    print(f"  2) Credits              ")
    print(f"  3) Change theme         ")
    print(f"  4) Exit program         ")
    print(f"                           ")
    print(f"+-------------------------+{attr('reset')}")
    option = input("Enter your choice (1/2/3/4): ")
    if option == "1":
        clear_screen()
        print_banner()
        link = get_link()
        clear_screen()
        print_banner()
        print(f'{fg(196)}Your destination URL is: {link}')
        input(f"{fg(118)}Press Enter to continue...{attr('reset')}")
    elif option == "2":
        show_credits()
        main()
    elif option == "3":
        change_theme()
        main()
    elif option == "4":
        clear_screen()
        print("Exiting program...")
        sys.exit()
    else:
        print("Invalid input. Please try again.")
        main()


if __name__ == '__main__':
    # Calculate the SHA-256 hash of the script
    with open(sys.argv[0], "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    print(f"Script hash: {file_hash}")

    main()
