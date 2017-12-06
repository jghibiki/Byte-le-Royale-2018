import math

import pygame

class HealthBar(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, unit_id):
        super().__init__()
        self.unit_id = unit_id
        self.max = 0
        self.current = 0
        self.font_obj = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf', 12)

        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.Surface((w, h), pygame.SRCALPHA)

    def update(self, units):

        unit = self.get_unit(units)

        if unit is None: # couldn't find a valid unit
            return

        updates = False

        if unit.health is not self.max:
            self.max = unit.health
            updates = True

        if unit.current_health is not self.current:
            self.current = unit.current_health
            updates = True

        if updates:

            # render text
            self.text_surf = self.font_obj.render('HP:{0}'.format(
                str(self.current).rjust(6, "0")), True, pygame.Color("#2a2b2b"))

            text_rect = self.text_surf.get_rect()

            #Choose where to draw the amount of HP left
            text_rect.topleft = (4, 3)
            self.image.fill(pygame.Color("#DEDEDE"), (0, 1, 300, 20))
            self.image.blit(self.text_surf, text_rect)

            #Draw health bars
            self.image.fill(pygame.Color("#FFFFFF"),(96, 2, 202, 18))
            self.image.fill(pygame.Color("#FF0000"),(97, 3, 200, 16))
            self.image.fill(pygame.Color("#33BF00"),(97, 3, math.floor((self.current/float(self.max))*200), 16))


    def get_unit(self, units):
        for unit in units:
            if unit.id == self.unit_id:
                return unit
        return None
