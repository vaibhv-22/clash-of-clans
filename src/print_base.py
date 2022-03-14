from colorama import Fore, Back, Style
from .header import *
from .buildings import *
from .init import *
from .king import *
def printing_base():
    for i in range(HEIGHT_BASE):
        for j in range(WIDTH_BASE):
            if board[i][j] == '#':
                if town_hall.health > HEALTH_TOWN/2:
                    print(Fore.GREEN + board[i][j], end='')
                elif town_hall.health > HEALTH_TOWN/4:
                    print(Fore.YELLOW + board[i][j], end='')
                else:
                    print(Fore.RED + board[i][j], end='')
                print(Fore.RESET, end='')
            elif board[i][j] == 'C':
                if cannons[(int)(filled[i][j][6])-1].power_on == True:
                    print(Back.WHITE, end='')
                if cannons[(int)(filled[i][j][6])-1].health > HEALTH_CANNON/2:
                    print(Fore.GREEN + board[i][j], end='')
                    print(Fore.RESET, end='')
                elif cannons[(int)(filled[i][j][6])-1].health > HEALTH_CANNON/4:
                    print(Fore.YELLOW + board[i][j], end='')
                    print(Fore.RESET, end='')
                else:
                    print(Fore.RED + board[i][j], end='')
                    print(Fore.RESET, end='')
                print(Back.RESET, end='')
            elif len(filled[i][j]) > 0 and filled[i][j][0] == 'h':
                if huts[(int)(filled[i][j][3])-1].health > HEALTH_HUT/2:
                    print(Fore.GREEN + board[i][j], end='')
                    print(Fore.RESET, end='')
                elif huts[(int)(filled[i][j][3])-1].health > HEALTH_HUT/4:
                    print(Fore.YELLOW + board[i][j], end='')
                    print(Fore.RESET, end='')
                else:
                    print(Fore.RED + board[i][j], end='')
                    print(Fore.RESET, end='')
            elif board[i][j] == 'W':
                print(Fore.BLUE + Back.LIGHTMAGENTA_EX + 'W', end='')
                print(Fore.RESET, end='')
                print(Back.RESET, end='')
            else:
                print(board[i][j], end='')
        print()
    healthDisplay = ' ' * int(king.health*10/HEALTH_KING)  
    remainingDisplay = ' ' * (10 - int(king.health*10/HEALTH_KING))
    print("King's Health : |" + Back.GREEN + healthDisplay + Back.RED + remainingDisplay + Back.RESET + "|" )  # Print out textbased healthbar
    if Buildings.TOTAL_BUILDING == 0:
        print(r"""
            ___  _ ____  _       _      ____  _     
            \  \///  _ \/ \ /\  / \  /|/  _ \/ \  /|
             \  / | / \|| | ||  | |  ||| / \|| |\ ||
             / /  | \_/|| \_/|  | |/\||| \_/|| | \||
            /_/   \____/\____/  \_/  \|\____/\_/  \|
            """)                 
        return -1
    total_troops_health = 0
    for i in all_troops:
        if i.health <= 0:
            i.health = 0
        total_troops_health += i.health
    if king.health <= 0 and total_troops_health <= 0:
        print(r"""
            ___  _ ____  _       _     ____  ____  _____
            \  \///  _ \/ \ /\  / \   /  _ \/ ___\/  __/
             \  / | / \|| | ||  | |   | / \||    \|  \  
             / /  | \_/|| \_/|  | |_/\| \_/|\___ ||  /_ 
            /_/   \____/\____/  \____/\____/\____/\____\
        """)
        return -1