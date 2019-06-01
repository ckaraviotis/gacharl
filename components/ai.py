import random

"""
Very Stupid AI component
Do something once a turn!
"""
class Ai_Test:
    def __init__(self):
        self.owner = None

    def turn(self, level):
        d = random.randint(-1, 1)
        x = random.randint(0, 1)
        if x == 0:
            self.owner.creature.move(d, 0, level)
        else:
            self.owner.creature.move(0, d, level)

