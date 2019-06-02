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
            if (o is not player and o.x == x and o.y == y and o.race):
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
        # potions = potion_factory.PotionFactory(self)

        # Create player
        player = creatures.player(1, 1)

        # Create enemy 1
        blode = creatures.blode(10, 4)
        blode2 = creatures.blode(11, 6)
        blode3 = creatures.blode(10, 3)
        blode4 = creatures.blode(14, 5)
        blode5 = creatures.blode(3, 4)

        # Create enemy 2
        # beano = creatures.beano(15, 8)

        # Create item
        # thing = potions.debugItem(3, 3)
        # heal_potion = potions.heal_potion(5, 4)

        #npcs = [blode, beano]
        npcs = [blode, blode2, blode3, blode4, blode5]
        # items = [thing, heal_potion]
        items = []

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

    def get_line(self, origin, destination, bypassWalls = False, ignoreFov = False, limit = None):
        """Return list of all tiles between the two coordinates
        origin: (x, y)
        destination: (x, y)
        bypassWalls: Flag to allow line to pass through walls
        ignoreFov: Flag to allow line to extend out of FOV
        limit: Maximum number of cells to return
        """
        if (origin == destination):
            return [origin]

        libtcod.line_init(origin[0], origin[1], destination[0], destination[1])
        x, y = libtcod.line_step()
        coords = []

        while (not x is None):
            passable = self.is_passable(x,y)
            infov = self.is_visible(x,y)
            validCell = True

            if (x, y) == destination:
                break

            if x < 0 or x > self.width or y < 0 or y > self.height:
                break

            if not ignoreFov:
                if not infov:
                    validCell = False

            if not bypassWalls:
                if not passable:
                    validCell = False

            if validCell:
                coords.append((x, y))

            x, y = libtcod.line_step()

        if limit:
            coords = coords[:limit]
        return coords

    def get_line_inclusive(self, origin, destination):
        """Return list of all tiles between the two coordinates. Includes origin and destination.
        origin: (x, y)
        destination: (x, y)
        """
        libtcod.line_init(origin[0], origin[1], destination[0], destination[1])

        coords = []
        x,y = origin

        while (not x is None):
            if x < 0 or x > self.width or y < 0 or y > self.height:
                break
            coords.append((x, y))
            x, y = libtcod.line_step()
        return coords

    def get_square(self, coord, radius):
        """Return list of all tiles in the radius around a coordinate
        coord: (x, y)
        radius: Integer giving the circle radius
        bypassWalls: Flag to allow line to pass through walls
        ignoreFov: Flag to allow line to extend out of FOV
        """

    def get_circle(self, center, radius, bypassWalls = False, ignoreFov = False):
        """Return list of all tiles in the radius around a coordinate
        coord: (x, y)
        radius: Integer giving the circle radius
        bypassWalls: Flag to allow line to pass through walls
        ignoreFov: Flag to allow line to extend out of FOV

        Uses Bresenham's circle algorithm, https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
        using a line to infill the two points
        """
        coords = []
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius

        o1 = (center[0], center[1] + radius)
        o2 = (center[0], center[1] - radius)
        oo = self.get_line_inclusive(o1, o2)

        o3 = (center[0] + radius, center[1])
        o4 = (center[0] - radius, center[1])
        oa = self.get_line_inclusive(o3, o4)

        coords = oo + oa

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x

            ca = (center[0] + x, center[1] + y)
            cb = (center[0] - x, center[1] + y)
            cal = self.get_line_inclusive(ca, cb)

            cc = (center[0] + x, center[1] - y)
            cd = (center[0] - x, center[1] - y)
            ccl = self.get_line_inclusive(cc, cd)

            ce = (center[0] + y, center[1] + x)
            cf = (center[0] - y, center[1] + x)
            cel = self.get_line_inclusive(ce, cf)

            cg = (center[0] + y, center[1] - x)
            ch = (center[0] - y, center[1] - x)
            cgl = self.get_line_inclusive(cg, ch)

            candidates = cal + ccl + cel + cgl

            for coord in candidates:
                coords.append(coord)

        validCoords = []
        for coord in coords:
            exists = True
            valid = True
            x, y = coord

            if x < 0 or x > (self.width - 1) or y < 0 or y > (self.height - 1):
                valid = False
                exists = False

            if not bypassWalls and exists:
                if not self.is_passable(coord[0], coord[1]):
                    valid = False

            if not ignoreFov and exists:
                if not self.is_visible(coord[0], coord[1]):
                    valid = False

            if valid:
                validCoords.append(coord)


        validCoords
        return list(set(validCoords))

    def get_hollow_circle(self, center, radius):
        """Return list of all tiles in the radius around a coordinate
        coord: (x, y)
        radius: Integer giving the circle radius
        bypassWalls: Flag to allow line to pass through walls
        ignoreFov: Flag to allow line to extend out of FOV

        Uses Bresenham's circle algorithm, https://en.wikipedia.org/wiki/Midpoint_circle_algorithm
        """
        coords = []
        f = 1 - radius
        ddf_x = 1
        ddf_y = -2 * radius
        x = 0
        y = radius

        o1 = (center[0], center[1] + radius)
        o2 = (center[0], center[1] - radius)
        o3 = (center[0] + radius, center[1])
        o4 = (center[0] - radius, center[1])

        coords = [o1, o2, o3, o4]

        while x < y:
            if f >= 0:
                y -= 1
                ddf_y += 2
                f += ddf_y
            x += 1
            ddf_x += 2
            f += ddf_x

            ca = (center[0] + x, center[1] + y)
            cb = (center[0] - x, center[1] + y)
            cc = (center[0] + x, center[1] - y)
            cd = (center[0] - x, center[1] - y)
            ce = (center[0] + y, center[1] + x)
            cf = (center[0] - y, center[1] + x)
            cg = (center[0] + y, center[1] - x)
            ch = (center[0] - y, center[1] - x)

            candidates = [ca, cb, cc, cd, ce, cf, cg, ch]

            for coord in candidates:
                coords.append(coord)


        return list(set(coords))
