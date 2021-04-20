import pygame

class Ship():

    def __init__(self, screen):
        #initialize our ship and setting starting position
        self.screen = screen

        #load image
        self.image = pygame.image.load("my_enviroments/py3Env/images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #start each new ship at bottom center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom 

        #movement flag
        self.moving_right = False
    
    def update(self):
        #update the ships position on the movement flag
        if self.moving_right:
            self.rect.centerx +=1

    def blitme(self):
        #Draw the ship at its current location
        self.screen.blit(self.image, self.rect)