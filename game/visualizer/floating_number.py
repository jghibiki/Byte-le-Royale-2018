import math 

import pygame

class FloatingNumber(pygame.sprite.Sprite):
    def __init__(self, x, y, value, color):
        super().__init__()
        self.font_obj = pygame.font.Font('freesansbold.ttf',20)
        self.value = value
        self.color = color
        self.image = self.font_obj.render(self.value, True, self.color)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.counter = 20
        self.y = y
        
    def update(self, group):
        if self.counter > 0:
            y = ((((self.counter * 0.75)-10) ** 2) + 2 * (self.counter * 0.75) + 0) * 0.25
            self.rect.topleft = (self.rect.x+1, y+self.y)
        else:
            if self in group.sprites():
                group.remove(self)
                
        self.counter -= 1