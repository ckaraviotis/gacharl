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

"""
Basic AI that chases a target
"""
class basic_chase:
    def __init__(self):
        self.owner = None

    def turn(self, level):
        monster = self.owner.creature.owner
        player = level.player

        visible = level.is_visible(monster.x, monster.y)

        if visible:
            dx = player.x - monster.x
            dy = player.y - monster.y

            x = 0 if dx == 0 else int(dx / abs(dx))
            y = 0 if dy == 0 else int(dy / abs(dy))

            self.owner.creature.move(x, y, level)

"""
Confuse AI
"""
class ai_confuse:
    def __init__(self, previous_ai, duration, owner, log):
        self.owner = owner
        self.previous_ai = previous_ai
        self.duration = duration
        self.counter = 0
        self.log = log

    def turn(self, level):
        self.counter += 1

        if self.counter >= self.duration:
            self.owner.creature.owner.ai = self.previous_ai
            self.log.add(f'{self.owner.creature.name} is no longer confused', 'info')

        d = random.randint(-1, 1)
        x = random.randint(0, 1)
        if x == 0:
            self.owner.creature.move(d, 0, level)
        else:
            self.owner.creature.move(0, d, level)