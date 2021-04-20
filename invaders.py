import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    #initialize game and create a screen object

    pygame.init()
    infropy_settings = Settings()
    screen = pygame.display.set_mode((infropy_settings.screen_width, infropy_settings.screen_height))
    pygame.display.set_caption("invaders from python")

    #create a ship
    ship = Ship(screen)

    #start the main loop to run the game
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(infropy_settings, screen, ship)
run_game()
