from game.common.unit import *
from game.common.item_types import *
from game.common.items import *
from game.common.enums import *


def get_unit(unit_class, name):

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




class Knight(Unit):

    def init(self, name):
        Unit.init(self, name, "Knight", 5000, [ItemClass.melee, ItemType.sword])

class Brawler(Unit):
    def init(self, name):
        Unit.init(self, name, "Brawler", 5000, [ItemClass.melee, ItemType.mace])

class Pikeman(Unit):
    def init(self, name):
        Unit.init(self, name, "Pikeman", 5000, [ItemClass.melee, ItemType.spear])

class Rogue(Unit):
    def init(self, name):
        Unit.init(self, name, "Rogue", 5000, [ItemClass.melee, ItemType.dagger])

class Magus(Unit):
    def init(self, name):
        Unit.init(self, name, "Magus", 5000, [ItemClass.magic, ItemType.staff])

class Wizard(Unit):
    def init(self, name):
        Unit.init(self, name, "Wizard", 5000, [ItemClass.magic, ItemType.wand])

class Sorcerer(Unit):
    def init(self, name):
        Unit.init(self, name, "Sorcerer", 5000, [ItemClass.magic, ItemType.spell_book])

class Alchemist(Unit):
    def init(self, name):
        Unit.init(self, name, "Alchemist", 5000, [ItemClass.magic, ItemType.alchemy_supplies])



