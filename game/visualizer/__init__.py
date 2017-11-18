import pygame, sys 
from pygame.locals import *

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
    player1HP = 5000
    player1MaxHP = 5000
    player1Name = 'DoodBro'
    
    if(verbose):
        print("Visualizer")
    while True:
        windowSurfaceObj.fill(whiteColor)
        teamSurfaceObj = fontObj.render('Team: {0}'.format(team[0:15]),False,whiteColor)
        goldSurfaceObj = fontObj.render('Gold: {0}'.format(str(gold)),False,goldColor)
        trophiesSurfaceObj = fontObj.render('Trophies: {0}'.format(str(trophies)),False,goldColor)
        player1InfoSurface = fontObj.render('{0}'.format(player1Name),False,whiteColor)
        player1HPSurface = fontObj.render('HP: {0}'.format(str(player1HP)),False,whiteColor)
        
        teamRectObj = teamSurfaceObj.get_rect()
        teamRectObj.topleft = (10,20)
        goldRectObj = goldSurfaceObj.get_rect()
        goldRectObj.topleft = (10,36)
        trophiesRectObj = trophiesSurfaceObj.get_rect()
        trophiesRectObj.topleft = (10,52)
        player1InfoRect = player1InfoSurface.get_rect()
        player1InfoRect.topleft = (100,500)
        player1HPRect = player1HPSurface.get_rect()
        player1HPRect.topleft = (102,544)
        
        windowSurfaceObj.blit(bgSurfaceObj,(0,0))
        windowSurfaceObj.blit(teamSurfaceObj,teamRectObj)
        windowSurfaceObj.blit(goldSurfaceObj,goldRectObj)
        windowSurfaceObj.blit(trophiesSurfaceObj,trophiesRectObj)
        windowSurfaceObj.blit(player1InfoSurface,player1InfoRect)
        
        pygame.draw.rect(windowSurfaceObj,blackColor,(105,524,250,16),0)
        pygame.draw.rect(windowSurfaceObj,greenColor,(105,524,(player1HP/player1MaxHP)*250,16),0)
        pygame.draw.rect(windowSurfaceObj,whiteColor,(104,521,252,18),4)
        windowSurfaceObj.blit(player1HPSurface,player1HPRect)
        
        #pixArr = pygame.PixelArray(windowSurfaceObj)
        #for x in range(100,200,4):
        #   for y in range(100,200,4):
        #      pixArr[x][y] = redColor
        #del pixArr
        
        player1HP = player1HP - 10
        #player1HP = 0
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #elif event.type == MOUSEBUTTONUP:
            #   mousex,mousey = event.pos
            #   if event.button in (1, 2, 3):
            #       trophies -= 5
            #       msg = 'yay'
        pygame.display.update()
        fpsClock.tick(30)
