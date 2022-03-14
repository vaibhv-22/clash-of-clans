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
from src.print_base import *

def builds(objecttype):
    objecttype.build()

os.system("clear")
list = os.listdir("replay")
number_files = len(list)
z = number_files - int(sys.argv[1]) + 1
file = open(f'replay/{z}.txt', "r")
lines = file.readlines()
count = 0
while True:
    # Removing Cursor from Terminal     
    os.system("tput civis")
    if count == len(lines):
        break
    called = lines[count][0]
    count += 1
    if called == 'q':
        break
    elif called == 'a' or called == 'd' or called == 'w' or called == 's':
        king.move(king_pos, huts ,cannons ,called, all_troops)   
    elif called == ' ' or called == 'l':
        king.attack(town_hall, king_pos, huts,cannons ,called, all_troops)
    elif called == 'h' or called == 'r':
        spell = Spell(called)
        spell.cast(king,all_troops)
    elif called =='i' or called == 'o' or called == 'p':
        for i in cannons:
            i.attack(king,king_pos, all_troops)
        troop_gen = Troops(called)
        all_troops.append(troop_gen)
        troop_gen.build(called)
    elif called == None:
        for i in cannons:
            i.attack(king,king_pos, all_troops)
    os.system("clear")

    # Entry for the Foreign Troops
    board[4][0] = 'i'
    board[7][WIDTH_BASE-1] = 'o'
    board[1][23] = 'p'

    # Building all the buildings
    for i in list_buildings:
        builds(i)
    
    # KING    
    king.build()

    # Moving the troops for this loop
    for trp in all_troops:
        trp.move(huts,cannons,list_buildings)

    # Printing board
    k = printing_base()
    if k == -1:
        break
    time.sleep(0.2)