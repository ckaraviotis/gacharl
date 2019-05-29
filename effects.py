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
        args: A list containing an actor with a creature component and a message log
    """
    actor = args[0]
    log = args[1]
    damage = random.randint(30, 100)

    log.add(f'You call down a beam of solar energy!', 'info')

    actor.creature.take_damage(damage)