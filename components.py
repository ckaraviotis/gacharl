import random

'''
Creature component

Creatures have health, can damage other things and can die.
'''
class Creature:
    def __init__(self, name, hp = 10):
        self.name = name
        self.hp = hp

'''
Very Stupid AI component

Do something once a turn!
'''
class Ai_Test:
    def turn(self, level):
        d = random.randint(-1, 1)        
        x = random.randint(0, 1)
        if (x == 0):
            self.owner.move(d, 0, level)
        else:
            self.owner.move(0, d, level)


'''
Container component

TODO: Implement this!
'''
class Container:
    def __init__(self, passable):
        self.passable = passable

'''
Item component

TODO: Implement this!
'''
class Item:
    def __init__(self, passable):
        self.passable = passable
