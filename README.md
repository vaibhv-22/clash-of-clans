## How to Start the Game:
```python3 game.py```

## How to play:
    press w/a/s/d to up/left/bottom/right resp.

    press 'h' for Heal Spell
    press 'r' for Rage Spell

    press i/o/p for spawing the troops

    press Spacebar for King to attack
    press 'l' for King's Super Power (Area Splash)

    press q to quit


## OOPS Concepts:
    Inheritance:
        I have a Child class of Cannon in the Buildings Class.
    Polymorphism:
        Line 16 of play.py have a function build(objecttype), which is used to build all the buildings in the loop after every changes.
    Encapsulation:
        Other than Wall, I have used classes for all buildings(huts/town hall/hut) with objects in them like hut1,hut2,hut3 and King/Spell is also made in a class.
    Abstraction:
        The King have methods like move() , attack().

### Replay
    The command written below will replay the xth last game.
    x = 1 is for last game
```python3 replay.py x ```

## BONUS -> 
    King's Super Power:
        It will attack a area with radius=2
            .....
            .....
            ..K..
            .....
            .....
        Dots are the area King 'K' can attack


## Feature for bonus marks:
    There is sounds of bullet when the king or troop is near the cannon,
    There is sound of sword when the king attack.




         