import random

def take_damage(self, damage):
        """Apply damage to a creature"""
        self.hp -= damage
        self.owner.messages.add(f'{self.name} takes {damage} damage!', 'info')

        if self.hp <= 0:
            if self.on_death:
                self.on_death.trigger()

def random_walk(actor, level):
    d = random.randint(-1, 1)
    x = random.randint(0, 1)
    dx = 0
    dy = 0

    if x == 0:
        dx = d
    else:
        dy = d

    return (dx, dy)

def walk_towards_player(actor, level):
    monster = actor
    player = level.player

    visible = level.is_visible(monster.x, monster.y)

    if visible:
        dx = player.x - monster.x
        dy = player.y - monster.y

        x = 0 if dx == 0 else int(dx / abs(dx))
        y = 0 if dy == 0 else int(dy / abs(dy))

        return (x, y)
    return (0, 0)

"""Move to a given location"""
class Move:
    def __init__(self, dx, dy, actor, level):
        self.x = actor.x + dx
        self.y = actor.y + dy

        passable = level.is_passable(self.x, self.y)
        occupied = not not level.get_creature(self.x, self.y, actor)
        self.passable = passable and not occupied
        self.actor = actor

    def perform(self):
        if self.passable:
            self.actor.x = self.x
            self.actor.y = self.y

"""Attack an opponent"""
class Attack:
    def __init__(self, level, attacker, target, damage):
        self.log = level.game.log
        self.attacker = attacker
        self.target = target
        self.damage = damage

    def perform(self):
        self.log.add(self.attacker.race.name + ' attacks ' + self.target.race.name, 'info')

        self.target.race.hp -= self.damage
        self.log.add(f'{self.target.race.name} takes {self.damage} damage!', 'info')

        # if self.hp <= 0:
        #     if self.on_death:
        #         self.on_death.trigger()