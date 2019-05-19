'''
Creature component

Creatures have health, can damage other things and can die.
'''
class Creature:
    def __init__(self, name, hp = 10):
        self.name = name
        self.hp = hp

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
