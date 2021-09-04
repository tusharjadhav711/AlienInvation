import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen

        #create bullete at (0,0) And set at Ship top-center location
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y = float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor #Here we are updating only decimal value,
                                    # as rect attributes such as cnterx,y,top etc calculate and store to only integer values.
        self.rect.y=self.y #Here we are updating actual position of bullet

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)