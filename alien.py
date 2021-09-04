import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        """Initialize alien and its start position"""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load image and set rect
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()

        #start alien at top-left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store alien exact position
        self.x = float(self.rect.x)



    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)#fleet drection will be 1=right -1=left move.
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True