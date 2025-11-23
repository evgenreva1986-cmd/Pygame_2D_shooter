import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,bsg_game,x_direct, y_direct):
        super().__init__()

        self.screen = bsg_game.screen
        self.settings = bsg_game.settings
        self.color = bsg_game.settings.bullet_color

        self.stalker = bsg_game.user_stalker

        self.x_direct = x_direct
        self.y_direct = y_direct
        height = 0
        width = 0
        if self.x_direct != 0:
            height = self.settings.bullet_height_horizontal
            width = self.settings.bullet_width_horizontal
        elif self.y_direct != 0:
            height = self.settings.bullet_height_vertical
            width = self.settings.bullet_width_vertical


        self.rect = pygame.Rect(0, 0,width,height)
        self.rect.midtop = self.stalker.rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        self.x += self.settings.bullet_speed * self.x_direct
        self.y += self.settings.bullet_speed * self.y_direct
        self.rect.y = self.y
        self.rect.x = self.x


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


