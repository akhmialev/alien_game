import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        # Иницилизирует корабль и задает его наччальную позицию
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        #загружает изображения корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()

        #каждый новый корабль появляеться у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #Сохранение вещественной коориданты
        self.x = float(self.rect.x)

        # флаг для не прервного перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # обновляет позицию корабля с учетом флага
        # обновлять будем атрибут x

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # обновляем атрибут rect
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)