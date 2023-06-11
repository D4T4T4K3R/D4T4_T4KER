#Domain to IP

import pyfiglet
import socket
from termcolor import colored

banner = colored (pyfiglet.figlet_format("D4T4 T4k3R"),'green') #Banner+color
print(banner)
print(colored("**************** Create By D4T4 T4K3R ********************",'green'))#color print



print("                                                                           ")

Domain_name = input('Enter Your Target Domain : ')

ip = socket.gethostbyname(Domain_name)

print(ip)

