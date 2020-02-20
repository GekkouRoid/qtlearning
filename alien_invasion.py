import sys
import pygame
from settings import Settings


def run_game():
    # initiation
    pygame.init()
    ai_settings = Settings()
    # bg_color = (240, 240, 240)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)

    while True:
        # monitor keyboard & mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # show the screen
        # screen.fill(bg_color)
        pygame.display.flip()


run_game()

