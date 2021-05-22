from colorama import init
from colorama import Fore, Back, Style
init()

print(Back.BLUE + 'Welcome to the:')
print(' ______         __                            ')
print('|      |.-----.|  |.-----..----..-----..-----.')
print('|   ---||  _  ||  ||  _  ||   _||  -__||  _  |')
print('|______||_____||__||_____||__|  |_____||___  |')
print('                                       |_____|')
print(Style.RESET_ALL)
print(Fore.YELLOW + 'Enter text: ')
text = input()
print(Fore.CYAN + text)
print(Fore.BLUE + text)
print(Fore.GREEN + text)
print(Fore.YELLOW + text)
print(Fore.RED + text)
print(Fore.MAGENTA + text)