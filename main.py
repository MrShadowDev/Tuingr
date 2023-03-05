import os
import sys
from colored import fg, attr

def clear_screen():
    os.system(f"{fg(118)}{'cls' if os.name == 'nt' else 'clear'}{attr('reset')}")

def print_banner():
    clear_screen()
    banner = ["█████████╗██╗░░░██╗██╗███╗░░██╗░██████╗░██████╗░",
              "╚══██╔══██╗░░░██║██║████╗░██║██╔════╝░██╔══██╗",
              "░░░██║░░░██║░░░██║██║██╔██╗██║██║░░██╗░██████╔╝",
              "░░░██║░░░██║░░░██║██║██║╚████║██║░░╚██╗██╔══██╗",
              "░░░██║░░░╚██████╔╝██║██║░╚███║╚██████╔╝██║░░██║",
              "░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚══╝"]
    print(f"{fg(118)}{'╔'+('═'*48)+'╗'}")
    print("\n".join([f"{fg(118)}{'║'+r.center(48)+'║'}" for r in banner]))
    print(f"{fg(118)}{'╚'+('═'*48)+'╝'}")
    print(f"{fg(255)}{' '*14}Made by MrShadowDev\n")


def get_link():
    while True:
        linkvertise_link = input(f'{fg(118)}+{attr("reset")} {fg(118)}Enter Linkvertise link: {attr("reset")}')
        if linkvertise_link.startswith(("http://", "https://")):
            break
        print(f"{fg(196)}Invalid input. Please enter a valid URL.{attr('reset')}")
    return requests.get(f"https://bypass.bot.nu/bypass2?url={linkvertise_link}").json()["destination"]

def show_credits():
    clear_screen()
    print(f"{fg(196)}+-------------------------+")
    print(f"         Made by         ")
    print(f"   Credits:                ")
    print(f"     {fg(196)}- MrShadowDev{fg(196)}           ")
    print(f"{fg(196)}+-------------------------+{attr('reset')}")
    input(f"{fg(118)}Press Enter to continue...{attr('reset')}")

def change_theme():
    clear_screen()
    print(f"{fg(118)}+-------------------------+")
    print(f"   Choose a theme:         ")
    print(f"                           ")
    print(f"  1) Default              ")
    print(f"  2) Cyberpunk            ")
    print(f"  3) Matrix               ")
    print(f"  4) Green on Black       ")
    print(f"                           ")
    print(f"+-------------------------+{attr('reset')}")

    valid_choices = ("1", "2", "3", "4")
    theme_codes = {"1": "", "2": "0d", "3": "02", "4": "0a"}

    while True:
        user_choice = input(f"{fg(118)}Enter your choice (1/2/3/4): {attr('reset')}")
        if user_choice in valid_choices:
            break
        print(f"{fg(196)}Invalid input. Please enter a valid choice.{attr('reset')}")

    os.system(f"color {theme_codes[user_choice]}")
    clear_screen()
    input(f"{fg(118)}Theme changed successfully. Press Enter to continue...{attr('reset')}")    


def main():
    while True:
        clear_screen()
        print(f"{fg(118)}╔═══════════════════════════════════════════════╗")
        print(f"{fg(118)}║████████╗██╗░░░██╗██╗███╗░░██╗░██████╗░██████╗░║")
        print(f"{fg(118)}║╚══██╔══╝██║░░░██║██║████╗░██║██╔════╝░██╔══██╗║")
        print(f"{fg(118)}║░░░██║░░░██║░░░██║██║██╔██╗██║██║░░██╗░██████╔╝║")
        print(f"{fg(118)}║░░░██║░░░██║░░░██║██║██║╚████║██║░░╚██╗██╔══██╗║")
        print(f"{fg(118)}║░░░██║░░░╚██████╔╝██║██║░╚███║╚██████╔╝██║░░██║║")
        print(f"{fg(118)}║░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚══╝║")
        print(f"{fg(118)}╚═══════════════════════════════════════════════╝")

        print(f"{fg(118)}+-------------------------+")
        print(f"   Welcome to TUINGR   ")
        print(f"                           ")
        print(f"  1) Bypasser             ")
        print(f"  2) Credits              ")
        print(f"  3) Change theme         ")
        print(f"  4) Exit program         ")
        print(f"                           ")
        print(f"+-------------------------+{attr('reset')}")
        user_choice = input(f"{fg(118)}Enter your choice (1/2/3/4): {attr('reset')}")

        if user_choice == "1":
            clear_screen()
            print_banner()
            destination_url = get_link()
            clear_screen()
            print_banner()
            print(f"{fg(196)}Your destination URL is: {destination_url}")
            input(f"{fg(118)}Press Enter to continue...{attr('reset')}")
        elif user_choice == "2":
            show_credits()
        elif user_choice == "3":
            change_theme()
        elif user_choice == "4":
            clear_screen()
            print("Exiting program...")
            sys.exit()
        else:
            print(f"{fg(196)}Invalid input. Please try again.{attr('reset')}")
            continue



if __name__ == "__main__":
    main()
