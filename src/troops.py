from turtle import pos
from matplotlib.pyplot import fill
from numpy import Inf
from .header import *
from .buildings import *
from .init import *

class Troops:
    """Class to build attackers."""

    def __init__(self, called):
        """Initializing class."""
        self.pos = [0,0]
        self.health = HEALTH_TROOP
        self.speed = SPEED_TROOP
        self.attack_power = ATTACK_POWER_TROOP
    def build(self,called):
        if(called == 'i'):
            self.pos = [4,1]
            board[4][1] = '*'
            filled[4][1] = 'troop'
        elif(called == 'p'):
            self.pos = [2,23]
            board[2][23] = '*'
            filled[2][23] = 'troop'
        elif(called == 'o'):
            self.pos = [7,WIDTH_BASE - 2]
            board[7][WIDTH_BASE - 2] = '*'
            filled[7][WIDTH_BASE - 2] = 'troop'
        
    def move(self, huts , cannons,list_buildings):
        spd = self.speed
        while spd > 0:
            spd -= 1
            board[self.pos[0]][self.pos[1]] = ' '
            dis = Inf
            for i in list_buildings:
                if i.health > 0:
                    for j in i.lists:
                        if abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1]) < dis:
                            dis = abs(i.pos_x-self.pos[0] + j[0]) + abs(i.pos_y-self.pos[1] + j[1])
                            ind = i
                            indj = [i.pos_x + j[0],i.pos_y + j[1]]
            if dis != Inf:
                if(dis == 1 or (dis == 2 and indj[0] != self.pos[0] and indj[1] != self.pos[1])):
                    ind.health -= self.attack_power
                    os.system('aplay -q ./sounds/king_attack.wav& 2>/dev/null')
                    board[self.pos[0]][self.pos[1]] = '*'
                else:    
                    if(indj[0] < self.pos[0]):
                        self.pos[0] -= 1
                    elif(indj[0] > self.pos[0]):
                        self.pos[0] += 1
                    if (indj[1] < self.pos[1]):
                        self.pos[1] -= 1
                    elif(indj[1] > self.pos[1]):
                        self.pos[1] += 1
                    board[self.pos[0]][self.pos[1]] = '*'
