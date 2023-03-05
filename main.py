import os 
import re 
import string 
import sys 
import hashlib 
import requests
from colored import fg ,attr 
def clear_screen ():
    os .system ('cls'if os .name =='nt'else 'clear')
def print_banner ():
    clear_screen ()
    print (f'{fg(255)}')
    print (f'{fg(196)}╔══════════════════════════════════════════════╗')
    print (f'{fg(196)}║████████╗██╗░░░██╗██╗███╗░░██╗░██████╗░██████╗░║')
    print (f'{fg(196)}║╚══██╔══╝██║░░░██║██║████╗░██║██╔════╝░██╔══██╗║')
    print (f'{fg(196)}║░░░██║░░░██║░░░██║██║██╔██╗██║██║░░██╗░██████╔╝║')
    print (f'{fg(196)}║░░░██║░░░██║░░░██║██║██║╚████║██║░░╚██╗██╔══██╗║')
    print (f'{fg(196)}║░░░██║░░░╚██████╔╝██║██║░╚███║╚██████╔╝██║░░██║║')
    print (f'{fg(196)}║░░░╚═╝░░░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝║')
    print (f'{fg(196)}╚══════════════════════════════════════════════╝')
    print (f'{fg(130)}       Made by MrShadowDev')
    print ('')
def get_link ():
    O0O000O00000O000O =input (f'[{fg(118)}+{attr("reset")}] {fg(118)}Enter Linkvertise link: {attr("reset")}')
    OOO00OO00OO0O00O0 ="https://bypass.bot.nu/bypass2?url="
    O00OOO0O00OO00O0O =requests .get (OOO00OO00OO0O00O0 +O0O000O00000O000O )
    O0OO0O00OO00O00OO =O00OOO0O00OO00O0O .json ()['destination']
    return O0OO0O00OO00O00OO 
def show_credits ():
    clear_screen ()
    print (f"{fg(118)}+-------------------------+")
    print (f"         Made by         ")
    print (f"   Credits:                ")
    print (f"     - MrShadowDev           ")
    print (f"+-------------------------+{attr('reset')}")
    input ("Press Enter to continue...")
def change_theme ():
    clear_screen ()
    print (f"{fg(118)}+-------------------------+")
    print (f"   Choose a theme:         ")
    print (f"                           ")
    print (f"  1) Default              ")
    print (f"  2) Dark mode            ")
    print (f"  3) Light mode           ")
    print (f"                           ")
    print (f"+-------------------------+{attr('reset')}")
    OOOO000O00O000OO0 =input ("Enter your choice (1/2/3): ")
    if OOOO000O00O000OO0 =="1":
        os .system ("color")
    elif OOOO000O00O000OO0 =="2":
        os .system ("color 0f")
    elif OOOO000O00O000OO0 =="3":
        os .system ("color f0")
    input ("Theme changed successfully. Press Enter to continue...")
def main ():
    clear_screen ()
    print (f"{fg(118)}+-------------------------+")
    print (f"   Welcome to TUINGR   ")
    print (f"                           ")
    print (f"  1) Bypasser             ")
    print (f"  2) Credits              ")
    print (f"  3) Change theme         ")
    print (f"  4) Exit program         ")
    print (f"                           ")
    print (f"+-------------------------+{attr('reset')}")
    OOO00O00O0O0OOOO0 =input ("Enter your choice (1/2/3/4): ")
    if OOO00O00O0O0OOOO0 =="1":
        clear_screen ()
        print_banner ()
        O0O0OO00O000O00OO =get_link ()
        clear_screen ()
        print_banner ()
        print (f'{fg(196)}Your destination URL is: {O0O0OO00O000O00OO}')
        input (f"{fg(118)}Press Enter to continue...{attr('reset')}")
    elif OOO00O00O0O0OOOO0 =="2":
        show_credits ()
        main ()
    elif OOO00O00O0O0OOOO0 =="3":
        change_theme ()
        main ()
    elif OOO00O00O0O0OOOO0 =="4":
        clear_screen ()
        print ("Exiting program...")
        sys .exit ()
    else :
        print ("Invalid input. Please try again.")
        main ()
if __name__ =='__main__':
    with open (sys .argv [0 ],"rb")as f :
        file_hash =hashlib .sha256 (f .read ()).hexdigest ()
    print (f"Script hash: {file_hash}")
    main ()
