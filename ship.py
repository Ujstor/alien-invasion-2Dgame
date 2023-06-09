import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #start each new ship at the bottom center of the screan
        self.rect.midbottom = self.screen_rect.midbottom

        #Store decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        #Movment flag
        self.moving_rigt = False
        self.moving_left = False


    def update(self):
        """Update ship's position based on the movment flag"""
        #Update ship's x value, not the rect
        if self.moving_rigt and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at ist current location"""
        self.screen.blit(self.image, self.rect)