class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #screan settings
        self.screan_width = 1920
        self.screan_height = 1080
        self.bg_color = (255, 255, 255)

        #Ship speed
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (220, 20, 60)
        self.bullet_allowed = 3
