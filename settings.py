class Settings():
    def __init__(self):
        """Initializing game settings"""
        #Screen setting
        self.screen_width=1080
        self.screen_height=800
        self.bg_color=(225,225,225)

        #Ship settings
        self.ship_speed_factor=1.5

        #Bullet settings
        self.bullet_height=15
        self.bullet_width=3
        self.bullet_color=(60,60,60)
        self.bullet_speed_factor=3
        self.bullets_allowed=5

        #alien setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #Assume 1 for right and -1 for left

        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        self.alien_points = 50

    def initialize_dynamic_settings(self):
            self.ship_speed_factor = 1.5
            self.bullet_speed_factor = 3
            self.alien_speed_factor = 1
            self.fleet_direction = 1

    def increase_speed(self):
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale