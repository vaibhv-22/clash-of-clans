from ctypes import sizeof
from .header import *
from .buildings import *
from .king import King
from .troops import Troops
for i in range(WIDTH_BASE):
        board[0][i] = '-'
        board[1][i] = '-'
        board[HEIGHT_BASE-2][i] = '-'
        board[HEIGHT_BASE-1][i] = '-'
        filled[0][i] = 'BORDER'
        filled[1][i] = 'BORDER'
        filled[HEIGHT_BASE-2][i] = 'BORDER'
        filled[HEIGHT_BASE-1][i] = 'BORDER'
for i in range(HEIGHT_BASE):
    board[i][0] = '|'
    board[i][WIDTH_BASE - 1] = '|'
    filled[i][0] = 'BORDER'
    filled[i][WIDTH_BASE - 1] = 'BORDER'
list_buildings = []
all_troops = []
town_hall_shape = [[i, j, '#'] for i in range(3) for j in range(5)]
town_hall = Buildings('Town Hall', 7, 18, town_hall_shape)
list_buildings.append(town_hall)
town_hall.build()

hut_pos = [[3, 7], [4, 30], [11, 8], [15, 25], [13, 33]]
hut_shape = [[0, 0, '_'], [1, -1, '/'], [1, 1, '\\'],
                [2, -1, '|'], [2, 0, '_'], [2, 1, '|']]
hut1 = Buildings('hut1', hut_pos[0][0], hut_pos[0][1],  hut_shape)
hut2 = Buildings('hut2', hut_pos[1][0], hut_pos[1][1], hut_shape)
hut3 = Buildings('hut3', hut_pos[2][0], hut_pos[2][1], hut_shape)
hut4 = Buildings('hut4', hut_pos[3][0], hut_pos[3][1], hut_shape)
hut5 = Buildings('hut5', hut_pos[4][0], hut_pos[4][1], hut_shape)
huts = [hut1, hut2, hut3, hut4, hut5]
for i in huts:
    list_buildings.append(i)
    i.build()

cannon_pos = [[7, 5], [13, 19], [9, 29]]
cannon_shape = [[i, j, 'C'] for i in range(2) for j in range(2)]
cannon1 = Cannon('Cannon1', cannon_pos[0][0], cannon_pos[0][1], cannon_shape)
cannon2 = Cannon('Cannon2', cannon_pos[1][0], cannon_pos[1][1], cannon_shape)
cannon3 = Cannon('Cannon3', cannon_pos[2][0], cannon_pos[2][1], cannon_shape)
cannons = [cannon1, cannon2, cannon3]
for i in cannons:
    list_buildings.append(i)
    i.build()

for i in range(15, 26):
        board[5][i] = 'W'
        board[11][i] = 'W'
        filled[5][i] = 'walls'
        filled[11][i] = 'walls'
for i in range(5, 12):
    board[i][15] = 'W'
    board[i][25] = 'W'
    filled[i][15] = 'walls'
    filled[i][25] = 'walls'



king_pos = [18,2]
king = King(king_pos)
troop = Troops([0,0])
Not_Started = True
