from game.common.unit import *
from game.common.item_types import *
from game.common.items import *
from game.common.enums import *


def get_unit(unit_class, name=""):

    knight = 1
    brawler = 2
    pikeman = 3
    rogue = 4
    wizard = 5
    sorcerer = 6
    alchemist = 7
    magus = 8

    if unit_class == UnitClass.knight:
        new_unit = Knight()
    elif unit_class == UnitClass.brawler:
        new_unit = Brawler()
    elif unit_class == UnitClass.pikeman:
        new_unit = Pikeman()
    elif unit_class == UnitClass.rogue:
        new_unit = Rogue()

    elif unit_class == UnitClass.magus:
        new_unit = Magus()
    elif unit_class == UnitClass.wizard:
        new_unit = Wizard()
    elif unit_class == UnitClass.sorcerer:
        new_unit = Sorcerer()
    elif unit_class == UnitClass.alchemist:
        new_unit = Alchemist()

    new_unit.init(name)

    return new_unit


    primary_weapon = 1
    secondary_1 = 2
    secondary_2 = 3
    secondary_3 = 4
    secondary_4 = 5
    special_ability = 6
    wait = 7


class Knight(Unit):

    def init(self, name):
        Unit.init(self, 
            name, 
            "Knight", 
            UnitClass.knight, 
            5000, 
            [
                ItemClass.melee, 
                ItemType.sword
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait 
            ])


class Brawler(Unit):
    def init(self, name):
        Unit.init(self, 
            name, 
            "Brawler", 
            UnitClass.brawler, 
            5000, 
            [
                ItemClass.melee, 
                ItemType.mace
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait 
            ])

class Pikeman(Unit):
    def init(self, name):
        Unit.init(self, 
            name, 
            "Pikeman", 
            UnitClass.pikeman, 
            5000, 
            [
                ItemClass.melee, 
                ItemType.spear
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait 
            ])

class Rogue(Unit):
    def init(self, name):
        Unit.init(self, name, 
            "Rogue", 
            UnitClass.rogue, 
            5000,
            [
                ItemClass.melee, 
                ItemType.dagger
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.wait 
            ])

class Magus(Unit):
    def init(self, name):
        Unit.init(self, 
            name, "Magus", 
            UnitClass.magus, 
            5000, 
            [
                ItemClass.magic,
                ItemType.staff
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.secondary_3,
                CombatAction.secondary_4,
                CombatAction.special_ability,
                CombatAction.wait 
            ])

class Wizard(Unit):
    def init(self, name):
        Unit.init(self, 
            name, 
            "Wizard", 
            UnitClass.wizard, 
            5000, 
            [
                ItemClass.magic, 
                ItemType.wand
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.secondary_3,
                CombatAction.secondary_4,
                CombatAction.special_ability,
                CombatAction.wait 
            ])

class Sorcerer(Unit):
    def init(self, name):
        Unit.init(self, 
            name, 
            "Sorcerer", 
            UnitClass.sorcerer, 
            5000, 
            [
                ItemClass.magic, 
                ItemType.spell_book
            ],
            [
                CombatAction.primary_weapon,
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.secondary_3,
                CombatAction.secondary_4,
                CombatAction.special_ability,
                CombatAction.wait 
            ])

class Alchemist(Unit):
    def init(self, name):
        Unit.init(self, 
            name, 
            "Alchemist", 
            UnitClass.alchemist, 
            5000, 
            [
                ItemClass.magic, 
                ItemType.alchemy_supplies
            ],
            [
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.secondary_3,
                CombatAction.special_ability,
                CombatAction.wait 
            ])




