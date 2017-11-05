
class CombatAction:
    primary_weapon = 1
    secondary_1 = 2
    secondary_2 = 3
    secondary_3 = 4
    secondary_4 = 5
    special_ability = 6
    wait = 7

class UnitClass:
    knight = 1
    brawler = 2
    pikeman = 3
    rogue = 4
    magus = 5
    wizard = 6
    sorcerer = 7
    alchemist = 8


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
    chimera = 1
    beholder = 2
    goblin = 3
