import math

from game.common.unit import *
from game.common.item_types import *
from game.common.items import *
from game.common.enums import *


def get_unit(unit_class, name=""):

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


def load_unit(unit_class, unit_data):
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

    new_unit.from_dict(unit_data)

    return new_unit




class Knight(Unit):

    def init(self, name):
        Unit.init(self,
            name,
            "Knight",
            UnitClass.knight,
            11000,
            100, # focus
            100, # will
            ItemType.sword)

    def attack(self):
        self.combat_action = CombatAction.primary_weapon

    def taunt(self):
        self.combat_action = CombatAction.special_ability

    def wait(self):
        self.combat_action = CombatAction.wait


class Brawler(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Brawler",
            UnitClass.brawler,
            12000, # health
            100, # focus
            100, # will
            ItemType.mace)

    def attack(self):
        self.combat_action = CombatAction.primary_weapon

    def fit_of_rage(self):
        self.combat_action = CombatAction.special_ability

    def wait(self):
        self.combat_action = CombatAction.wait



class Pikeman(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Pikeman",
            UnitClass.pikeman,
            13000, # health
            100, # focus
            100, # will
            ItemType.spear)

    def attack(self):
        self.combat_action = CombatAction.primary_weapon

    def target_weakness(self):
        self.combat_action = CombatAction.special_ability

    def wait(self):
        self.combat_action = CombatAction.wait


class Rogue(Unit):
    def init(self, name):
        Unit.init(self, name,
            "Rogue",
            UnitClass.rogue,
            14000, # health
            100, # focus
            100, # will
            ItemType.dagger)

        self.bomb_1 = None
        self.bomb_1_quantity = 0

        self.bomb_2 = None
        self.bomb_2_quantity = 0

        self.bomb_3 = None
        self.bomb_3_quantity = 0

    def to_dict(self):
        data = Unit.to_dict(self)

        if self.bomb_1 is None:
            data["bomb_1"] = None
        else:
            data["bomb_1"] = self.bomb_1.to_dict()
        data["bomb_1_quantity"] = self.bomb_1_quantity

        if self.bomb_2 is None:
            data["bomb_2"] = None
        else:
            data["bomb_2"] = self.bomb_2.to_dict()
        data["bomb_2_quantity"] = self.bomb_2_quantity

        if self.bomb_3 is None:
            data["bomb_3"] = None
        else:
            data["bomb_3"] = self.bomb_3.to_dict()
        data["bomb_3_quantity"] = self.bomb_3_quantity

        return data

    def from_dict(self, data):
        Unit.from_dict(self, data)

        if data["bomb_1"] is not None:
            self.bomb_1 = load_item(data["bomb_1"]["item_type"], data["bomb_1"])
        else:
            self.bomb_1 = None
        self.bomb_1_quantity = data["bomb_1_quantity"]

        if data["bomb_2"] is not None:
            self.bomb_2 = load_item(data["bomb_2"]["item_type"], data["bomb_2"])
        else:
            self.bomb_2 = None
        self.bomb_2_quantity = data["bomb_2_quantity"]

        if data["bomb_3"] is not None:
            self.bomb_3 = load_item(data["bomb_3"]["item_type"], data["bomb_3"])
        else:
            self.bomb_3 = None
        self.bomb_3_quantity = data["bomb_3_quantity"]

    def use_bomb_1(self):
        self.combat_action = CombatAction.secondary_1

    def use_bomb_2(self):
        self.combat_action = CombatAction.secondary_2

    def use_bomb_3(self):
        self.combat_action = CombatAction.secondary_3

    def wait(self):
        self.combat_action = CombatAction.wait

