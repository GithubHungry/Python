import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class with model of an alien."""

    def __init__(self, ai_setting, screen):
        """Initializing an alien and his position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_setting
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Print an alien in position."""
        self.screen.blit(self.image, self.rect)
