import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        self.screen=screen

        #load ship image and its rect
        self.image=pygame.image.load('images/spaceship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings

        #start each new ship at bottom-center of screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        # movement flags
        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def blitme(self):
        ##Draw its current position
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center

    def center_ship(self):
        self.center=self.screen_rect.centerx