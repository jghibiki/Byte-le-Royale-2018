import sys, math, random

import pygame
from pygame.locals import *

from game.common.enums import *
from game.common.monster_types import get_monster

from game.visualizer.health_bar import HealthBar
from game.visualizer.spritesheet_functions import SpriteSheet
from game.visualizer.sprite_sheets import *
from game.visualizer.game_log_parser import GameLogParser
from game.visualizer.floating_number import FloatingNumber


def party_killed_screen(global_surf, fps_clock, data):
    big_font = pygame.font.Font('game/visualizer/assets/manaspc.ttf',70)
    little_font = pygame.font.Font('game/visualizer/assets/manaspc.ttf',20)

    you_have_died = big_font.render("Game Over", True, pygame.Color("#FFFFFF"))


    while True:
        global_surf.fill(pygame.Color("#000000"))

        width = math.floor(1280/2.0)

        # center and print game over
        rect = you_have_died.get_rect()
        pos = ( width-math.floor(rect.w/2), 200)
        global_surf.blit(you_have_died, pos)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()


        pygame.display.update()
        fps_clock.tick(60)



def start(verbose):

    if len(sys.argv) == 3:
        log_path = sys.argv[2]
    else:
        log_path = "./game_log"

    log_parser = GameLogParser(log_path)
    units, events = log_parser.get_turn()

    # assign unit colors
    unit_colors = {}
    colors = [
        pygame.Color("#05AFE8"),
        pygame.Color("#AF05E8"),
        pygame.Color("#E83E05"),
        pygame.Color("#3EE805")
    ]
    for unit in units:
        unit_colors[unit.id] = colors.pop()
    del colors

    location = None # current location

    pygame.init()
    fpsClock = pygame.time.Clock()

    global_surf = pygame.display.set_mode((1280,720))
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


    fontObj = pygame.font.Font('game/visualizer/assets/manaspc.ttf',20)

    team = 'Doodz'
    gold = 300
    trophies = 0

    monster = None

    unit_hp_bars = pygame.sprite.Group()

    unit_hp_bar_pos = [(20, 544), (332, 544), (644, 544), (956, 544)]

    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id) )

    unit_damage_number_pos = {}

    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_damage_number_pos[ units[idx].id ] = ( pos[0]+20, pos[1]-80 )

    unit_damage_animation_pos = {}
    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_damage_animation_pos[ units[idx].id ] = (pos[0], pos[1]- 200)

    monster_hp_bar = pygame.sprite.Group()
    monster_name_surface = None

    floating_number_group = pygame.sprite.Group()
    attack_animation_group = pygame.sprite.Group()
    unit_icon_sprite_group = pygame.sprite.Group()
    icon_back_group = pygame.sprite.Group()
    monster_group = pygame.sprite.Group()


    monster_pos = (585,120)

    teamSurfaceObj = fontObj.render('Team: {0}'.format(team[0:15]), True, whiteColor)

    icon_sprite_positions = [(20,504), (332,504), (644,504), (956,504)]
    icon_sprite_backs = [IconBackSprite(pos[0]-4, pos[1]-4) for pos in icon_sprite_positions]
    icon_back_group.add(icon_sprite_backs)
    icon_sprite_number = 0
    for unit in units:
        unit_type = unit.unit_class
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

    # load background image sprites
    background_group = pygame.sprite.Group()

    town_shop_sprite = TownShopSprite()
    monster_room_sprite = get_monster_room_sprite()

    if(verbose):
        print("Visualizer")

    first_loop = True
    next_turn_counter = 0
    background = NodeType.town
    attack_counter = 0

    while True:

        # per loop flags
        draw_gold = False
        draw_trophies = False
        location_change = False

        if log_parser.check_finished():
            sys.exit()

        if next_turn_counter <= 0:
            print("Game Turn: " + str(log_parser.tick))
            units, events = log_parser.get_turn()

        # read through the events
        for event in events:
            if not event["handled"]:
                if event["type"] == Event.set_location:

                    if location is not None and location.id != event["location"].id:
                        location_change = True

                    location = event["location"]

                    background = location.node_type

                    next_turn_counter += 5
                    if location.node_type == NodeType.town:
                        next_turn_counter += 5

                    event["handled"] = True

                elif event["type"] == Event.combat_resolved:
                    gold = event["gold"]
                    trophies = event["trophies"]
                    draw_gold = True
                    draw_trophies = True

                    event["handled"] = True

                elif event["type"] == Event.purchase_item:
                    #TODO finish handling event
                    gold = event["gold"]
                    draw_gold = True

                    event["handled"] = True

                elif event["type"] == Event.unit_attack:

                    if attack_counter <= 0:

                        attack_counter = 0
                        next_turn_counter += 0

                        event["handled"] = True

                        color = unit_colors[event["unit"]]

                        fn = FloatingNumber(520 + random.randint(-15, 15) , 10 , '-{}'.format(event["damage"]), color)
                        floating_number_group.add(fn)

                        aa = AttackAnimation(576 + random.randint(-50, 70), 200 + random.randint(-70, 50), color)
                        attack_animation_group.add(aa)

                        if monster is not None:
                            monster.current_health -= event["damage"]

                elif event["type"] == Event.monster_attack:
                    if attack_counter <= 0:
                        attack_counter = 0
                        next_turn_counter += 0

                        event["handled"] = True

                        u_pos = unit_damage_number_pos[event["unit"]]
                        color = pygame.Color("#FF0000")
                        unit_animation_pos  = unit_damage_animation_pos[event["unit"]]

                        fn = FloatingNumber(
                                u_pos[0] + random.randint(-15, 15),
                                u_pos[1],
                                '-{}'.format(event["damage"]),
                                color,
                                size=24)
                        floating_number_group.add(fn)

                        aa = AttackAnimation(unit_animation_pos[0], unit_animation_pos[1], pygame.Color("#FF0000"))
                        attack_animation_group.add(aa)



                elif event["type"] == Event.combat_resolved:

                    next_turn_counter += 30

                    event["handled"] = True

                elif event["type"] == Event.party_killed:
                    party_killed_screen(global_surf, fpsClock, event)


        attack_counter -= 1


        if location.node_type == NodeType.monster:
            monster = location.monster

            monster_name_surface = fontObj.render(monster.name, True, whiteColor)

            # clear monster hp bar
            monster_hp_bar.empty()

            bar = HealthBar(530, 90, 300, 50, monster.id)
            bar.rect.x = 640 - math.floor(bar.rect.w/2)
            monster_hp_bar.add(bar)

            # clear monster_group

            if location_change:
                monster_group.empty()

                monster_sprite = get_monster_sprite(monster.monster_type, monster_pos)
                monster_sprite.rect.x = 640 - math.floor(monster_sprite.rect.w/2)
                monster_group.add( monster_sprite )

        if location.node_type == NodeType.town:
            monster_hp_bar.empty()
            monster_group.empty()
            monster_name_surface = None


        # swap background image
        if location_change:
            if background == NodeType.monster:
                background_group.empty()
                background_group.add( get_monster_room_sprite() )
            if background == NodeType.town:
                background_group.empty()
                background_group.add( town_shop_sprite )
            else:
                pass


        #####
        # Rendering Stuff
        #####

        # render gold text if changed
        if draw_gold or first_loop:
            goldSurfaceObj = fontObj.render('Gold: {0}'.format(str(gold)), True, goldColor)

        # render trophies text if changed
        if draw_trophies or first_loop:
            trophiesSurfaceObj = fontObj.render('Trophies: {0}'.format(str(trophies)), True, goldColor)

        player1InfoSurface = fontObj.render(units[0].name, True, whiteColor)
        player2InfoSurface = fontObj.render(units[1].name, True, whiteColor)
        player3InfoSurface = fontObj.render(units[2].name, True, whiteColor)
        player4InfoSurface = fontObj.render(units[3].name, True, whiteColor)


        teamRectObj = teamSurfaceObj.get_rect()
        teamRectObj.topleft = (10,20)

        goldRectObj = goldSurfaceObj.get_rect()
        goldRectObj.topleft = (10,40)

        trophiesRectObj = trophiesSurfaceObj.get_rect()
        trophiesRectObj.topleft = (10, 60)

        player1InfoRect = player1InfoSurface.get_rect()
        player1InfoRect.topleft = (58, 512)

        player2InfoRect = player2InfoSurface.get_rect()
        player2InfoRect.topleft = (370, 512)

        player3InfoRect = player3InfoSurface.get_rect()
        player3InfoRect.topleft = (682, 512)

        player4InfoRect = player4InfoSurface.get_rect()
        player4InfoRect.topleft = (994, 512)

        if monster_name_surface is not None:
            monster_info_rect = monster_name_surface.get_rect()
            monster_info_rect.topleft = ( 640 - math.floor(monster_info_rect.w/2), 70)

        unit_hp_bars.update(units)

        monster_hp_bar.update([monster])

        monster_group.update()

        floating_number_group.update(floating_number_group)

        attack_animation_group.update(attack_animation_group)

        #####
        # Begin Drawing to screen
        #####

        # clear screen, fill with white
        global_surf.fill(blackColor)


        background_group.update()
        background_group.draw(global_surf)

        # draw team name
        global_surf.blit(teamSurfaceObj,teamRectObj)

        # draw gold text
        global_surf.blit(goldSurfaceObj,goldRectObj)

        # draw trohpy text
        global_surf.blit(trophiesSurfaceObj,trophiesRectObj)

        # draw unit info text
        global_surf.blit( player1InfoSurface, player1InfoRect)
        global_surf.blit( player2InfoSurface, player2InfoRect)
        global_surf.blit( player3InfoSurface, player3InfoRect)
        global_surf.blit( player4InfoSurface, player4InfoRect)
        if monster_name_surface is not None:
            global_surf.blit( monster_name_surface, monster_info_rect)

        # draw player hitpoints
        unit_hp_bars.draw(global_surf)

        monster_hp_bar.draw(global_surf)

        monster_group.draw(global_surf)

        icon_back_group.draw(global_surf)
        unit_icon_sprite_group.draw(global_surf)

        floating_number_group.draw(global_surf)
        attack_animation_group.draw(global_surf)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
               mousex, mousey = event.pos
               if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    fn = FloatingNumber(mouse_x, mouse_y, '-5000', whiteColor)
                    floating_number_group.add(fn)

        first_loop = False

        if next_turn_counter > 0:
            next_turn_counter -= 1

        pygame.display.update()
        #fpsClock.tick(60)


