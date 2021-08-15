import sys
import pygame


def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
            elif event.key == pygame.K_UP:
                rocket.moving_up = True
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False
            elif event.key == pygame.K_UP:
                rocket.moving_up = False
            elif event.key == pygame.K_DOWN:
                rocket.moving_down = False


def update_screen(ai_settings, screen, rocket):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen each pass through the loop.
    screen.fill(ai_settings.bg_color)
    rocket.blit_me()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
