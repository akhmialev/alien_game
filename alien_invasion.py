import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    # для управления поведением игры

    def __init__(self):
    #Создание игрового окна
        pygame.init()
        self.settings = Settings()

        # Оконный режим
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Полноэкранный режим
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Kill Aliens')
        self.ship = Ship(self)

    def run(self):
    #Запуск оснвого цикла
        while True:
            self.check_events()
            self.update_screen()
            self.ship.update()


    def check_events(self):
        # обработка нажатия клавиш и мышки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # проверка нажатие клавиши и перемещение корабля
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_enevts(event)
            # если отпустить <- или -> то корабль перестанет двигаться
            elif event.type == pygame.KEYUP:
                self.check_keyup_enevets(event)

    def check_keydown_enevts(self, event):
        # логоика нажатия клавиш
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_enevets(self, event):
        # логика если отпустить клавишу
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def update_screen(self):
        # Обновляет изображения на экране
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()

