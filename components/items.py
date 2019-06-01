


"""
Item component
"""
class Item:
    def __init__(self, level, weight = 0.0, volume = 0.0, charges = 1, on_use = None, identified = False):
        self.weight = weight
        self.volume = volume
        self.charges = charges
        self.owner = None
        self.level = level
        self.container = None
        self.on_use = on_use
        self.identified = identified

    @property
    def name(self):
        if self.identified:
            return self.owner.name
        return 'Unknown item'

    # Pick up
    def pick_up(self, actor):
        if actor.container:
            if actor.container.volume + self.volume >= actor.container.max_volume:
                actor.messages.add('Could not pick up, overencumbered', 'info')
            else:
                actor.messages.add(f'Picked up {self.name}', 'info')
                actor.container.insert(self.owner)
                self.level.game_objects.remove(self.owner)
                self.level.items.remove(self.owner)
                self.container = actor.container

    # Drop
    def drop(self, x, y):
        self.owner.messages.add(f'Dropped {self.name}', 'info')
        self.owner.x = x
        self.owner.y = y
        self.container.remove(self.owner)
        self.level.game_objects.append(self.owner)
        self.level.items.append(self.owner)
        self.container = None

    # Use
    def use(self, args):
        if self.on_use:
            if self.charges > 0:
                success = self.on_use(args)

                if success:
                    self.owner.messages.add(f'Activated {self.name}', 'info')
                    self.charges -= 1
                    if self.charges == 0:
                        self.destroy()
                else:
                    self.owner.messages.add(f'Nothing seems to happen...')

    def destroy(self):
        self.container.remove(self.owner)
        self.container = None
        self.owner = None
