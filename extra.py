# os.system("clear")
# z = int(sys.argv[1])
# file = open(f'replay/{z}.txt', "r")
# lines = file.readlines()
# count = 0

# while True:
    # Removing Cursor from Terminal     
    # os.system("tput civis")
    # if Not_Started == False:
    #     # break
    #     if count == len(lines):
    #         break
    #     called = lines[count][0]
    #     count += 1
    #
    #
    #
    # time.sleep(0.3)



from turtle import color
from matplotlib.pyplot import fill

from numpy import char
from input import *
import os
import time
from colorama import Fore, Back, Style
from src.header import *
from src.init import *
from src.buildings import *
from src.king import *
from src.spell import *
from src.troops import *

os.system("clear")
z = int(sys.argv[1])
file = open(f'replay/{z}.txt', "r")
lines = file.readlines()
count = 0
while True:
    # Removing Cursor from Terminal     
    os.system("tput civis")
    if Not_Started == False:
        if count == len(lines):
            break
        called = lines[count][0]
        count += 1
        if called == 'q':
            # os.system("clear")
            break
        elif called == 'a' or called == 'd' or called == 'w' or called == 's':
            king.move(king_pos, huts ,cannons ,called, all_troops)   
            # troop.move(huts,cannons,list_buildings)   
        elif called == ' ':
            king.attack(town_hall, king_pos, huts,cannons ,called, all_troops)
        elif called == 'h' or called == 'r':
            spell = Spell(called)
            spell.cast()
        elif called =='i' or called == 'o' or called == 'p':
            troop_gen = Troops(called)
            all_troops.append(troop_gen)
            troop_gen.build(called)
    Not_Started = False
    os.system("clear")
    # Base of the village
    # for i in range(46):
    #     board[0][i] = '-'
    #     board[1][i] = '-'
    #     board[19][i] = '-'
    #     board[20][i] = '-'
    #     filled[0][i] = 'BORDER'
    #     filled[1][i] = 'BORDER'
    #     filled[19][i] = 'BORDER'
    #     filled[20][i] = 'BORDER'
    # for i in range(21):
    #     board[i][0] = '|'
    #     board[i][45] = '|'
    #     filled[i][0] = 'BORDER'
    #     filled[i][45] = 'BORDER'

    # Town Hall for the base
    # town_hall_shape = [[i, j, '#'] for i in range(3) for j in range(5)]
    # town_hall = Buildings('Town Hall', 7, 18, town_hall_shape)
    town_hall.build()

    # Making the Huts for the base
    for i in huts:
        i.build()
    

    # Building Walls around the Town Hall
    # for i in range(15, 26):
    #     board[5][i] = 'W'
    #     board[11][i] = 'W'
    # for i in range(5, 12):
    #     board[i][15] = 'W'
    #     board[i][25] = 'W'
    # for i in walls:
    #     i.build()
    # Entry for the Foreign Troops
    board[4][0] = 'i'
    board[7][WIDTH_BASE-1] = 'o'
    board[1][23] = 'p'

    # Cannon for protecting the base
    # cannon_pos = [[7, 5], [13, 19], [9, 29]]
    # cannon_shape = [[i, j, 'C'] for i in range(2) for j in range(2)]
    # cannon1 = Buildings(
    #     'Cannon1', cannon_pos[0][0], cannon_pos[0][1], cannon_shape)
    # cannon2 = Buildings(
    #     'Cannon2', cannon_pos[1][0], cannon_pos[1][1], cannon_shape)
    # cannon3 = Buildings(
    #     'Cannon3', cannon_pos[2][0], cannon_pos[2][1], cannon_shape)
    # cannons = [cannon1, cannon2, cannon3]
    for i in cannons:
        i.build()
        # i.power_on = False
    
    # KING
    
    king.build()

    for trp in all_troops:
        trp.move(huts,cannons,list_buildings)
    #     print(i.health)
    # print(all_troops)
    # troop.build(called='i')
    # Printing Board B&W
    # print(Fore.RED, end='')
    # for i in range(21):
    #     for j in range(46):
    #         print(board[i][j], end='')
    #     print()

    # Printing board
    for i in range(21):
        for j in range(46):
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
    print("KING MOVEMENT SPEED IS: " + str(king.speed))
    ## if all BUILDINGS are destroyed
    print("TOTAL BUILDINGS ARE:  " + str(Buildings.TOTAL_BUILDING))
    if Buildings.TOTAL_BUILDING == 0:
        print(r"""
            ___  _ ____  _       _      ____  _     
            \  \///  _ \/ \ /\  / \  /|/  _ \/ \  /|
             \  / | / \|| | ||  | |  ||| / \|| |\ ||
             / /  | \_/|| \_/|  | |/\||| \_/|| | \||
            /_/   \____/\____/  \_/  \|\____/\_/  \|
            """)                 
        break
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
        break
    time.sleep(0.2)    
    # print sum of health of all huts
    # print("Health of TH: " + str(town_hall.health))
    # print("HEALTH OF ALL HUTS IS: " + str(hut1.health + hut2.health + hut3.health + hut4.health + hut5.health))
    # print("HEALTH OF ALL CANNONS IS: " + str(cannon1.health + cannon2.health + cannon3.health))
    # print("HEALTH OF ALL WALLS IS: " + str(Wall1.health))
