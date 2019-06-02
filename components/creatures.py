from actions import random_walk, Move, Attack, walk_towards_player

"""
Creature component.
Creatures can move, attack and take damage
"""
class Creature:
    def __init__(self, name, hp=10, on_death=None):
        """Constructor"""
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.on_death = on_death
        self.owner = None
        if on_death:
            on_death.owner = self

    def take_damage(self, damage):
        """Apply damage to a creature"""
        self.hp -= damage
        self.owner.messages.add(f'{self.name} takes {damage} damage!', 'info')

        if self.hp <= 0:
            if self.on_death:
                self.on_death.trigger()

    def move(self, dx, dy, level):
        """Attempt to move the Creature, attacking as necessary"""
        dest_x = self.owner.x + dx
        dest_y = self.owner.y + dy

        dest_passable = level.is_passable(dest_x, dest_y)
        tile_occupant = level.get_creature(dest_x, dest_y, self.owner)

        if tile_occupant:
            self.attack(tile_occupant, 5)

        elif dest_passable:
            self.owner.x = dest_x
            self.owner.y = dest_y

    def attack(self, target, damage):
        """Attack target for damage"""
        self.owner.messages.add(self.owner.race.name + ' attacks ' + target.race.name, 'info')
        target.race.take_damage(damage)

"""
Creature component.
Creatures can move, attack and take damage
"""
class Slime:
    def __init__(self, name, level, hp=10, on_death=None):
        """Constructor"""
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.on_death = on_death
        self.owner = None
        self.move = Move
        self.pattern = random_walk
        self.melee = Attack
        self.level = level
        if on_death:
            on_death.owner = self

    def takeTurn(self):
        dx, dy = self.pattern(self.owner, self.level)
        tile_occupant = self.level.get_creature(self.owner.x + dx, self.owner.y + dy, self.owner)

        if tile_occupant:
            return self.melee(self.level, self.owner, tile_occupant, 5)
        else:
            return self.move(dx, dy, self.owner, self.level)