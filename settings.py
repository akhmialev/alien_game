class Settings():
    def __init__(self):
        #Статические данные
        #настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3

        # настройки для стрельбы
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        #настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 7
        self.fleet_direction = 1


        #Темп ускорение игры
        self.speedup = 1.1
        self.initialize_dynamic_settings()
        #Рост стоимости за перход на следующий уровень
        self.score_scare = 1.5

    # Динамические данные
    def initialize_dynamic_settings(self):
        #Натсройки изменяюшиеся в ходе игры
        self.ship_speed_facotr = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleed_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        #Увеличивет настройки скорости и стоимсоть прешельцев
        self.ship_speed_facotr *= self.speedup
        self.bullet_speed_factor *= self.speedup
        self.alien_speed_factor *= self.speedup

        self.alien_points = int(self.alien_points * self.score_scare)



