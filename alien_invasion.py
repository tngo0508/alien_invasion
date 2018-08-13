"""creating a pygame window and responding to user input"""
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    """running the game"""
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop
    while True:
        gf.check_events()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()
