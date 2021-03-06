import pygame


class Ship():

    def __init__(self, screen):
        """initialize the ship and its starting position"""
        self.screen = screen
        # Load the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw the ship at assigned position"""
        self.screen.blit(self.image, self.rect)
