import pygame


class Ship():
    """Class ship"""

    def __init__(self, screen):  # screen - obj on which will print ship
        """Initializing ship and his start coordinates"""
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')  # loading image of a ship, return area(ship)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()  # create rectangle for ship
        self.screen_rect = screen.get_rect()  # create window-rectangle
        self.rect.centerx = self.screen_rect.centerx  # put middle of ship to the middle of window
        self.rect.bottom = self.screen_rect.bottom  # put bottom side of ship on the bottom side of window

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)  # print ship on it`s start position
