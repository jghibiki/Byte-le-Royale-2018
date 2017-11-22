import pygame

from game.visualizer.spritesheet_functions import SpriteSheet
from game.common.enums import *

class UnitIconSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data, x, y):
        super().__init__()
        
        sprite_sheet = SpriteSheet("game/visualizer/assets/unit_class_icons.png")
        
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
                                            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class KnightIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.knight * 32,
            32, 32
        ], x, y)        
        
        
class BrawlerIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.brawler * 32,
            32, 32
        ], x, y)   
        
class PikemanIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.pikeman * 32,
            32, 32
        ], x, y)
        
class RogueIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.rogue * 32,
            32, 32
        ], x, y)
        
class MagusIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.magus * 32,
            32, 32
        ], x, y)
        
class WizardIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.wizard * 32,
            32, 32
        ], x, y)
        
class SorcererIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.sorcerer * 32,
            32, 32
        ], x, y)
        
class AlchemistIconSprite(UnitIconSprite):
    def __init__(self, x, y):
        UnitIconSprite.__init__(self, [
            0, UnitClass.alchemist * 32,
            32, 32
        ], x, y)
        
class IconBackSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        sprite_sheet = SpriteSheet("game/visualizer/assets/icon_back.png")
        
        self.image = sprite_sheet.get_image(0, 0, 40, 40)
                                            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class MonsterSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, frames, x, y, h, w, animation_speed):
        super().__init__()
        
        self.frames = frames
        self.index = 0
        self.tick_counter = 0
        self.animation_speed = animation_speed
        
        self.h = h
        self.w = w
        
        self.sprite_sheet = SpriteSheet(sprite_sheet_path)
        
        self.image = self.sprite_sheet.get_image( 
                                                self.frames[self.index][0],
                                                self.frames[self.index][1],
                                                self.h,
                                                self.w
                                                )
                                            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        self.tick_counter += 1
        if self.tick_counter % self.animation_speed is 0:
            if self.index < len(self.frames)-1:
                self.index += 1
            else:
                self.index = 0
        self.image = self.sprite_sheet.get_image( 
                                                self.frames[self.index][0],
                                                self.frames[self.index][1],
                                                self.h,
                                                self.w
                                                )
            
            
class BeholderSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/beholder.png", [
            [0, 0],
            [128, 0],
            [0, 128],
            [128, 128]
        ], x, y, 128, 128, 4)
        
class SlimeSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/slime.png", [
            [0, 0],
            [128, 0],
            [256,0],
            [384,0],
            [0, 128],
            [128,128],
            [256,128],
            [384,128],
            [0,256],
            [128,256],
            [256,256],
            [384,256],
            [0,384],
            [128,384],
        ], x, y, 128, 128,2)
        
class MinotaurSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/minotaur.png", [
            [0, 0],
            [128, 0],
            [256,0],
            [384,0],
            [0, 128],
            [128,128],
            [256,128],
            [384,128],
            [0,256],
            [128,256],
            [256,256],
            [384,256],
            [0,384],
            [128,384],
            [256,384],
            [384,384]
        ], x, y, 128, 128,3)
        
class DragonSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/dragon.png", [
            [0, 0],
            [128, 0],
            [256,0],
            [384,0],
            [512,0],
            [0, 128],
            [128,128],
            [256,128],
            [384,128],
            [512,128],
            [0,256],
            [128,256],
            [256,256],
            [384,256],
            [512,256],
            [0,384],
            [128,384],
            [256,384],
            [384,384],
            [512,384],
            [0,512],
            [128,512],
            [256,512]
        ], x, y, 128, 128,5)
        
class WraithSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/wraith.png", [
            [0, 0],
            [128, 0],
            [256,0],
            [384,0],
            [512,0],
            [0, 128],
            [128,128],
            [256,128],
            [384,128],
            [512,128],
            [0,256],
            [128,256],
            [256,256],
            [384,256],
            [512,256],
            [0,384],
            [128,384],
            [256,384],
            [384,384],
            [512,384],
            [0,512],
            [128,512],
            [256,512],
            [384,512],
            [512,512],
            [0,640],
            [128,640],
            [256,640],
            [384,640],
            [512,640]
        ], x, y, 128, 128,5)
        
class WispSprite(MonsterSprite):
    def __init__(self, x, y):
        MonsterSprite.__init__(self, "game/visualizer/assets/wisp.png", [
            [0, 0],
            [128, 0],
            [256,0],
            [384,0],
            [512,0],
            [0, 128],
            [128,128],
            [256,128],
            [384,128],
            [512,128],
            [0,256],
            [128,256],
            [256,256],
            [384,256],
            [512,256],
            [0,384],
            [128,384],
            [256,384],
            [384,384],
            [512,384],
            [0,512],
            [128,512],
            [256,512],
            [384,512]
        ], x, y, 128, 128,3)
        
def get_monster_sprite(monster_type, pos):
    if monster_type is MonsterType.beholder:
        return BeholderSprite(*pos) 
    elif monster_type is MonsterType.slime:
        return SlimeSprite(*pos) 
    elif monster_type is MonsterType.minotaur:
        return MinotaurSprite(*pos) 
    elif monster_type is MonsterType.dragon:
        return DragonSprite(*pos)
    ##elif monster_type is MonsterType.wraith:
    ##    return WraithSprite(*pos)
    elif monster_type is MonsterType.wisp:
        return WispSprite(*pos)