class Magus(Unit):
    def init(self, name):
        Unit.init(self,
            name, "Magus",
            UnitClass.magus,
            15000, # health
            100, # focus
            100, # will
            ItemType.staff)

        self.spell_1 = None
        self.spell_2 = None
        self.spell_3 = None
        self.spell_4 = None

    def to_dict(self):
        data = Unit.to_dict(self)

        if self.spell_1 is None:
            data["spell_1"] = None
        else:
            data["spell_1"] = self.spell_1.to_dict()

        if self.spell_2 is None:
            data["spell_2"] = None
        else:
            data["spell_2"] = self.spell_2.to_dict()

        if self.spell_3 is None:
            data["spell_3"] = None
        else:
            data["spell_3"] = self.spell_3.to_dict()

        if self.spell_4 is None:
            data["spell_4"] = None
        else:
            data["spell_4"] = self.spell_4.to_dict()

        return data

    def from_dict(self, data):
        Unit.from_dict(self, data)

        if data["spell_1"] is not None:
            self.spell_1 = load_item(data["spell_1"]["item_type"], data["spell_1"])
        else:
            self.spell_1 = None

        if data["spell_2"] is not None:
            self.spell_2 = load_item(data["spell_2"]["item_type"], data["spell_2"])
        else:
            self.spell_2 = None

        if data["spell_3"] is not None:
            self.spell_3 = load_item(data["spell_3"]["item_type"], data["spell_3"])
        else:
            self.spell_3 = None

        if data["spell_4"] is not None:
            self.spell_4 = load_item(data["spell_4"]["item_type"], data["spell_4"])
        else:
            self.spell_4 = None

    def use_spell_1(self):
        self.combat_action = CombatAction.secondary_1

    def use_spell_2(self):
        self.combat_action = CombatAction.secondary_2

    def use_spell_3(self):
        self.combat_action = CombatAction.secondary_3

    def use_spell_4(self):
        self.combat_action = CombatAction.secondary_4

    def elemental_burst(self):
        self.combat_action = CombatAction.special_ability

    def wait(self):
        self.combat_action = CombatAction.wait


class Wizard(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Wizard",
            UnitClass.wizard,
            16000, # health
            100, # focus
            100, # will
            ItemType.wand)

        self.spell_1 = None
        self.spell_2 = None
        self.spell_3 = None
        self.spell_4 = None

    def to_dict(self):
        data = Unit.to_dict(self)

        if self.spell_1 is None:
            data["spell_1"] = None
        else:
            data["spell_1"] = self.spell_1.to_dict()

        if self.spell_2 is None:
            data["spell_2"] = None
        else:
            data["spell_2"] = self.spell_2.to_dict()

        if self.spell_3 is None:
            data["spell_3"] = None
        else:
            data["spell_3"] = self.spell_3.to_dict()

        if self.spell_4 is None:
            data["spell_4"] = None
        else:
            data["spell_4"] = self.spell_4.to_dict()

        return data

    def from_dict(self, data):
        Unit.from_dict(self, data)

        if data["spell_1"] is not None:
            self.spell_1 = load_item(data["spell_1"]["item_type"], data["spell_1"])
        else:
            self.spell_1 = None

        if data["spell_2"] is not None:
            self.spell_2 = load_item(data["spell_2"]["item_type"], data["spell_2"])
        else:
            self.spell_2 = None

        if data["spell_3"] is not None:
            self.spell_3 = load_item(data["spell_3"]["item_type"], data["spell_3"])
        else:
            self.spell_3 = None

        if data["spell_4"] is not None:
            self.spell_4 = load_item(data["spell_4"]["item_type"], data["spell_4"])
        else:
            self.spell_4 = None

    def use_spell_1(self):
        self.combat_action = CombatAction.secondary_1

    def use_spell_2(self):
        self.combat_action = CombatAction.secondary_2

    def use_spell_3(self):
        self.combat_action = CombatAction.secondary_3

    def use_spell_4(self):
        self.combat_action = CombatAction.secondary_4

    def invigorate(self, target):
        self.combat_action = CombatAction.special_ability
        self.combat_action_target_1 = target.id

    def wait(self):
        self.combat_action = CombatAction.wait


