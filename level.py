import libtcodpy as libtcod
import constants
import sprites_dawn as sprites

class Tile:
    def __init__(self, passable):
        self.passable = passable
        self.explored = False

class Level:
    def __init__(self, width, height, game_objects):
        self.width = width
        self.height = height
        self.game_objects = game_objects
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

    def generate(self):
        ''' Generate a map '''
        new_map = [[Tile(True) for y in range(0, self.height)] for x in range(0, self.width)]

        new_map[5][5].passable = False
        new_map[5][10].passable = False
        new_map[10][5].passable = False
        new_map[10][10].passable = False

        for x in range(self.width):
            new_map[x][0].passable = False
            new_map[x][self.height-1].passable = False
        
        for y in range(self.height):
            new_map[0][y].passable = False
            new_map[self.width-1][y].passable = False
        
        self.level = new_map
        self.generate_fov()

    def render(self, surface):
        ''' The map rendering method '''
        for x in range(0, self.width):
            for y in range(0, self.height):
                is_visible = self.is_visible(x, y)

                if is_visible:
                    self.level[x][y].explored = True
                    if self.level[x][y].passable:
                        # draw floor
                        surface.blit(sprites.S_FLOOR, (x * sprites.SPRITE_WIDTH, y * sprites.SPRITE_HEIGHT))
                    else:
                        # draw wall
                        surface.blit(sprites.S_WALL, (x * sprites.SPRITE_WIDTH, y * sprites.SPRITE_HEIGHT))
                else:
                    if self.level[x][y].explored:
                        if self.level[x][y].passable:
                            # draw floor
                            surface.blit(sprites.S_FLOOR_UNEXPLORED, (x * sprites.SPRITE_WIDTH, y * sprites.SPRITE_HEIGHT))
                        else:
                            # draw wall
                            surface.blit(sprites.S_WALL_UNEXPLORED, (x * sprites.SPRITE_WIDTH, y * sprites.SPRITE_HEIGHT))
    
    def generate_fov(self):
        fov_map = libtcod.map_new(self.width, self.height)

        for y in range(self.height):
            for x in range(self.width):
                passable = self.is_passable(x, y)
                libtcod.map_set_properties(fov_map, x, y, passable, passable)
        
        self.fov_map = fov_map

    def calculate_fov(self, x, y, radius):
        libtcod.map_compute_fov(self.fov_map, x, y, radius, True, libtcod.FOV_BASIC)