import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #init game and create a screen object
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    #make a group to store bullets
    bullets = Group()
    #start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        #remove old bullets
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship, bullets)

run_game()
