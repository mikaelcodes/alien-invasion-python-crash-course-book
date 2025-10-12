import sys
import pygame

from bullet import Bullet

def check_keydown_events(ai_settings, screen, ship, bullets, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ai_settings, screen, ship, bullets, event)
            # If the user pressed space, create a new bullet and add it to the bullets group.
            
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
    
            


def update_screen(ai_settings,screen,ship,bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets:
        bullet.draw_bullet()

    # remove bullet when it disappears
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.display.flip()

