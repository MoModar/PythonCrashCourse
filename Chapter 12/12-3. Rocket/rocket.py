import pygame


class Rocket:

    def __init__(self, screen, rg_settings):
        """Initialize the rocket and set its starting position."""
        self.screen = screen
        self.rg_settings = rg_settings
        # Load the rocket image and its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Start each new rocket in the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Store a decimal value for the ship's center.
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket position based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.rg_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center_x -= self.rg_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.rg_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.center_y -= self.rg_settings.rocket_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blit_me(self):
        """Draw the rocket at its current position."""
        self.screen.blit(self.image, self.rect)
