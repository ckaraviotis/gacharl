import libtcodpy as libtcod
import actors.creatures as creature_factory
import actors.potions as potion_factory

class Tile:
    def __init__(self, passable):
        self.passable = passable
        self.explored = False
        self.sprite = None
        self.sprite_unexplored = None

    def render(self, surface, x, y, visible):
        if self.explored:
            if visible:
                surface.blit(self.sprite, (x, y))
            else:
                surface.blit(self.sprite_unexplored, (x, y))

class Wall(Tile):
    def __init__(self, sprites):
        super().__init__(False)
        self.sprite = sprites.S_WALL
        self.sprite_unexplored = sprites.S_WALL_UNEXPLORED

class Floor(Tile):
    def __init__(self, sprites):
        super().__init__(True)
        self.sprite = sprites.S_FLOOR
        self.sprite_unexplored = sprites.S_FLOOR_UNEXPLORED

class Level:
    def __init__(self, game, width, height):
        self.width = width
        self.height = height
        self.game = game
        self.player = None
        self.npcs = None
        self.game_objects = self.populate()
        self.fov_map = None
        self.generate()

    def is_passable(self, x, y):
        return self.level[x][y].passable

    def is_visible(self, x, y):
        return libtcod.map_is_in_fov(self.fov_map, x, y)

    def get_creature(self, x, y, player):
        for o in self.game_objects:
            if (o is not player and o.x == x and o.y == y and o.creature):
                return o
        return None

    def get_objects(self, x, y):
        """Get a list of all objects on tile x,y"""
        return [o for o in self.game_objects
                    if (o.x == x and o.y == y)]

    def generate(self):
        ''' Generate a map '''
        sprites = self.game.assets.sprites

        new_map = [[Floor(sprites) for y in range(0, self.height)] for x in range(0, self.width)]

        new_map[5][5] = Wall(sprites)
        new_map[5][10] = Wall(sprites)
        new_map[10][5] = Wall(sprites)
        new_map[10][10] = Wall(sprites)

        for x in range(self.width):
            new_map[x][0]  = Wall(sprites)
            new_map[x][self.height-1]  = Wall(sprites)

        for y in range(self.height):
            new_map[0][y] = Wall(sprites)
            new_map[self.width-1][y] = Wall(sprites)

        self.level = new_map
        self.generate_fov()

    def populate(self):
        creatures = creature_factory.CreatureFactory(self)
        potions = potion_factory.PotionFactory(self)

        # Create player
        player = creatures.player(1, 1)

        # Create enemy 1
        blode = creatures.blode(10, 4)

        # Create enemy 2
        beano = creatures.beano(15, 8)

        # Create item
        thing = potions.debugItem(3, 3)
        heal_potion = potions.heal_potion(5, 4)

        npcs = [blode, beano]
        items = [thing, heal_potion]

        self.player = player
        self.npcs = npcs
        self.items = items
        return [player] + npcs + items

    def render(self, surface):
        ''' The map rendering method '''
        sprites = self.game.assets.sprites

        for x in range(0, self.width):
            for y in range(0, self.height):
                is_visible = self.is_visible(x, y)

                if is_visible:
                    self.level[x][y].explored = True
                self.level[x][y].render(surface, x * sprites.width, y * sprites.height, is_visible)

        for item in self.items:
            if self.is_visible(item.x, item.y):
                item.render(surface)

        for npc in self.npcs:
            if self.is_visible(npc.x, npc.y):
                npc.render(surface)

        self.player.render(surface)

    def generate_fov(self):
        fov_map = libtcod.map_new(self.width, self.height)

        for y in range(self.height):
            for x in range(self.width):
                passable = self.is_passable(x, y)
                libtcod.map_set_properties(fov_map, x, y, passable, passable)

        self.fov_map = fov_map

    def calculate_fov(self, x, y, radius):
        libtcod.map_compute_fov(self.fov_map, x, y, radius, True, libtcod.FOV_BASIC)