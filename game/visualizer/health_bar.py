import math

import pygame

class HealthBar:

    def __init__(self, x, y, max_hp):
        self.x = x
        self.y = y
        self.max = max_hp
        self.current = max_hp
        self.font_obj = pygame.font.Font('freesansbold.ttf',20)

    
    def draw(self, parent_surf):
        parent_surf.fill(pygame.Color("#FFFFFF"),(self.x, self.y, 252, 18))
        parent_surf.fill(pygame.Color("#000000"),(self.x+1, self.y+1, 250, 16))
        parent_surf.fill(pygame.Color(0,255,0),(self.x+1, self.y+1, math.floor((self.current/float(self.max))*250), 16))
        parent_surf.fill(pygame.Color("#696969"), (self.x, self.y+18, 100, 28))
        self.text_surf = self.font_obj.render('HP: {0}'.format(str(self.current)),False,pygame.Color("#2a2b2b"))
        text_rect = self.text_surf.get_rect()
        text_rect.topleft = (self.x+4, self.y+25)
        parent_surf.blit(self.text_surf, text_rect)
        
    def set_current_health(self, current_health):
        self.current = current_health