from sheet import Sheet

class Sprites:
    def __init__(self):
        # Sprites!
        self.source_width = 16
        self.source_height = 16
        self.scale = 3

        self.width = self.source_width * self.scale
        self.height = self.source_height * self.scale

        self.sheets = {}
        self.walls = {}
        self.floors = {}
        self.slimes = {}
        self.players = {}

    def load(self):
        # Sprite Sheets
        self.sheets['player'] = Sheet(self.width, self.height, self.scale, "data/img/Characters/Player")
        self.sheets['slime'] = Sheet(self.width, self.height, self.scale, "data/img/Characters/Slime")
        self.sheets['floor'] = Sheet(self.width, self.height, self.scale, "data/img/Objects/Floor", False)
        self.sheets['wall'] = Sheet(self.width, self.height, self.scale, "data/img/Objects/Wall", False)

        self.walls['marble'] = {
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

        self.walls['granite'] = {
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

        self.walls['slate'] = {
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

        self.walls['obsidian'] = {
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

        # Static sprites
        # Note the array index on the end! REQUIRED! :)
        self.S_FLOOR = self.sheets['floor'].get((1, 10))[0]
        self.S_FLOOR_UNEXPLORED = self.sheets['floor'].get((1, 13))[0]

        self.S_WALL = self.sheets['wall'].get(self.walls['slate']['center'])[0]
        self.S_WALL_UNEXPLORED = self.sheets['wall'].get(self.walls['obsidian']['center'])[0]

        self.S_DBG_ITEM = self.sheets['slime'].get((1, 4))


        # Animated Sprites
        self.S_PLAYER = self.sheets['player'].get((6, 3))
        self.S2_JELLY = self.sheets['slime'].get((0, 1))
        self.S2_SLIME = self.sheets['slime'].get((1, 1))
        self.S2_BEANO = self.sheets['slime'].get((2, 1))
        self.S2_BLODE = self.sheets['slime'].get((0, 2))
        self.S2_GAZER = self.sheets['slime'].get((1, 2))
        self.S2_SNAIL = self.sheets['slime'].get((2, 2))
        self.S2_POKEA = self.sheets['slime'].get((1, 3))
        self.S2_POKEB = self.sheets['slime'].get((2, 3))
        self.S2_POKEC = self.sheets['slime'].get((3, 3))
        self.S2_SPLAT = self.sheets['slime'].get((0, 4))
        self.S2_SPLET = self.sheets['slime'].get((1, 4))
