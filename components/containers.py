


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