import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf


def run_game():
    """Initialize pygame, settings and create screen object."""
    pygame.init()
    rg_settings = Settings()
    screen = pygame.display.set_mode(
        (rg_settings.screen_width, rg_settings.screen_height))
    pygame.display.set_caption("The Rocket")

    # Make a rocket.
    rocket = Rocket(screen, rg_settings)

    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(rg_settings, screen, rocket)


run_game()
