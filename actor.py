'''An Actor is the base class for all other objects in the game'''
import constants

class Actor:
    def __init__(self, x, y, sprite, name, creature = None, ai = None):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.creature = creature
        self.ai = ai

        if creature:    
            creature.owner = self
        if ai:
            ai.owner = self

    def render(self, surface):
         # Draw character
        surface.blit(self.sprite, (self.x * constants.SPRITE_WIDTH, self.y * constants.SPRITE_HEIGHT))

    def move(self, dx, dy, level, game_objects):
        dest_x = self.x + dx
        dest_y = self.y + dy

        dest_passable = level[dest_x][dest_y].passable == True
        tile_occupant = None

        for o in game_objects:
            if (o is not self and o.x == dest_x and o.y == dest_y and o.creature):
                tile_occupant = o
                break
        
        if tile_occupant:
            print(self.creature.name + ' attacks ' + tile_occupant.creature.name)

        elif dest_passable:
            self.x = dest_x
            self.y = dest_y