
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
        self.owner.messages.add(self.owner.creature.name + ' attacks ' + target.creature.name, 'info')
        target.creature.take_damage(damage)