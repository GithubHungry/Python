import pygame


class Ship():
    """Class ship"""

    def __init__(self, screen, ai_settings):  # screen - obj on which will print ship
        """Initializing ship and his start coordinates"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')  # loading image of a ship, return area(ship)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()  # create rectangle for ship
        self.screen_rect = screen.get_rect()  # create window-rectangle
        self.rect.centerx = self.screen_rect.centerx  # put middle of ship to the middle of window
        self.rect.bottom = self.screen_rect.bottom  # put bottom side of ship on the bottom side of window
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)  # print ship on it`s start position

    def update(self):
        """Update ship position depending on the `moving_right and moving_left`."""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # while we press key, ship will move
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # while we press key, ship will move
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """Put ship in the screen center."""
        self.center = self.screen_rect.centerx
