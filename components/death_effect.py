
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