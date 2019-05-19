import pygame
import libtcodpy as libtcod
import constants

def draw_game():
    ''' The main game rendering method '''
    global SURFACE_MAIN
    # Clear the display
    SURFACE_MAIN.fill(constants.COLOR_DEFAULT_BG)

    # Draw character
    SURFACE_MAIN.blit(constants.S_PLAYER, (200, 200))

    # Update the display
    pygame.display.flip()

def game_main_loop():
    ''' The main game loop '''
    game_quit = False
    while not game_quit:
        events = pygame.event.get()

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                game_quit = True
        
        # Render!
        draw_game()

    # Quit the game
    pygame.quit()
    exit()

def game_init():
    ''' Initialize the main game window & pygame '''
    global SURFACE_MAIN
    pygame.init()
    SURFACE_MAIN = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))

if __name__ == '__main__':
    game_init()
    game_main_loop()