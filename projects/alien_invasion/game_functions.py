import sys
import pygame


def check_events(ship):
    """Checkin events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # If we press key on keyboard
            if event.key == pygame.K_RIGHT:  # If we press right arrow
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:  # If we press left arrow
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and show new screen."""
    screen.fill(ai_settings.bg_color)  # Filling game area, atr tuple or var only
    ship.blitme()  # draw new(old) ship, after filling, because we wanna ship on background
    pygame.display.flip()  # This line update screen after each event
