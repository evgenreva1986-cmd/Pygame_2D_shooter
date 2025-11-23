import pygame
from pygame.sprite import Sprite

class HealthBar(Sprite):
    def __init__(self,bsg_game,object):
        super().__init__()
        self.settings = bsg_game.settings
        self.object = object
        self.screen = bsg_game.screen

        self.back_bar = pygame.Rect(0, 0,
                                self.settings.back_bar_width,
                                self.settings.back_bar_height)
        self.fore_bar = pygame.Rect(0, 0,
                                self.settings.fore_bar_width,
                                self.settings.fore_bar_height)

        self.back_bar.midbottom = self.object.rect.midtop
        self.fore_bar.center = self.back_bar.center

    def update_hp(self):
        self.back_bar.midbottom = self.object.rect.midtop
        self.fore_bar.center = self.back_bar.center

    def draw_hp(self):
        pygame.draw.rect(self.screen, self.settings.back_hp_color, self.back_bar)
        pygame.draw.rect(self.screen, self.settings.fore_hp_color, self.fore_bar)