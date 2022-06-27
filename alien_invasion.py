import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self):
        #Создание пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Доступное пространство(от ширины экрана отняли двух ширину двух пришельцев для отступов)
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # Количество пришельцев - делим простарвно на удвоенного пришельца(между пришельцами пустое пространство равно
        # пришельцу)
        number_aliens_x = available_space_x // (2 * alien_width)

        #Количество рядов
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #Создание рядов пришельцев
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_aliens(alien_number, row)

    def create_aliens(self, alien_number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        self.aliens.add(alien)


    def run(self):
    #Запуск оснвого цикла
        while True:
            self.check_events()
            self.update_screen()
            self.update_bullet()
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
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def check_keyup_enevets(self, event):
        # логика если отпустить клавишу
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def fire_bullet(self):
        #создание пули
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def update_bullet(self):
        #Обновление позиции пули
        self.bullets.update()

        # Удаление пуль при достижение верха экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update_screen(self):
        # Обновляет изображения на экране
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run()

