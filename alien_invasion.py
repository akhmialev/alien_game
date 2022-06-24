import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    # для управления поведением игры

    def __init__(self):
    #Создание игрового окна
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption('Kill Aliens')
        self.ship = Ship(self)

    def run(self):
    #Запуск оснвого цикла
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()

