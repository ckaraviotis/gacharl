'''
Main Game
'''
import collections
import pygame
import libtcodpy as libtcod
import constants
import level
from actor import Actor
from components import Creature, Ai_Test, Death_Test

def render(level, surface, player, npcs):
    ''' The main game rendering method '''
    # Clear the display
    surface.fill(constants.COLOR_DEFAULT_BG)

    level.render(surface)

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
                    player.creature.move(0, -1, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_DOWN:
                    player.creature.move(0, 1, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_LEFT:
                    player.creature.move(-1, 0, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_RIGHT:
                    player.creature.move(1, 0, level, game_objects)
                    ai_move = True
                if event.key == pygame.K_PERIOD:
                    player.creature.move(0, 0, level, game_objects)
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

    d = Death_Test()
    d2 = Death_Test()
    pc = Creature('Bert', 40)
    ec = Creature('Blob', 5, d)
    ec2 = Creature('Blob B', 15, d2)
    ai = Ai_Test()
    ai2 = Ai_Test()
    player = Actor(1, 1, constants.S_PLAYER, 'Human', creature = pc)
    enemy = Actor(10, 5, constants.S_ENEMY, 'Slime', creature = ec, ai = ai)
    enemy2 = Actor(15, 3, constants.S_ENEMY_2, 'Slime', creature = ec2, ai = ai2)

    npcs = [enemy, enemy2]

    lvl = level.Level(constants.MAP_WIDTH, constants.MAP_HEIGHT, [player] + npcs)

    return Game(surface, lvl, player, npcs)

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME.surface, GAME.level, GAME.player, GAME.npcs)
