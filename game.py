'''
Main Game
'''
import collections
import pygame
import constants
import sprites_dawn as sprites
import level as Level
from actor import Actor
from components import Creature, Ai_Test, Death_Test
import messages as Messages

def render(level, surface, player, npcs, messages):
    ''' The main game rendering method '''
    # Clear the display
    surface.fill(constants.COLOR_DEFAULT_BG)

    level.render(surface)

    for npc in npcs:
        if level.is_visible(npc.x, npc.y):
            npc.render(surface)

    player.render(surface)

    # Update the display
    messages.r2(surface)
    pygame.display.flip()

def game_main_loop(surface, level, player, npcs, messages):
    ''' The main game loop '''
    game_quit = False

    while not game_quit:
        events = pygame.event.get()
        ai_move = False

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.creature.move(0, -1, level)
                    ai_move = True
                if event.key == pygame.K_DOWN:
                    player.creature.move(0, 1, level)
                    ai_move = True
                if event.key == pygame.K_LEFT:
                    player.creature.move(-1, 0, level)
                    ai_move = True
                if event.key == pygame.K_RIGHT:
                    player.creature.move(1, 0, level)
                    ai_move = True
                if event.key == pygame.K_PERIOD:
                    player.creature.move(0, 0, level)
                    ai_move = True
        
        # Handle FOV
        level.calculate_fov(player.x, player.y, 8)

        # Ai Turns
        if ai_move:
            for npc in npcs:
                if npc.ai:
                    npc.ai.turn(level)

        # Render!
        render(level, surface, player, npcs, messages)

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    Game = collections.namedtuple('Game', ['surface', 'level', 'player', 'npcs', 'messages'])
    pygame.init()
    surface = pygame.display.set_mode((constants.MAP_WIDTH * sprites.SPRITE_WIDTH, constants.MAP_HEIGHT * sprites.SPRITE_HEIGHT))    
    
    messages = Messages.Log()

    d = Death_Test()
    d2 = Death_Test()
    pc = Creature('Bert', 40)
    ec = Creature('Blob', 5, d)
    ec2 = Creature('Blob B', 15, d2)
    ai = Ai_Test()
    ai2 = Ai_Test()
    player = Actor(1, 1, sprites.S_PLAYER, 'Human', messages, pc)
    enemy = Actor(10, 5, sprites.S_ENEMY, 'Slime', messages, ec, ai)
    enemy2 = Actor(15, 3, sprites.S_ENEMY_2, 'Slime', messages, ec2, ai2)

    npcs = [enemy, enemy2]
    level = Level.Level(constants.MAP_WIDTH, constants.MAP_HEIGHT, [player] + npcs)

    return Game(surface, level, player, npcs, messages)

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME.surface, GAME.level, GAME.player, GAME.npcs, GAME.messages)
