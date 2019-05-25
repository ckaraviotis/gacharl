"""
This module holds the components which can be attached
to an actor.
"""
import random

"""
Creature component.
Creatures can move, attack and take damage
"""
class Creature:
    def __init__(self, name, hp=10, on_death=None):
        """Constructor"""
        self.name = name
        self.hp = hp
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
        self.owner.messages.add(self.owner.creature.name + ' attacks ' + target.creature.name, 'info')
        target.creature.take_damage(damage)

""" Simple death trigger """
class Death_Test:
    def __init__(self):
        self.owner = None

    def trigger(self):
        creature = self.owner
        creature.owner.messages.add(f'{self.owner.name} dies!', 'info')
        creature.owner.creature = None
        creature.owner.ai = None
        creature.owner.alive = False

""" Simple death trigger """
class drop_corpse:
    def __init__(self):
        self.owner = None

    def trigger(self):
        creature = self.owner
        creature.owner.messages.add(f'{self.owner.name} dies!', 'info')
        creature.owner.creature = None
        creature.owner.ai = None
        creature.owner.alive = False

        # Remove from npcs list and add to items list
        creature.owner.item.level.npcs.remove(creature.owner)
        creature.owner.item.level.items.append(creature.owner)

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
Container component
"""
class Container:
    def __init__(self, volume = 10.0, contents = None):
        self.max_volume = volume
        self.contents = []

        if contents:
            self.contents += contents

    @property
    def volume(self):
        vol = 0
        for i in self.contents:
            vol += i.volume
        return vol

    # TODO: Get item names in inv
    # TODO: Get current volume
    # TODO: Get weight of everything
    # TODO: Take item from inv

    def insert(self, actor):
        """Insert an item into the container"""
        self.contents.append(actor.item)

    def remove(self, actor):
        """Remove an item from the container"""
        # TODO: What if the given item isn't in the container?
        self.contents.remove(actor.item)

"""
Item component
"""
class Item:
    def __init__(self, level, weight = 0.0, volume = 0.0, charges = 1):
        self.weight = weight
        self.volume = volume
        self.charges = charges
        self.owner = None
        self.level = level
        self.container = None

    # Pick up
    def pick_up(self, actor):
        if actor.container:
            if actor.container.volume + self.volume >= actor.container.max_volume:
                actor.messages.add('Could not pick up, overencumbered', 'info')
            else:
                actor.messages.add(f'Picked up {self.owner.name}', 'info')
                actor.container.insert(self.owner)
                self.level.game_objects.remove(self.owner)
                self.level.items.remove(self.owner)
                self.container = actor.container

    # Drop
    def drop(self, x, y):
        self.owner.messages.add(f'Dropped {self.owner.name}', 'info')
        self.owner.x = x
        self.owner.y = y
        self.container.remove(self.owner)
        self.level.game_objects.append(self.owner)
        self.level.items.append(self.owner)
        self.container = None

    # Use
