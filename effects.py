"""
Contains triggered effects
"""
import random

def heal(args):
    """Heal a target for a given amount
    args:
        args: A list containing an actor and a value
    """
    target = args[0]
    amount = args[1]

    if target.creature.hp < target.creature.max_hp:
        target.creature.hp += amount
        if target.creature.hp > target.creature.max_hp:
            target.creature.hp = target.creature.max_hp

        target.messages.add(f'{target.creature.name} healed for {amount}', 'info')
        target.messages.add(f'{target.creature.name} has {target.creature.hp} health', 'info')
        return True
    return False

def sunstrike(args):
    """Damage a target with a massive burst of power
    args:
        args[0] a Level
        args[1] a Message Log
        args[2] An (x, y) coordinate
    """
    level = args[0]
    log = args[1]
    coord = args[2]
    damage = random.randint(30, 100)

    objects = level.get_objects(coord[0], coord[1])
    for o in objects:
        if o.creature:
            log.add(f'You call down a beam of solar energy!', 'info')
            o.creature.take_damage(damage)



def lightning(args):
    """Damage a line of targets
    args:
        args: A list containing a level and a line of tiles
    """
    level = args[0]
    log = args[1]
    line = args[2]
    damage = random.randint(10, 30)

    log.add(f'Lightning bursts forth!', 'info')

    for tile in line:
        objects = level.get_objects(tile[0], tile[1])

        for o in objects:
            if o.creature:
                o.creature.take_damage(damage)