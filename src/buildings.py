from .header import *
import os
class Buildings:
    TOTAL_BUILDING = 0
    """Class to build buildings."""
    def __init__(self, name, pos_x, pos_y, lists):
        """Initializing class."""
        Buildings.TOTAL_BUILDING += 1
        self.name = name
        # Starting Position of the building (top left corner)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lists = lists
        self.health = 100
        self.power_on = False
        if self.name[0] == 'T':
            self.health = HEALTH_TOWN
        elif self.name == 'h':
            self.health = HEALTH_HUT
        elif self.name == 'C':
            self.health = HEALTH_CANNON
            
    def build(self):
        """Building buildings."""
        if(self.health > 0):
            for i in self.lists:
                board[self.pos_x + i[0]][self.pos_y + i[1]] = i[2]
                filled[self.pos_x + i[0]][self.pos_y + i[1]] = self.name
        else:
            if filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != '' and filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != 'K' and filled[self.pos_x + self.lists[0][0]][self.pos_y + self.lists[0][1]] != '*':
                Buildings.TOTAL_BUILDING -= 1
            for i in self.lists:
                board[self.pos_x + i[0]][self.pos_y + i[1]] = ' '
                filled[self.pos_x + i[0]][self.pos_y + i[1]] = ''

class Cannon(Buildings):
    
    def attack(self,king,king_pos,all_troops):
        """Attacking Troops/King."""
        self.range = RANGE_CANNON
        self.attack_power = ATTACK_POWER_CANNON
        if self.health <= 0:
            self.power_on = False
        elif abs(self.pos_x - king_pos[0]) + abs(self.pos_y - king_pos[1]) <= self.range and king.health > 0:
            king.health -= self.attack_power
            # os.system('aplay -q ./sounds/cannon_shot.wav& 2>/dev/null')
            if king.health <= 0:
                king.health = 0
                board[king_pos[0]][king_pos[1]] = 'D'
                filled[king_pos[0]][king_pos[1]] = ''
                self.power_on = False
            else:
                self.power_on = True
        else:
            self.power_on = False
            for i in all_troops:
                if abs(self.pos_x - i.pos[0]) + abs(self.pos_y - i.pos[1]) <= self.range and i.health > 0:
                    # os.system('aplay -q ./sounds/cannon_shot.wav& 2>/dev/null')
                    i.health -= self.attack_power
                    if i.health <= 0:
                        board[i.pos[0]][i.pos[1]] = ' '
                        filled[i.pos[0]][i.pos[1]] = ''
                        all_troops.remove(i)
                    self.power_on = True
                    break