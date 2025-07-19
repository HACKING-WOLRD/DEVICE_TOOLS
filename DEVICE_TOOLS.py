from os import system as c
import time

#--------- COLOUR ---------#
G = '\x1b[38;5;46m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
C = '\x1b[38;5;14m'

def logo():
    c('clear')
    print(f"""{G}
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║
███████║███████║██║     █████╔╝ ██║██╔██╗ ██║
██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║
██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
         {Y}HACKING WORLD - DEVICE TOOL 
""")

def root_prank():
    logo()
    print(f"{Y}[+] Checking Root Permission...")
    time.sleep(2)
    print(f"{R}[!] Root Permission Required!")
    time.sleep(2)
    print(f"{C}Requesting Root Access...\n")
    time.sleep(3)
    print(f"{R}[X] Root Access Denied!\n")
    time.sleep(1)
    print(f"{R}Tool Stopped Automatically!")
    time.sleep(2)
    exit()

root_prank()