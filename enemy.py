import pygame
from pygame.sprite import Sprite
import random
import math

class Enemy(Sprite):
    def __init__(self, bsg_game):
        super().__init__()
        self.screen = bsg_game.screen
        self.settings = bsg_game.settings
        self.stalker = bsg_game.user_stalker

        self.orig_image = pygame.image.load("images/enemy.bmp")
        self.image = self.orig_image
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(200,1000) - self.stalker.rect.x
        self.rect.y = random.randint(200,500) - self.stalker.rect.y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        difference_x = self.stalker.rect.x - self.rect.x
        difference_y = self.stalker.rect.y - self.rect.y
        way= math.sqrt(difference_x**2 + difference_y**2)

        one_x = difference_x / (way + 0.5)
        one_y = difference_y / (way + 0.5)
        self.x += one_x
        self.y += one_y

        self.rect.x = self.x
        self.rect.y = self.y





