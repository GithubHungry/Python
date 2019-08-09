import sys
import pygame


def check_keydown_events(event, ship):
    """Check keydown events."""
    if event.key == pygame.K_RIGHT:  # If we press right arrow
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # If we press left arrow
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Check keyup events."""
    if event.key == pygame.K_RIGHT:  # If we up right arrow
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # If we up left arrow
        ship.moving_left = False


def check_events(ship):
    """Checkin events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and show new screen."""
    screen.fill(ai_settings.bg_color)  # Filling game area, atr tuple or var only
    ship.blitme()  # draw new(old) ship, after filling, because we wanna ship on background
    pygame.display.flip()  # This line update screen after each event
