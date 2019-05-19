'''
Main Game
'''

import collections
import pygame
import libtcodpy as libtcod
import constants
from tile import Tile

def create_map():
    ''' Generate a map '''
    new_map = [[Tile(True) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[10][10].passable = False
    new_map[10][15].passable = False
    
    return new_map

def render_level(level, surface):
    ''' The map rendering method '''
    for x in range(0, constants.MAP_WIDTH):
        for y in range(0, constants.MAP_HEIGHT):
            if level[x][y].passable:
                # draw floor
                surface.blit(constants.S_FLOOR, (x * constants.SPRITE_WIDTH, y * constants.SPRITE_HEIGHT))
            else:
                # draw wall
                surface.blit(constants.S_WALL, (x * constants.SPRITE_WIDTH, y * constants.SPRITE_HEIGHT))



def render(level, surface):
    ''' The main game rendering method '''
    # Clear the display
    surface.fill(constants.COLOR_DEFAULT_BG)

    render_level(level, surface)

    # Draw character
    surface.blit(constants.S_PLAYER, (200, 200))

    # Update the display
    pygame.display.flip()

def game_main_loop(surface, level):
    ''' The main game loop '''
    game_quit = False
    while not game_quit:
        events = pygame.event.get()

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                game_quit = True
        
        # Render!
        render(level, surface)

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    Game = collections.namedtuple('Game', ['surface', 'level'])
    pygame.init()
    surface = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    level = create_map()

    return Game(surface, level)

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME.surface, GAME.level)
