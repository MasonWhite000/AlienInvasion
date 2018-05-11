import sys
import pygame
from general_settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()

    ai_settings = Settings()
    """ Screen settings and such"""
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)
    """backround screen color; grey"""

    ship = Ship(ai_settings, screen)

    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
