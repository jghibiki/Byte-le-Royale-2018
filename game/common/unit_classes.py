from game.common.unit import *
from game.common.item_types import *
from game.common.items import *

class UnitClass:
    knight = 1
    brawler = 2
    pikeman = 3
    rogue = 4
    wizard = 5
    sorcerer = 6
    alchemist = 7


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



