import pygame


class UserStalker:
    def __init__(self,bsg_game):
        self.screen = bsg_game.screen
        self.screen_rect = bsg_game.screen.get_rect()
        self.settings = bsg_game.settings

        self.orig_image  = pygame.image.load("images/stalker.bmp")
        self.image = self.orig_image
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.current_vector = [1,0]
        self.last_vector = [1,0]

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.stalker_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.stalker_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.stalker_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.stalker_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)