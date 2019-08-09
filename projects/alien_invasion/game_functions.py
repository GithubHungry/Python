import sys
import pygame
from projects.alien_invasion.bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Check keydown events."""
    if event.key == pygame.K_RIGHT:  # If we press right arrow
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # If we press left arrow
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Check keyup events."""
    if event.key == pygame.K_RIGHT:  # If we up right arrow
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # If we up left arrow
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Checkin events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and show new screen."""
    screen.fill(ai_settings.bg_color)  # Filling game area, atr tuple or var only
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # draw new(old) ship, after filling, because we wanna ship on background
    pygame.display.flip()  # This line update screen after each event
