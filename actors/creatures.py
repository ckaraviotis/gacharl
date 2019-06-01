from pprint import pprint
from actors.actor import Actor
# from components import Creature, Ai_Test, Death_Test, Container, Item, drop_corpse
import components.ai as ais
import components.death_effect as deaths
import components.creatures as creatures
import components.containers as containers
import components.items as items


class CreatureFactory:
    def __init__(self, level):
        self.sprites = level.game.assets.sprites
        self.log = level.game.log
        self.level = level

    def player(self, x, y):
        sprites = self.sprites
        alive = True
        pc = creatures.Creature('Bert', 40)
        container = containers.Container()
        player = Actor(x, y, sprites.width, sprites.height, sprites.S_PLAYER, 'Human', self.log, alive, pc, None, container)

        return player

    def blode(self, x, y):
        sprites = self.sprites
        on_death = deaths.drop_corpse()
        alive = True

        creature = creatures.Creature('Blode', 5, on_death, 3)
        ai = ais.Ai_Test()
        container = None
        item = items.Item(self.level)

        blode = Actor(x, y, sprites.width, sprites.height, sprites.S2_BLODE, 'Slime', self.log, alive, creature, ai, container, item)
        return blode

    def beano(self, x, y):
        sprites = self.sprites
        on_death = deaths.drop_corpse()
        alive = True

        creature = creatures.Creature('Beano', 15, on_death, 3)
        ai = ais.basic_chase()
        container = None
        item = items.Item(self.level)

        beano = Actor(x, y, sprites.width, sprites.height, sprites.S2_BEANO, 'Bean', self.log, alive, creature, ai, container, item)
        return beano
