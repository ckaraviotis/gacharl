"""
Contains triggered effects
"""

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
