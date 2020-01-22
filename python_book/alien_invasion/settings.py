
class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 10
        
        # Ship Settings
        self.ship_limit = 3

        # How Quick the game speeds up
        self.speedup_scale = 1.1
        # how quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleetl direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
       """Increase speed settings."""
       self.ship_speed_factor *= self.speedup_scale
       self.bullet_speed_factor *= self.speedup_scale
       self.alien_speed_factor *= self.speedup_scale
       self.alien_points = int(self.alien_points * self.score_scale) 
       print(self.alien_points)
