class NodeType:
    monster = 1
    trap = 2
    town = 3
    start = 4
    end = 5

class Event:
    unit_health_restored = 0
    begin_combat = 1
    set_location = 2
    purchase_item = 3
    combat_resolved = 4
    party_killed = 5
    special_ability = 6
    special_ability_charging = 7
    special_ability_attack = 8
    monster_attack = 9
    unit_attack = 10
    room_choice = 11


class ItemSlot:
    primary = 0

    spell_1 = 1
    bomb_1 = 1

    spell_2 = 2
    bomb_2 = 2

    spell_3 = 3
    bomb_3 = 3

    spell_4 = 4

class CombatAction:
    primary_weapon = 1
    secondary_1 = 2
    secondary_2 = 3
    secondary_3 = 4
    secondary_4 = 5
    special_ability = 6
    wait = 8
    none = 9

class UnitClass:
    knight = 0
    brawler = 1
    pikeman = 2
    rogue = 3
    magus = 4
    wizard = 5
    sorcerer = 6
    alchemist = 7


class MessageType:
    town = 1
    combat_begin = 2
    combat_round = 3
    combat_end = 4
    room_choice = 5
    unit_choice = 6
    null = 7
    town_choice = 8


class ItemType:
    # melee
    sword = 1
    dagger = 2
    mace = 3
    spear = 4

    # magic item
    staff = 5
    wand = 6
    spell_book = 7
    alchemical_supplies = 8

    # magic spell
    fire_ball = 9
    thunderbolt = 10
    ice_spike = 11

    rope = 12

    fire_bomb = 13
    frost_bomb = 14
    shock_bomb = 15
    acid_bomb = 16
    flash_bomb = 17
    frost_bomb = 14
    shock_bomb = 15
    acid_bomb = 16
    flash_bomb = 17
    spike_bomb = 18
    concussion_bomb = 19

class ItemClass:
    melee = 1
    magic = 2
    spell = 3
    utility = 3



class DamageType:
    piercing = 0
    slashing = 1
    bludgeoning = 2
    precision = 3
    fire = 4
    cold = 5
    electricity = 6
    acid = 7
    sonic = 8
    force = 9



class TRAP_TYPE:
    pit_trap = 1
    spike_trap = 2
    boulder_trap = 3
    dart_trap = 4
    narrow_bridge = 5


class Direction:
    forward = 1
    left = 2
    right = 3


class MonsterType:
    wisp = 0
    beholder = 1
    goblin = 2
    dragon = 3
    minotaur = 4
    slime = 5






