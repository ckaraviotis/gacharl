'''
Main Game
'''
# pylint: disable=no-member
import pygame
import game as Game

def game_main_loop(game):
    ''' The main game loop '''
    game_quit = False

    while not game_quit:
        game_quit = game.update()

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    pygame.init()
    pygame.key.set_repeat(200, 75)
    return Game.Game()

if __name__ == '__main__':
    GAME = game_init()
    game_main_loop(GAME)
