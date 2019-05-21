import constants

class Tile:
    def __init__(self, passable):
        self.passable = passable

class Level:
    def __init__(self, width, height, game_objects):
        self.width = width
        self.height = height
        self.game_objects = game_objects
        self.generate()
    
    def is_passable(self, x, y):
        return self.level[x][y].passable
    
    def get_creature(self, x, y, player):
        for o in self.game_objects:
            if (o is not player and o.x == x and o.y == y and o.creature):
                return o
        return None

    def generate(self):
        ''' Generate a map '''
        new_map = [[Tile(True) for y in range(0, self.height)] for x in range(0, self.width)]

        new_map[10][10].passable = False
        new_map[10][15].passable = False

        for x in range(self.width):
            new_map[x][0].passable = False
            new_map[x][self.height-1].passable = False
        
        for y in range(self.height):
            new_map[0][y].passable = False
            new_map[self.width-1][y].passable = False
        
        self.level = new_map

    def render(self, surface):
        ''' The map rendering method '''
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.level[x][y].passable:
                    # draw floor
                    surface.blit(constants.S_FLOOR, (x * constants.SPRITE_WIDTH, y * constants.SPRITE_HEIGHT))
                else:
                    # draw wall
                    surface.blit(constants.S_WALL, (x * constants.SPRITE_WIDTH, y * constants.SPRITE_HEIGHT))