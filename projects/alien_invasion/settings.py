class Settings():
    """Class for game settings(bg_color,width_window,height_window)"""

    def __init__(self):
        """Initializing settings function"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_limit = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings which will change."""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # (1) - move right,(-1) -move left
        self.alien_points = 50

    def increase_speed(self):
        """Increment speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

