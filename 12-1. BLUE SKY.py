# TRY IT YOURSELF
#  12-1. BLUE SKY:
import sys
import pygame


def run_game():
    """Initialize the game and create a screen object"""
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("The Blue Sky")
    # Set the back ground color RGB.
    bg_color = (176, 224, 230)

    while True:
        """Create The main loop and check for mouse and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        # Return The most recently drawn screen
        pygame.display.flip()


run_game()
