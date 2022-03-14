from matplotlib.pyplot import fill
from .header import *
from .buildings import *
from .init import *


class King:
    """Class to build attackers."""

    def __init__(self, pos):
        """Initializing class."""
        self.pos = pos
        self.health = HEALTH_KING
        self.speed = SPEED_KING
        self.attack_power = ATTACK_POWER_KING

    def build(self):
        """Building attackers."""
        if self.health > 0:
            board[self.pos[0]][self.pos[1]] = 'K'
            filled[self.pos[0]][self.pos[1]] = 'K'
        else:
            board[self.pos[0]][self.pos[1]] = 'D'
            filled[self.pos[0]][self.pos[1]] = ''

    def move(self, king_pos, huts, cannons, called, all_troops):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[king_pos[0]][king_pos[1]] = ' '
            filled[king_pos[0]][king_pos[1]] = ''
            if called == 'a':
                if(filled[king_pos[0]][max(king_pos[1] - 1, 1)] == ''):
                    king_pos[1] = max(king_pos[1] - 1, 1)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
            elif called == 'd':
                if(filled[king_pos[0]][min(king_pos[1] + 1, WIDTH_BASE - 2)] == ''):
                    king_pos[1] = min(king_pos[1] + 1, WIDTH_BASE - 2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
            elif called == 'w':
                if(filled[max(king_pos[0] - 1, 1)][king_pos[1]] == ''):
                    king_pos[0] = max(king_pos[0] - 1, 2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)
            elif called == 's':
                if(filled[min(king_pos[0] + 1, HEIGHT_BASE-2)][king_pos[1]] == ''):
                    king_pos[0] = min(king_pos[0] + 1, HEIGHT_BASE-2)
                    for i in cannons:
                        i.attack(self, king_pos, all_troops)

    def attack(self, town_hall, king_pos, huts, cannons, called, all_troops):
        for i in cannons:
            i.attack(self, king_pos, all_troops)
        direction =[]
        if called == ' ':
            direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for d in direction:
                if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                    if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'T'):
                        town_hall.health -= self.attack_power
                        os.system(
                            'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                        break
                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                        # Cannon1
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][6]) - 1
                        cannons[ind].health -= self.attack_power
                        os.system(
                            'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                        break

                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'h'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][3]) - 1
                        huts[ind].health -= self.attack_power
                        os.system(
                            'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                        break

                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                        filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                        board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
                        os.system(
                            'aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                        break
        else:
            for i in range(5):
                for j in range(5):
                    if i == 2 and j == 2:
                        continue
                    direction.append([i-2, j-2])
            for d in direction:
                if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != '' and filled[king_pos[0] + d[0]][king_pos[1] + d[1]] != 'BORDER'):
                    if(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'T'):
                        town_hall.health -= self.attack_power
                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'C'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][6]) - 1
                        cannons[ind].health -= self.attack_power
                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'h'):
                        ind = int(filled[king_pos[0] + d[0]]
                                    [king_pos[1] + d[1]][3]) - 1
                        huts[ind].health -= self.attack_power
                    elif(filled[king_pos[0] + d[0]][king_pos[1] + d[1]][0] == 'w'):
                        filled[king_pos[0] + d[0]][king_pos[1] + d[1]] = ''
                        board[king_pos[0] + d[0]][king_pos[1] + d[1]] = ' '
