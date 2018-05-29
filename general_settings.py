class Settings():
    def __init__(self):
        # ship settings
        self.ship_speed_factor = 3
        self.ship_limit = 3
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 750

        self.bg_color = (230, 230, 230)
        # Bullet settings
        self.bullet_speed_factor = 5.75
        self.bullet_width = 10
        self.bullet_height = 20
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 4.5
        self.fleet_direction = 1