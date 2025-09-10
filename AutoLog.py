from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime
init()

def log(col = None, text = ""):
    add=""
    if col == "r":
        add = Fore.RED+"#RED"
    elif col == "g":
        add = Fore.GREEN+"#GRN"
    elif col == "gw":
        add = Style.DIM+"#GRY"
    elif col == "w":
        add = Style.BRIGHT+"#WHT"
    elif col == "y":
        add = Fore.YELLOW+"#YEL"
    elif col == "b":
        add = Fore.BLUE+"#BLU"
    elif col == "p":
        add = Fore.MAGENTA+"#PUR"
    print(Fore.WHITE+ Style.NORMAL +str(datetime.now()) +add +" >>"+ text+Fore.WHITE+ Style.NORMAL)