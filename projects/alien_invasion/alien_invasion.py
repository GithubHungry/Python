import pygame
from projects.alien_invasion.settings import Settings
from projects.alien_invasion.ship import Ship
from projects.alien_invasion import game_functions as gf
from pygame.sprite import Group
from projects.alien_invasion.game_stats import GameStats
from projects.alien_invasion.button import Button


def run_game() -> None:
    """Initializing new game"""
    ai_settings = Settings()
    pygame.init()  # Inside settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # Create screen area
    pygame.display.set_caption("Alien Invasion")  # Create window title
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    ship = Ship(screen, ai_settings)  # create ship
    bullets = Group()  # Create group to save bullets
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:  # Game cycle
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship,  aliens, bullets, play_button)


run_game()
