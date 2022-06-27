import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        # Инициализация пришельца
        super().__init__()
        self.screen = ai_game.screen

        # загрузка изображения и назначение атрибука rect
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        #Каждый новый пришелец появиться в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной горизонтальной позиции
        self.x = float(self.rect.x)