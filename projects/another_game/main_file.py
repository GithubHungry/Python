import pygame
from projects.another_game.settings import Settings


def run_game():
    vr_settings = Settings()
    pygame.init()
    screen = pygame.display.setmode(vr_settings.window_width, vr_settings.window_height)
    pygame.display.set_captions("Vadims_rogalik")
    while True:
        pass


run_game()
