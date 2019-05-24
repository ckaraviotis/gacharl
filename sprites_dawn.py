from sheet import Sheet

class Sprites:
    def __init__(self):
        # Sprites!
        self.SOURCE_WIDTH = 16
        self.SOURCE_HEIGHT = 16
        self.SCALE_MULT = 3

        self.SPRITE_WIDTH = self.SOURCE_WIDTH * self.SCALE_MULT
        self.SPRITE_HEIGHT = self.SOURCE_HEIGHT * self.SCALE_MULT

    def load(self):
        # Sprite Sheets
        self.PLAYERS = Sheet(self.SPRITE_WIDTH, self.SPRITE_HEIGHT, self.SCALE_MULT, "data/img/Characters/Player")
        self.SLIMES = Sheet(self.SPRITE_WIDTH, self.SPRITE_HEIGHT, self.SCALE_MULT, "data/img/Characters/Slime")
        self.FLOOR = Sheet(self.SPRITE_WIDTH, self.SPRITE_HEIGHT, self.SCALE_MULT, "data/img/Objects/Floor", False)
        self.WALL = Sheet(self.SPRITE_WIDTH, self.SPRITE_HEIGHT, self.SCALE_MULT, "data/img/Objects/Wall", False)

        self.MARBLE_WALLS = {
            'northEast': (0, 3),
            'north'    : (1, 3),
            'northWest': (2, 3),
            'west'     : (0, 4),
            'center'   : (1, 4),
            'east'     : (2, 4),
            'southWest': (0, 5),
            'south'    : (1, 5),
            'southEast': (2, 5)
        }

        self.GRANITE_WALLS = {
            'northEast': (0, 6),
            'north'    : (1, 6),
            'northWest': (2, 6),
            'west'     : (0, 7),
            'center'   : (1, 7),
            'east'     : (2, 7),
            'southWest': (0, 8),
            'south'    : (1, 8),
            'southEast': (2, 8)
        }

        self.SLATE_WALLS = {
            'northEast': (0, 9),
            'north'    : (1, 9),
            'northWest': (2, 9),
            'west'     : (0, 10),
            'center'   : (1, 10),
            'east'     : (2, 10),
            'southWest': (0, 11),
            'south'    : (1, 11),
            'southEast': (2, 11)
        }

        self.OBSIDIAN_WALLS = {
            'northEast': (0, 12),
            'north'    : (1, 12),
            'northWest': (2, 12),
            'west'     : (0, 13),
            'center'   : (1, 13),
            'east'     : (2, 13),
            'southWest': (0, 14),
            'south'    : (1, 14),
            'southEast': (2, 14)
        }

        # Individual sprites
        self.S_PLAYER = self.PLAYERS.get((0, 0))
        self.S_FLOOR = self.FLOOR.get((1, 10))
        self.S_FLOOR_UNEXPLORED = self.FLOOR.get((1, 1))

        self.S_WALL = self.WALL.get(self.SLATE_WALLS['center'])
        self.S_WALL_UNEXPLORED = self.WALL.get(self.OBSIDIAN_WALLS['center'])

        # New sprites test
        self.S2_JELLY = self.SLIMES.get((0, 1))
        self.S2_SLIME = self.SLIMES.get((1, 1))
        self.S2_BEANO = self.SLIMES.get((2, 1))
        self.S2_BLODE = self.SLIMES.get((0, 2))
        self.S2_GAZER = self.SLIMES.get((1, 2))
        self.S2_SNAIL = self.SLIMES.get((2, 2))
        self.S2_POKEA = self.SLIMES.get((1, 3))
        self.S2_POKEB = self.SLIMES.get((2, 3))
        self.S2_POKEC = self.SLIMES.get((3, 3))
        self.S2_SPLAT = self.SLIMES.get((0, 4))
        self.S2_SPLET = self.SLIMES.get((1, 4))
