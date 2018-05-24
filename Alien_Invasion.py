import pygame
from pygame.sprite import Group

import game_functions as gf
from general_settings import Settings
from ship import Ship
import alien


def run_game():
    pygame.init()

    ai_settings = Settings()

    """ Screen settings and such"""
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)
    """background screen color; grey"""

    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))


run_game()
