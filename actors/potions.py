from pprint import pprint
from actor import Actor
from components import Creature, Ai_Test, Death_Test, Container, Item, drop_corpse
from effects import heal

class PotionFactory:
    def __init__(self, level):
        self.sprites = level.game.assets.sprites
        self.log = level.game.log
        self.level = level

    def debugItem(self, x, y):
        sprites = self.sprites
        alive = False
        creature = None
        ai = None
        item = Item(self.level, identified=True)
        container = None
        debugItem = Actor(x, y, sprites.width, sprites.height, sprites.S_DBG_ITEM, 'Debug_Item', self.log, alive, creature, ai, container, item)
        return debugItem

    def heal_potion(self, x, y):
        on_use = heal
        sprites = self.sprites
        alive = False
        creature = None
        ai = None
        item = Item(self.level, 0, 0, 1, on_use)
        container = None

        heal_potion = Actor(x, y, sprites.width, sprites.height, sprites.S_HEAL_POTION, 'Potion of Minor Healing', self.log, alive, creature, ai, container, item)
        return heal_potion