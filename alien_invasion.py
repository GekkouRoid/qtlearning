import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # initiation
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)
    ship = Ship(screen)

    while True:
        # monitor keyboard & mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # show the screen
        # screen.fill(ai_settings.bg_color)

        ship.blitme()
        pygame.display.flip()


run_game()

