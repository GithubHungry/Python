import sys
import pygame
from projects.alien_invasion.bullet import Bullet
from projects.alien_invasion.alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Check keydown events."""
    if event.key == pygame.K_RIGHT:  # If we press right arrow
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # If we press left arrow
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and show new screen."""
    screen.fill(ai_settings.bg_color)  # Filling game area, atr tuple or var only
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()  # draw new(old) ship, after filling, because we wanna ship on background
    aliens.draw(screen)
    pygame.display.flip()  # This line update screen after each event


def update_bullets(bullets):
    """Update bullet position and delete old bullets."""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Create 1 bullet, if there is no max bullets."""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create alien fleet."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """Count number of aliens in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and put it in a row."""
    alien = Alien(ai_settings, screen)
    alien.width = alien.rect.width
    alien.x = alien.width + 2 * alien.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Count number of rows."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, aliens):
    """Update all aliens positions in fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """If alien is on the end of screen."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Move down all fleet and change right to left (or left to right)"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1