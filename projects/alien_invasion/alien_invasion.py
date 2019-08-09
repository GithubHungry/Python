import pygame
from projects.alien_invasion.settings import Settings
from projects.alien_invasion.ship import Ship
from projects.alien_invasion import game_functions as gf
from pygame.sprite import Group


def run_game() -> None:
    """Initializing new game"""
    ai_settings = Settings()
    pygame.init()  # Inside settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Create screen area
    pygame.display.set_caption("Alien Invasion")  # Create window title
    ship = Ship(screen, ai_settings)  # create ship
    bullets = Group()  # Create group to save bullets
    while True:  # Game cycle
        gf.check_events(ai_settings, screen, ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship,bullets)


run_game()
