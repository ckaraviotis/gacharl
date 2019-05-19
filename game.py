'''
Main Game
'''

import collections
import pygame
import libtcodpy as libtcod
import constants
from tile import Tile
from actor import Actor

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



def render(level, surface, player):
    ''' The main game rendering method '''
    # Clear the display
    surface.fill(constants.COLOR_DEFAULT_BG)

    render_level(level, surface)
    player.render(surface)

    # Update the display
    pygame.display.flip()

def game_main_loop(surface, level, player):
    ''' The main game loop '''
    game_quit = False
    while not game_quit:
        events = pygame.event.get()

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(0, -1, level)
                if event.key == pygame.K_DOWN:
                    player.move(0, 1, level)
                if event.key == pygame.K_LEFT:
                    player.move(-1, 0, level)
                if event.key == pygame.K_RIGHT:
                    player.move(1, 0, level)
        
        # Render!
        render(level, surface, player)

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    Game = collections.namedtuple('Game', ['surface', 'level', 'player'])
    pygame.init()
    surface = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    level = create_map()

    player = Actor(0, 0, constants.S_PLAYER)

    return Game(surface, level, player)

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME.surface, GAME.level, GAME.player)
