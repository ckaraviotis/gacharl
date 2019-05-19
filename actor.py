'''An Actor is the base class for all other objects in the game'''
import constants

class Actor:
    def __init__(self, x, y, sprite, name, creature = None):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name

        if creature:
            self.creature = creature
            creature.owner = self

    def render(self, surface):
         # Draw character
        surface.blit(self.sprite, (self.x * constants.SPRITE_WIDTH, self.y * constants.SPRITE_HEIGHT))

    def move(self, dx, dy, level):
        dest_x = self.x + dx
        dest_y = self.y + dy

        if level[dest_x][dest_y].passable == True:
            self.x = dest_x
            self.y = dest_y