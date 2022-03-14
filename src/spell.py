from .header import *
def Increment_King_Health(king,all_troops):
    king.health = min(100, king.health*2)
    for i in all_troops:
        i.health = min(100, i.health*2)

def Increment_King_Movement(king,all_troops):
    king.speed = min(2, king.speed*2)
    king.attack_power = 2*king.attack_power
    for i in all_troops:
        i.attack_power = 2*i.attack_power
        i.speed = min(2, i.speed*2)

class Spell:
    """Class to cast spells."""

    def __init__(self, name):
        """Initializing class."""
        self.name = name

    def cast(self,king,all_troops):
        """Casting spells."""
        if self.name == 'r':
            Increment_King_Movement(king,all_troops)
            
        elif self.name == 'h':
            Increment_King_Health(king,all_troops)