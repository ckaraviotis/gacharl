import random

'''
Creature component

Creatures have health, can damage other things and can die.
'''
class Creature:
    def __init__(self, name, hp = 10, on_death = None):
        self.name = name
        self.hp = hp
        self.on_death = on_death
        if on_death:
            on_death.owner = self
    
    def take_damage(self, damage):
        self.hp -= damage
        print(f'{self.name} takes {damage} damage!')

        if self.hp <= 0:
            if self.on_death:
                self.on_death.trigger()

''' Simple death trigger '''
class Death_Test:
    def trigger(self):
        print(f'{self.owner.name} dies!')
        self.owner.owner.creature = None
        self.owner.owner.ai = None

'''
Very Stupid AI component

Do something once a turn!
'''
class Ai_Test:
    def turn(self, level, game_objects):
        d = random.randint(-1, 1)        
        x = random.randint(0, 1)
        if (x == 0):
            self.owner.move(d, 0, level, game_objects)
        else:
            self.owner.move(0, d, level, game_objects)


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
