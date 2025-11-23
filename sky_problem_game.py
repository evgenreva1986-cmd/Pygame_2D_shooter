import pygame
import sys
from stalker_user import UserStalker
from st_settings import Settings
from st_bullet import Bullet
from enemy import Enemy
from health_bar import HealthBar

class BlueSkyGame:
    def __init__(self):
        self.settings = Settings()
        pygame.init()
        self.screen = pygame.display.set_mode(self.settings.screen_scale)
        self.screen_rect = self.screen.get_rect()
        self.background_image = pygame.image.load(self.settings.screen_background)

        pygame.display.set_caption("Testik")

        self.user_stalker = UserStalker(self)
        self.bullets = pygame.sprite.Group()
        self.enemys = pygame.sprite.Group()
        self.enemys_bullets = pygame.sprite.Group()
        self.health_bars = pygame.sprite.Group()

    def run_game(self):
        while True:
            self.check_events()
            self._check_loose()
            self.user_stalker.update()
            self.update_bullets()
            self.create_enemy()
            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

    def _check_keydown(self,event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_d:
            self.user_stalker.moving_right = True
            self.user_stalker.current_vector[0] = 1
            self.user_stalker.last_vector = self.user_stalker.current_vector.copy()
            self.user_stalker.image = self.user_stalker.orig_image
        if event.key == pygame.K_a:
            self.user_stalker.moving_left = True
            self.user_stalker.current_vector[0] = -1
            self.user_stalker.last_vector = self.user_stalker.current_vector.copy()
            self.user_stalker.image = pygame.transform.flip(self.user_stalker.orig_image, True, False)
        if event.key == pygame.K_w:
            self.user_stalker.moving_up = True
            self.user_stalker.current_vector[1] = -1
            self.user_stalker.last_vector = self.user_stalker.current_vector.copy()
        if event.key == pygame.K_s:
            self.user_stalker.moving_down = True
            self.user_stalker.current_vector[1] = 1
            self.user_stalker.last_vector = self.user_stalker.current_vector.copy()
        if event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup(self,event):
        if event.key == pygame.K_d:
            self.user_stalker.moving_right = False
            self.user_stalker.current_vector[0] = 0
        if event.key == pygame.K_a:
            self.user_stalker.moving_left = False
            self.user_stalker.current_vector[0] = 0
        if event.key == pygame.K_w:
            self.user_stalker.moving_up = False
            self.user_stalker.current_vector[1] = 0
        if event.key == pygame.K_s:
            self.user_stalker.moving_down = False
            self.user_stalker.current_vector[1] = 0

    def _check_loose(self):
       for enemy in self.enemys.sprites():
            if self.user_stalker.rect.colliderect(enemy.rect):
                sys.exit()

    def fire_bullet(self):
        new_bullet = Bullet(self,
                            *self.user_stalker.last_vector)
        self.bullets.add(new_bullet)

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if (bullet.rect.left > self.screen_rect.right or
                    bullet.rect.right < self.screen_rect.left):
                self.bullets.remove(bullet)
            if (bullet.rect.top < self.screen_rect.top or
                    bullet.rect.bottom > self.screen_rect.bottom):
                self.bullets.remove(bullet)
        collissions = pygame.sprite.groupcollide(self.bullets, self.enemys,
                                             True, True)
        if collissions:
            for health_bar in self.health_bars.sprites():
                self.health_bars.remove(health_bar)
        """зарефачить метод/створити метод перевірку зіткнень і т.д."""


    def create_enemy(self):
        if len(self.enemys.sprites()) < 1:
            enemy = Enemy(self)
            self.enemys.add(enemy)
            self.create_hp(enemy)

        for enemy in self.enemys.sprites():
            if self.user_stalker.current_vector[0] == 1:
                enemy.image = pygame.transform.flip(enemy.orig_image,True,False)
            if self.user_stalker.current_vector[0] == -1:
                enemy.image = enemy.orig_image

    def create_hp(self, object):
        health_bar = HealthBar(self, object)
        self.health_bars.add(health_bar)


    def update_screen(self):
        self.screen.blit(self.background_image,(0,0))
        self.user_stalker.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.enemys.draw(self.screen)
        self.enemys.update()

        for health_bar in self.health_bars.sprites():
            health_bar.draw_hp()
            health_bar.update_hp()

        pygame.display.flip()

if __name__ == "__main__":
    bsg = BlueSkyGame()
    bsg.run_game()