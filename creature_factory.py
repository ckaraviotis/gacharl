from pprint import pprint
from actor import Actor
from components import Creature, Ai_Test, Death_Test, Container, Item, drop_corpse

class CreatureFactory:
    def __init__(self, level):
        self.sprites = level.game.assets.sprites
        self.log = level.game.log
        self.level = level

    def player(self, x, y):
        sprites = self.sprites
        alive = True
        pc = Creature('Bert', 40)
        container = Container()
        player = Actor(x, y, sprites.width, sprites.height, sprites.S_PLAYER, 'Human', self.log, alive, pc, None, container)

        return player

    def blode(self, x, y):
        sprites = self.sprites
        on_death = drop_corpse()
        alive = True

        creature = Creature('Blode', 5, on_death)
        ai = Ai_Test()
        container = None
        item = Item(self.level)

        blode = Actor(x, y, sprites.width, sprites.height, sprites.S2_BLODE, 'Slime', self.log, alive, creature, ai, container, item)
        return blode

    def beano(self, x, y):
        sprites = self.sprites
        on_death = Death_Test()
        alive = True

        creature = Creature('Beano', 15, on_death)
        ai = Ai_Test()
        container = None
        item = None

        beano = Actor(x, y, sprites.width, sprites.height, sprites.S2_BEANO, 'Slime', self.log, alive, creature, ai, container, item)
        return beano

    def debugItem(self, x, y):
        sprites = self.sprites
        alive = False
        creature = None
        ai = None
        item = Item(self.level)
        container = None
        debugItem = Actor(x, y, sprites.width, sprites.height, sprites.S_DBG_ITEM, 'Item', self.log, alive, creature, ai, container, item)
        return debugItem