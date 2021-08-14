import pygame
#The racoon Vector is free is free licensed and it has been found at Vecteezy.com website https://www.vecteezy.com/

class Racoon:
    def __init__(self, screen):
        """Initialize the racoon and its starting position."""
        self.screen = screen
        # Load the racoon and get its rect.
        self.image = pygame.image.load('images/racoon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        # Start position is the center of the left edge.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.midleft = self.screen_rect.midleft

    def blitme(self):
        """Draw the racoon at its current position"""
        self.screen.blit(self.image, self.rect)
