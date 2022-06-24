import pygame

class Ship():
    def __init__(self, ai_game):
        # Иницилизирует корабль и задает его наччальную позицию
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #загружает изображения корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship1.bmp')
        self.rect = self.image.get_rect()

        #каждый новый корабль появляеться у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)