import sys, math, random

import pygame
from pygame.locals import *

import ptext

from game.common.enums import *
from game.common.monster_types import get_monster

from game.visualizer.health_bar import HealthBar
from game.visualizer.spritesheet_functions import SpriteSheet
from game.visualizer.sprite_sheets import *
from game.visualizer.game_log_parser import GameLogParser
from game.visualizer.floating_number import FloatingNumber
from game.visualizer.progress_bar import ProgressBar
from game.visualizer.trap_text import TrapText


def party_killed_screen(global_surf, fps_clock, data):
    width = math.floor(1280/2.0)

    big_font = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf',70)
    med_font = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf',45)
    little_font = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf',30)

    you_have_died = big_font.render("Game Over", True, pygame.Color("#FFFFFF"))

    trophies = little_font.render(    "    Trophies: {0:06d}".format(data["trophies"]), True, pygame.Color("#FFFFFF"))

    current_gold = little_font.render("Current Gold: {0:06d}".format(data["gold"]), True, pygame.Color("#FFFFFF"))

    total_gold = little_font.render(  "  Total Gold: {0:06d}".format(data["total_gold"]), True, pygame.Color("#FFFFFF"))

    press_space_to_exit = med_font.render("Press Space to Exit...", True, pygame.Color("#FFFFFF"))

    # compute info rect
    info_rect = trophies.get_rect().unionall([current_gold.get_rect(), total_gold.get_rect()])

    # center info rect
    info_rect.x = (width-math.floor(info_rect.w/2))


    while True:
        global_surf.fill(pygame.Color("#000000"))


        # center and print game over
        rect = you_have_died.get_rect()
        pos = ( width-math.floor(rect.w/2), 100)
        global_surf.blit(you_have_died, pos)


        # draw trophies
        rect = trophies.get_rect()
        pos = ( info_rect.x + (math.floor(info_rect.w/2)-math.floor(rect.w/2)), 200)
        global_surf.blit(trophies, pos)

        # draw current gold
        rect = current_gold.get_rect()
        pos = ( info_rect.x + (math.floor(info_rect.w/2)-math.floor(rect.w/2)), 230)
        global_surf.blit(current_gold, pos)

        # draw total gold
        rect = total_gold.get_rect()
        pos = ( info_rect.x + (math.floor(info_rect.w/2)-math.floor(rect.w/2)), 260)
        global_surf.blit(total_gold, pos)


        # center and print press space to exit
        rect = press_space_to_exit.get_rect()
        pos = ( width-math.floor(rect.w/2), 600)
        global_surf.blit(press_space_to_exit, pos)

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


