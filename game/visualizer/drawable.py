import pygame

class Drawable:

    def __init__(self, height=None, width=None, path=None):
        if path != None:
            self.surf = pygame.image.load(path)
        elif height != None and width != None:
            self.surf = pygame.Surface((width, height), pygame.SRCALPHA)
        else:
            raise Exception("Invalid Drawable Initialization - Missing height and width or path.")
    
        self.dirty = 1
        
    def update(self):
        raise Exception("Drawable.update not implemented.")
        
    def render(self):
        raise Exception("Drawable.render not implemented.")
        
    def _draw(self, parent_surf):
        if self.dirty in [1, 2]:
            if self.dirty is 1:
                self.dirty = 0
            self.draw(parent_surf)
        
    def draw(self, parent_surf):
        raise Exception("Drawable.draw not implemented.")