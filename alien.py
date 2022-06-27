import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        # Инициализация пришельца
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings


        # загрузка изображения и назначение атрибука rect
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появиться в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной горизонтальной позиции
        self.x = float(self.rect.x)

    def check_edges(self):
        #Проверка достижения края и изменения движения
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        #Перемешение вправо
        self.x += (self.setting.alien_speed * self.setting.fleet_direction)
        self.rect.x = self.x

