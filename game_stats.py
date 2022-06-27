class GameStats():
    def __init__(self, ai_game):
        self.setting = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ship_left = self.setting.ship_limit