def unit_text(font, upper_left, unit):

    text_parts = []

    text = "Lvl{0} {1}".format(
        unit.primary_weapon.level,
        unit.primary_weapon.name
    )

    primary_weapon_text = ptext.draw(
        text,
        (0,0),
        color=(255, 255, 255),
        owidth=2.0,
        ocolor=(0, 0, 0),
        fontsize=14,
        fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

    primary_weapon_rect = primary_weapon_text.get_rect()

    primary_weapon_rect.topleft = upper_left

    text_parts.append([
        primary_weapon_text,
        primary_weapon_rect])

    if unit.unit_class is UnitClass.knight:
        pass

    elif unit.unit_class is UnitClass.brawler:
        pass

    elif unit.unit_class is UnitClass.rogue:
        if unit.bomb_1 is not None:

            text = "Lvl{0} {1} x {2}".format(
                unit.bomb_1.level,
                unit.bomb_1.name,
                unit.bomb_1_quantity
            )

            bomb_1_text = ptext.draw(
                text,
                (0,0),
                color=(255, 255, 255),
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=14,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            bomb_1_rect = bomb_1_text.get_rect()
            bomb_1_rect.topleft = (upper_left[0], upper_left[1]+20)

            text_parts.append([
                bomb_1_text,
                bomb_1_rect
            ])

        if unit.bomb_2 is not None:
            text = "Lvl{0} {1} x {2}".format(
                unit.bomb_2.level,
                unit.bomb_2.name,
                unit.bomb_2_quantity
            )

            bomb_2_text = ptext.draw(
                text,
                (0,0),
                color=(255, 255, 255),
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=14,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            bomb_2_rect = bomb_2_text.get_rect()
            bomb_2_rect.topleft = (upper_left[0], upper_left[1]+40)

            text_parts.append([
                bomb_2_text,
                bomb_2_rect
            ])

        if unit.bomb_3 is not None:
            text = "Lvl{0} {1} x {2}".format(
                unit.bomb_3.level,
                unit.bomb_3.name,
                unit.bomb_3_quantity
            )

            bomb_3_text = ptext.draw(
                text,
                (0,0),
                color=(255, 255, 255),
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=14,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            bomb_3_rect = bomb_3_text.get_rect()
            bomb_3_rect.topleft = (upper_left[0], upper_left[1]+60)

            text_parts.append([
                bomb_3_text,
                bomb_3_rect
            ])

    elif unit.unit_class is UnitClass.alchemist:
        if unit.bomb_1 is not None:
            text = "Lvl{0} {1} x {2}".format(
                unit.bomb_1.level,
                unit.bomb_1.name,
                unit.bomb_1_quantity
            )

            bomb_1_text = ptext.draw(
                text,
                (0,0),
                color=(255, 255, 255),
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=14,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            bomb_1_rect = bomb_1_text.get_rect()
            bomb_1_rect.topleft = (upper_left[0], upper_left[1]+20)

            text_parts.append([
                bomb_1_text,
                bomb_1_rect
            ])

        if unit.bomb_2 is not None:
            text = "Lvl{0} {1} x {2}".format(
                unit.bomb_2.level,
                unit.bomb_2.name,
                unit.bomb_2_quantity
            )

            bomb_2_text = ptext.draw(
                text,
                (0,0),
                color=(255, 255, 255),
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=14,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            bomb_2_rect = bomb_2_text.get_rect()
            bomb_2_rect.topleft = (upper_left[0], upper_left[1]+40)

            text_parts.append([
                bomb_2_text,
                bomb_2_rect
            ])

    return text_parts


def start(verbose, log_path, gamma):

    log_parser = GameLogParser(log_path)
    team_name, units, events = log_parser.get_turn()

    # assign unit colors
    unit_colors = {}
    colors = [
        pygame.Color("#FFFB00"),
        pygame.Color("#FF0084"),
        pygame.Color("#0005FF"),
        pygame.Color("#00FF7A")
    ]
    for unit in units:
        unit_colors[unit.id] = colors.pop()
    del colors

    location = None # current location

    pygame.init()
    fpsClock = pygame.time.Clock()

    global_surf = pygame.display.set_mode((1280,720))
    pygame.display.set_caption('DnD Visualizer')

    pygame.display.set_gamma(gamma)

    bgSurfaceObj = pygame.image.load('game/visualizer/assets/brick_wall.png')
    bgSurfaceObj = pygame.transform.scale(bgSurfaceObj,(1280,720))

    redColor = pygame.Color(255,0,0)
    greenColor = pygame.Color(0,255,0)
    blueColor = pygame.Color(0,0,255)
    color_white = pygame.Color(255,255,255)
    goldColor = pygame.Color(255,215,0)
    blackColor = pygame.Color(0,0,0)
    mousex, mousey = 0, 0


    fontObj = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf',20)
    small_font = pygame.font.Font('game/visualizer/assets/joystix/joystix monospace.ttf', 14)

    team_name = ''
    gold = 300
    trophies = 0

    monster = None

    archway_group = pygame.sprite.OrderedUpdates()

    unit_hp_bars = pygame.sprite.Group()
    unit_sprite_group = pygame.sprite.Group()

    trap_progress_group = pygame.sprite.Group()

    trap_text_group = pygame.sprite.Group()

    unit_hp_bar_pos = [(20, 544), (332, 544), (644, 544), (956, 544)]
    unit_sprite_pos = [(80, 320), (392, 320), (704, 320), (1016, 320)]

    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id, unit=True) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id, unit=True) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id, unit=True) )
        unit_hp_bars.add( HealthBar(*pos, 300, 50, units[idx].id, unit=True) )

    unit_damage_number_pos = {}

    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_damage_number_pos[ units[idx].id ] = ( pos[0]+20, pos[1]-80 )

    unit_damage_animation_pos = {}
    for idx, pos in enumerate(unit_hp_bar_pos):
        unit_damage_animation_pos[ units[idx].id ] = (pos[0]+80, pos[1]- 200)

    for idx, pos in enumerate(unit_sprite_pos):
        unit_sprite = get_unit_sprite( units[idx].unit_class, pos)
        unit_sprite_group.add( unit_sprite )


    monster_hp_bar = pygame.sprite.Group()
    monster_name_surface = None

    floating_number_group = pygame.sprite.Group()
    attack_animation_group = pygame.sprite.Group()
    unit_icon_sprite_group = pygame.sprite.Group()
    icon_back_group = pygame.sprite.Group()
    monster_group = pygame.sprite.Group()


    monster_pos = (585,120)


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
    background_group.add(HillSprite())

    town_shop_sprite = TownShopSprite()

    trap_sprite_group = pygame.sprite.Group()


    first_loop = True
    next_turn_counter = 0
    background = NodeType.town
    attack_counter = 0
    room_choice = False
    room_resolved = False

    while True:

        # per loop flags
        draw_gold = False
        draw_trophies = False
        location_change = False

        if log_parser.check_finished():
            sys.exit()

        if next_turn_counter <= 0:
            if (verbose):
                print("Game Turn: " + str(log_parser.tick))
            team_name, units, events = log_parser.get_turn()

            room_choice = False
            archway_group.empty()

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
                        next_turn_counter += 55

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
                                size=25)
                        floating_number_group.add(fn)

                        aa = AttackAnimation(unit_animation_pos[0], unit_animation_pos[1], pygame.Color("#FF0000"))
                        attack_animation_group.add(aa)

                elif event["type"] == Event.combat_resolved:

                    next_turn_counter += 30

                    event["handled"] = True

                elif event["type"] == Event.begin_trap_evade:

                    event["handled"] = True

                    trap_sprite_group.add( get_trap_sprite(location.trap.trap_type) )

                    trap_text_group.add( TrapText(10, "Lvl{} {}".format(location.trap.level, location.trap.name)))

                    if(location.trap.pass_type is TrapPassType.individual_pass or
                       location.trap.pass_type is TrapPassType.group_pass_on_first_success):

                        def get_effort(trap, index):
                            return trap.current_effort[index]

                        trap_progress_group.add( ProgressBar(80, 300, 200, 20, location.trap.required_effort, lambda t: get_effort(t, 0)) )
                        trap_progress_group.add( ProgressBar(390, 300, 200, 20, location.trap.required_effort, lambda t: get_effort(t, 1)) )
                        trap_progress_group.add( ProgressBar(700, 300, 200, 20, location.trap.required_effort, lambda t: get_effort(t, 2)) )
                        trap_progress_group.add( ProgressBar(1010, 300, 200, 20, location.trap.required_effort, lambda t: get_effort(t, 3)) )

                    elif location.trap.pass_type is TrapPassType.group_pass:

                        def get_effort(trap):
                            return trap.current_effort

                        trap_progress_group.add( ProgressBar(400, 50, 500, 30, location.trap.required_effort, get_effort) )


                elif event["type"] == Event.trap_resolved:
                    event["handled"] = True
                    trap_progress_group.empty()
                    trap_text_group.empty()

                elif event["type"] == Event.party_killed:
                    party_killed_screen(global_surf, fpsClock, event)

                elif event["type"] == Event.room_choice:
                    room_choice = True

                    trap_sprite_group.empty()

                    if event["room_1"] is not None and event["room_2"] is not None:
                        room_1_pos = (256, 48)
                        room_2_pos = (768, 48)
                    else:
                        room_1_pos = (512, 48)

                    rm_1 = None
                    rm_2 = None

                    if event["room_1"] is not None:
                        if event["room_1"].node_type is NodeType.monster:
                            rm_1 = ArchwaySprite(
                                *room_1_pos,
                                "Lvl{}\n{}".format(
                                    event["room_1"].monster.level,
                                    event["room_1"].monster.name
                                ),
                                event["choice"] == "room_1")

                        elif event["room_1"].node_type is NodeType.trap:
                            rm_1 = ArchwaySprite(
                                *room_1_pos,
                                "Lvl{}\n{}".format(
                                    event["room_1"].trap.level,
                                    event["room_1"].trap.name
                                ),
                                event["choice"] == "room_1")

                        elif event["room_1"].node_type is NodeType.town:
                            rm_1 = ArchwaySprite(
                                *room_1_pos,
                                "Town",
                                event["choice"] == "room_1")

                    # room 2
                    if event["room_2"] is not None:
                        if event["room_2"].node_type is NodeType.monster:
                            rm_2 = ArchwaySprite(
                                *room_2_pos,
                                "Lvl{}\n{}".format(
                                    event["room_2"].monster.level,
                                    event["room_2"].monster.name
                                ),
                                event["choice"] == "room_2")

                        elif event["room_2"].node_type is NodeType.trap:
                            rm_2 = ArchwaySprite(
                                *room_2_pos,
                                "Lvl{}\n{}".format(
                                    event["room_2"].trap.level,
                                    event["room_2"].trap.name
                                ),
                                event["choice"] == "room_2")

                        elif event["room_2"].node_type is NodeType.town:
                            rm_2 = ArchwaySprite(
                                *room_2_pos,
                                "Town",
                                event["choice"] == "room_2")

                    if rm_1 is not None and rm_2 is not None:
                        if event["choice"] == "room_1":
                            archway_group.add(rm_2)
                            archway_group.add(rm_1)
                        else:
                            archway_group.add(rm_1)
                            archway_group.add(rm_2)
                    elif rm_1 is not None:
                        archway_group.add(rm_1)


                    if background == NodeType.town:
                        background_group.empty()
                        background_group.add(HillSprite())

                    monster_hp_bar.empty()
                    monster_group.empty()
                    monster_name_surface = pygame.Surface((0,0))

                    next_turn_counter += 30

                    event["handled"] = True

        attack_counter -= 1


        if location.node_type == NodeType.monster and not room_choice:
            monster = location.monster

            monster_name_surface = fontObj.render("Lvl{} {}".format(monster.level, monster.name), True, color_white)

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
                trap_sprite_group.empty()
                background_group.add( get_room_sprite() )

            elif background == NodeType.trap:
                background_group.empty()
                background_group.add( get_room_sprite() )

            elif background == NodeType.town:
                background_group.empty()
                trap_sprite_group.empty()
                background_group.add( town_shop_sprite )
            else:
                pass


        #####
        # Rendering Stuff
        #####

        unit_item_text = []
        unit_item_text_pos = [(20, 584), (332, 584), (644, 584), (956, 584)]
        # render unit item text
        for unit, pos in zip(units, unit_item_text_pos):
            unit_item_text +=  unit_text(small_font, pos, unit)

        # render gold text if changed
        if draw_gold or first_loop:
            gold_surf = fontObj.render('Gold: {0:06d}'.format(gold), True, goldColor)

            _pos = (1270, 10)

            # handle font shifting when rendering a to a different width as a result of a narrow character such as 1
            gold_rect = gold_surf.get_rect()
            gold_rect.topright = _pos


        # render trophies text if changed
        if draw_trophies or first_loop:
            trophiesSurfaceObj = fontObj.render('Trophies: {0:06d}'.format(trophies), True, goldColor)

            _pos = (1270, 35)

            trophies_rect = trophiesSurfaceObj.get_rect()
            trophies_rect.topright = _pos

        # render gold and trophies bg
        if trophies_rect and gold_rect and first_loop:
            trophy_gold_background_rect = trophies_rect.union(gold_rect)
            trophy_gold_background_rect.inflate_ip(10, 10)


        # render team name
        if first_loop:
            team_name_surf = fontObj.render(team_name[0:20], True, color_white)
            team_name_rect = team_name_surf.get_rect()
            team_name_rect.topleft = (10,10)

            # calculate rect for team name background
            team_background_rect = team_name_rect.copy()
            team_background_rect.inflate_ip(10, 10)


        # draw unit names
        unit_name_text_pos = [
            (58, 512),
            (370, 512),
            (682, 512),
            (994, 512)
        ]
        unit_name_texts = []
        for idx, (unit, pos) in enumerate(zip(units, unit_name_text_pos)):
            unit_text_surf = ptext.draw(
                units[idx].name,
                (0,0),
                color=unit_colors[unit.id],
                owidth=2.0,
                ocolor=(0, 0, 0),
                fontsize=20,
                fontname='game/visualizer/assets/joystix/joystix monospace.ttf')[0]

            unit_text_rect = unit_text_surf.get_rect()
            unit_text_rect.topleft = pos

            unit_name_texts.append( [unit_text_surf, unit_text_rect] )

        if monster_name_surface is not None:
            monster_info_rect = monster_name_surface.get_rect()
            monster_info_rect.topleft = ( 640 - math.floor(monster_info_rect.w/2), 60)

        archway_group.update()

        unit_sprite_group.update()

        unit_hp_bars.update(units)

        monster_hp_bar.update([monster])

        monster_group.update()

        floating_number_group.update(floating_number_group)

        attack_animation_group.update(attack_animation_group)

        background_group.update()

        trap_sprite_group.update()

        if location is not None and location.node_type is NodeType.trap:
            trap_progress_group.update(location.trap)

        #####
        # Begin Drawing to screen
        #####

        # clear screen, fill with white
        global_surf.fill(blackColor)

        background_group.draw(global_surf)

        trap_sprite_group.draw(global_surf)


        # draw team name background
        global_surf.fill(pygame.Color(54, 54, 54, 200), rect=team_background_rect, special_flags=pygame.BLEND_RGBA_SUB)

        # draw team name
        global_surf.blit(team_name_surf, team_name_rect)

        global_surf.fill(pygame.Color(54, 54, 54, 200), rect=trophy_gold_background_rect, special_flags=pygame.BLEND_RGBA_SUB)

        # draw gold text
        global_surf.blit(gold_surf, gold_rect)

        # draw trohpy text
        global_surf.blit(trophiesSurfaceObj,trophies_rect)


        # draw unit info text
        for text, pos in unit_name_texts:
            global_surf.blit( text, pos )

        if monster_name_surface is not None:
            global_surf.blit( monster_name_surface, monster_info_rect)

        # draw unit item text
        for text, pos in unit_item_text:
            global_surf.blit(text, pos)

        # draw player hitpoints
        unit_hp_bars.draw(global_surf)

        # draw monster hp bars
        monster_hp_bar.draw(global_surf)

        # draw monsters
        monster_group.draw(global_surf)

        archway_group.draw(global_surf)

        # draw units
        unit_sprite_group.draw(global_surf)

        # draw unit icons
        icon_back_group.draw(global_surf)
        unit_icon_sprite_group.draw(global_surf)

        # draw floating numbers
        floating_number_group.draw(global_surf)
        attack_animation_group.draw(global_surf)

        trap_progress_group.draw(global_surf)

        trap_text_group.draw(global_surf)

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
                    fn = FloatingNumber(mouse_x, mouse_y, '-5000', color_white)
                    floating_number_group.add(fn)

        first_loop = False

        if next_turn_counter > 0:
            next_turn_counter -= 1


        pygame.display.update()
        fpsClock.tick(30)