class Sorcerer(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Sorcerer",
            UnitClass.sorcerer,
            17000, # health
            100, # focus
            100, # will
            ItemType.spell_book)

        self.spell_1 = None
        self.spell_2 = None
        self.spell_3 = None
        self.spell_4 = None

    def to_dict(self):
        data = Unit.to_dict(self)

        if self.spell_1 is None:
            data["spell_1"] = None
        else:
            data["spell_1"] = self.spell_1.to_dict()

        if self.spell_2 is None:
            data["spell_2"] = None
        else:
            data["spell_2"] = self.spell_2.to_dict()

        if self.spell_3 is None:
            data["spell_3"] = None
        else:
            data["spell_3"] = self.spell_3.to_dict()

        if self.spell_4 is None:
            data["spell_4"] = None
        else:
            data["spell_4"] = self.spell_4.to_dict()

        return data

    def from_dict(self, data):
        Unit.from_dict(self, data)

        if data["spell_1"] is not None:
            self.spell_1 = load_item(data["spell_1"]["item_type"], data["spell_1"])
        else:
            self.spell_1 = None

        if data["spell_2"] is not None:
            self.spell_2 = load_item(data["spell_2"]["item_type"], data["spell_2"])
        else:
            self.spell_2 = None

        if data["spell_3"] is not None:
            self.spell_3 = load_item(data["spell_3"]["item_type"], data["spell_3"])
        else:
            self.spell_3 = None

        if data["spell_4"] is not None:
            self.spell_4 = load_item(data["spell_4"]["item_type"], data["spell_4"])
        else:
            self.spell_4 = None

    def use_spell_1(self):
        self.combat_action = CombatAction.secondary_1

    def use_spell_2(self):
        self.combat_action = CombatAction.secondary_2

    def use_spell_3(self):
        self.combat_action = CombatAction.secondary_3

    def use_spell_4(self):
        self.combat_action = CombatAction.secondary_4

    def illusion(self, target_1, target_2):
        self.combat_action = CombatAction.special_ability
        self.combat_action_target_1 = target_1.id
        self.combat_action_target_2 = target_2.id

    def wait(self):
        self.combat_action = CombatAction.wait



class Alchemist(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Alchemist",
            UnitClass.alchemist,
            18000, # health
            100, # focus
            100, # will
            ItemType.alchemical_supplies)


        self.bomb_1 = None
        self.bomb_1_quantity = 0

        self.bomb_2 = None
        self.bomb_2_quantity = 0

    def to_dict(self):
        data = Unit.to_dict(self)

        if self.bomb_1 is None:
            data["bomb_1"] = None
        else:
            data["bomb_1"] = self.bomb_1.to_dict()
        data["bomb_1_quantity"] = self.bomb_1_quantity

        if self.bomb_2 is None:
            data["bomb_2"] = None
        else:
            data["bomb_2"] = self.bomb_2.to_dict()
        data["bomb_2_quantity"] = self.bomb_2_quantity

        return data

    def from_dict(self, data):
        Unit.from_dict(self, data)

        if data["bomb_1"] is not None:
            self.bomb_1 = load_item(data["bomb_1"]["item_type"], data["bomb_1"])
        else:
            self.bomb_1 = None
        self.bomb_1_quantity = data["bomb_1_quantity"]

        if data["bomb_2"] is not None:
            self.bomb_2 = load_item(data["bomb_2"]["item_type"], data["bomb_2"])
        else:
            self.bomb_2 = None
        self.bomb_2_quantity = data["bomb_2_quantity"]


    def use_bomb_1(self):
        self.combat_action = CombatAction.secondary_1

    def use_bomb_2(self):
        self.combat_action = CombatAction.secondary_2

    def resupply(self, bomb_slot):
        self.combat_action = CombatAction.special_ability
        self.combat_action_target_1 = bomb_slot

    def wait(self):
        self.combat_action = CombatAction.wait
