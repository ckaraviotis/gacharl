'''
Main Game
'''
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
    return Game.Game()

if __name__ == '__main__':
    game = game_init()
    game_main_loop(game)
