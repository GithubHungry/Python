import sys
import pygame
from projects.alien_invasion.settings import Settings
from projects.alien_invasion.ship import Ship


def run_game() -> None:
    """Initializing new game"""
    ai_settings = Settings()
    pygame.init()  # Inside settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Create screen area
    pygame.display.set_caption("Alien Invasion")  # Create window title
    ship = Ship(screen)  # create ship
    while True:  # Game cycle
        for event in pygame.event.get():  # This cycle listen events
            if event.type == pygame.QUIT:  # Exit button
                sys.exit()
        screen.fill(ai_settings.bg_color)  # Filling game area, atr tuple or var only
        ship.blitme()  # draw new(old) ship, after filling, because we wanna ship on background
        pygame.display.flip()  # This line update screen after each event


run_game()
