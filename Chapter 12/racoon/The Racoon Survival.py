"""Main module starts here"""
import sys
import pygame
from settings import Settings
from racoon import Racoon


def run_game():
    """Initialize the game and create a screen object"""
    pygame.init()
    rf_settings = Settings()
    screen = pygame.display.set_mode(
        (rf_settings.screen_width, rf_settings.screen_height))
    pygame.display.set_caption("The Racoon Survival")

    # Make a racoon.
    racoon = Racoon(screen)

    while True:
        """Create The main loop and check for mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(rf_settings.bg_color)
        racoon.blitme()
        # Return The most recently drawn screen
        pygame.display.flip()


run_game()

"""Main module ends here"""
