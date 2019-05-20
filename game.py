'''
Main Game
'''

import collections
import pygame
import libtcodpy as libtcod
import constants
from tile import Tile
from actor import Actor
from components import Creature, Ai_Test

def create_map():
    ''' Generate a map '''
    new_map = [[Tile(True) for y in range(0, constants.MAP_HEIGHT)] for x in range(0, constants.MAP_WIDTH)]

    new_map[10][10].passable = False
    new_map[10][15].passable = False

    for x in range(constants.MAP_WIDTH):
        new_map[x][0].passable = False
        new_map[x][constants.MAP_HEIGHT-1].passable = False
    
    for y in range(constants.MAP_HEIGHT):
        new_map[0][y].passable = False
        new_map[constants.MAP_WIDTH-1][y].passable = False
    
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



def render(level, surface, player, npcs):
    ''' The main game rendering method '''
    # Clear the display
    surface.fill(constants.COLOR_DEFAULT_BG)

    render_level(level, surface)

    for npc in npcs:
        npc.render(surface)

    player.render(surface)

    # Update the display
    pygame.display.flip()

def game_main_loop(surface, level, player, npcs):
    ''' The main game loop '''
    game_quit = False
    game_objects = [player] + npcs

    while not game_quit:
        events = pygame.event.get()
        ai_move = False

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move(0, -1, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_DOWN:
                    player.move(0, 1, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_LEFT:
                    player.move(-1, 0, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_RIGHT:
                    player.move(1, 0, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_PERIOD:
                    player.move(0, 0, level, game_objects)
                    ai_move = True
        
        # Ai Turns
        if ai_move:
            for npc in npcs:
                if npc.ai:
                    npc.ai.turn(level, game_objects)

        # Render!
        render(level, surface, player, npcs)

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    Game = collections.namedtuple('Game', ['surface', 'level', 'player', 'npcs'])
    pygame.init()
    surface = pygame.display.set_mode((constants.MAP_WIDTH * constants.SPRITE_WIDTH, constants.MAP_HEIGHT * constants.SPRITE_HEIGHT))
    level = create_map()

    pc = Creature('Bert')
    ec = Creature('Blob')
    ai = Ai_Test()
    ai2 = Ai_Test()
    player = Actor(1, 1, constants.S_PLAYER, 'Human', creature = pc)
    enemy = Actor(10, 5, constants.S_ENEMY, 'Slime', creature = ec, ai = ai)
    enemy2 = Actor(15, 3, constants.S_ENEMY_2, 'Slime', creature = ec, ai = ai2)

    npcs = [enemy, enemy2]

    return Game(surface, level, player, npcs)

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME.surface, GAME.level, GAME.player, GAME.npcs)
