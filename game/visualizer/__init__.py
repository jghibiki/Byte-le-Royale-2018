import pygame, sys 
from pygame.locals import *

from game.visualizer.health_bar import HealthBar
from game.visualizer.spritesheet_functions import SpriteSheet
from game.common.enums import *
from game.visualizer.sprite_sheets import *
from game.common.monster_types import get_monster


pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((1280,720))
pygame.display.set_caption('DnD Visualizer')

bgSurfaceObj = pygame.image.load('game/visualizer/assets/brick_wall.png')
bgSurfaceObj = pygame.transform.scale(bgSurfaceObj,(1280,720))

redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
goldColor = pygame.Color(255,215,0)
blackColor = pygame.Color(0,0,0)
mousex, mousey = 0, 0


fontObj = pygame.font.Font('freesansbold.ttf',20)

def start(verbose):
    team = 'Doodz'
    gold = 1000
    trophies = 50
    
    player1MaxHP = 5000
    player2MaxHP = 5000
    player3MaxHP = 5000
    player4MaxHP = 5000
    player1Name = 'DoodBro'
    player2Name = 'BroDood'
    player3Name = 'BoodDro'
    player4Name = 'Carlos'
    
    monster = get_monster(MonsterType.wisp)
    
    monster.init(1)
    
    
    unit_types = [UnitClass.rogue, UnitClass.knight, UnitClass.pikeman, UnitClass.magus]
    player1HP = HealthBar(94, 544, player1MaxHP)
    player2HP = HealthBar(376, 544, player2MaxHP)
    player3HP = HealthBar(656, 544, player3MaxHP)
    player4HP = HealthBar(940, 544, player4MaxHP)
    monsterHP = HealthBar(530,100,monster.health)
    unit_icon_sprite_group = pygame.sprite.Group()
    icon_back_group = pygame.sprite.Group()
    monster_group = pygame.sprite.Group()
    
    monster_pos = (585,160)
    
    monster_group.add( get_monster_sprite(monster.monster_type, monster_pos) )
    
    
    icon_sprite_positions = [(92,504), (374,504), (654,504), (938,504)]
    icon_sprite_backs = [IconBackSprite(pos[0]-4, pos[1]-4) for pos in icon_sprite_positions]
    icon_back_group.add(icon_sprite_backs)
    icon_sprite_number = 0
    for unit_type in unit_types:
        if unit_type is UnitClass.knight:
            unit_icon_sprite_group.add( KnightIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.brawler:
            unit_icon_sprite_group.add( BrawlerIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.pikeman:
            unit_icon_sprite_group.add( PikemanIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.rogue:
            unit_icon_sprite_group.add( RogueIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.magus:
            unit_icon_sprite_group.add( MagusIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.wizard:
            unit_icon_sprite_group.add( WizardIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.sorcerer:
            unit_icon_sprite_group.add( SorcererIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
        elif unit_type is UnitClass.alchemist:
            unit_icon_sprite_group.add( AlchemistIconSprite(
                *icon_sprite_positions[icon_sprite_number]
            ) ) 
            icon_sprite_number += 1
    
    if(verbose):
        print("Visualizer")
    while True:
        windowSurfaceObj.fill(whiteColor)
        teamSurfaceObj = fontObj.render('Team: {0}'.format(team[0:15]),False,whiteColor)
        goldSurfaceObj = fontObj.render('Gold: {0}'.format(str(gold)),False,whiteColor)
        trophiesSurfaceObj = fontObj.render('Trophies: {0}'.format(str(trophies)),False,whiteColor)
        player1InfoSurface = fontObj.render('{0}'.format(player1Name),False,whiteColor)
        player2InfoSurface = fontObj.render('{0}'.format(player2Name),False,whiteColor)
        player3InfoSurface = fontObj.render('{0}'.format(player3Name),False,whiteColor)
        player4InfoSurface = fontObj.render('{0}'.format(player4Name),False,whiteColor)
        monsterNameSurface = fontObj.render('{0}'.format(monster.name),False,whiteColor)
       
        teamRectObj = teamSurfaceObj.get_rect()
        teamRectObj.topleft = (10,20)
        goldRectObj = goldSurfaceObj.get_rect()
        goldRectObj.topleft = (10,36)
        trophiesRectObj = trophiesSurfaceObj.get_rect()
        trophiesRectObj.topleft = (10,52)
        player1InfoRect = player1InfoSurface.get_rect()
        player1InfoRect.topleft = (128,512)      
        player2InfoRect = player2InfoSurface.get_rect()
        player2InfoRect.topleft = (414,512)
        player3InfoRect = player3InfoSurface.get_rect()
        player3InfoRect.topleft = (694,512)
        player4InfoRect = player4InfoSurface.get_rect()
        player4InfoRect.topleft = (978,512)
        monsterInfoRect = monsterNameSurface.get_rect()
        monsterInfoRect.topleft = (530,70)
        
        windowSurfaceObj.blit(bgSurfaceObj,(0,0))
        windowSurfaceObj.blit(teamSurfaceObj,teamRectObj)
        windowSurfaceObj.blit(goldSurfaceObj,goldRectObj)
        windowSurfaceObj.blit(trophiesSurfaceObj,trophiesRectObj)
        windowSurfaceObj.blit(player1InfoSurface,player1InfoRect)
        windowSurfaceObj.blit(player2InfoSurface,player2InfoRect)
        windowSurfaceObj.blit(player3InfoSurface,player3InfoRect)
        windowSurfaceObj.blit(player4InfoSurface,player4InfoRect)
        windowSurfaceObj.blit(monsterNameSurface,monsterInfoRect)
        
        player1HP.draw(windowSurfaceObj)
        player2HP.draw(windowSurfaceObj)
        player3HP.draw(windowSurfaceObj)
        player4HP.draw(windowSurfaceObj)
        monsterHP.draw(windowSurfaceObj)
        monster_group.draw(windowSurfaceObj)
        
        monster_group.update()
        
        icon_back_group.draw(windowSurfaceObj)
        unit_icon_sprite_group.draw(windowSurfaceObj)
        
        #pixArr = pygame.PixelArray(windowSurfaceObj)
        #for x in range(100,200,4):
        #   for y in range(100,200,4):
        #      pixArr[x][y] = redColor
        #del pixArr
        
        #player1HP.set_current_health(player1HP.current - 10)
        #player1HP = 0
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
               mousex,mousey = event.pos
               if event.button in (1, 2, 3):
                   msg = 'yay'
        pygame.display.update()
        fpsClock.tick(30)
