import math

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
            0,
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait
            ])

    def to_dict(self):
        data = Unit.to_dict()

    def from_dict(self, data):
        data = Unit.from_dict(data)

    def _special_ability(self, damage, targets):

        if type(targets) is list or type(targets) is tuple:
            # Deal Damage to other units
            damage = math.floor(damage * 0.5)
            for target in targets:
                if target is not self:
                    target.current_health -= damage
                    if target.current_health < 0: target.current_health = 0
        else:
            # Calculate Damage
            damage = math.floor(damage * 0.85)

        # Apply Damage to self
        self.current_health -= damage
        if self.current_health < 0: self.current_health = 0



class Brawler(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Brawler",
            UnitClass.brawler,
            5000, # health
            [
                ItemClass.melee,
                ItemType.mace
            ],
            0, #item slots
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait
            ])

        self.ability_charged = False
        self.ability_damage_taken = 0

    def to_dict(self, safe=False):
        data = Unit.to_dict(safe)

        data["ability_charged"] = self.ability_charged
        data["ability_damage_taken"] = self.ability_damage_taken

    def from_dict(self, data, safe=False):
        data = Unit.from_dict(data, safe)

        self.ability_charged = data["ability_charged"]
        self.ability_damage_taken = data["ability_damage_taken"]

    def _special_ability(self, damage, monster):

        if not self.ability_charged:
            self.special_ability_timer += 1
            self.ability_damage_taken += damage

            if self.special_ability_timer > 2:
                self.ability_charged = True

        else:
            n = 1.0
            if math.floor(self.health * 0.25) < damage < math.floor(self.health * 0.5):
                n = 2.0
            elif math.floor(self.health * 0.5) < damage < math.floor(self.health * 75):
                n = 3.0
            elif damage > math.floor(self.health * 0.75):
                n = 3.5

            monster.damage = math.floor( self.primary_weapon.damage * ( 2.5 + ( n * 0.5) ) )
            if monster.damage < 0: monster.damage = 0

            self.ability_charged = False
            self.special_ability_timer = 0



class Pikeman(Unit):
    def init(self, name):
        Unit.init(self,
            name,
            "Pikeman",
            UnitClass.pikeman,
            5000, #health
            [
                ItemClass.melee,
                ItemType.spear
            ],
            0, #item slots
            [
                CombatAction.primary_weapon,
                CombatAction.special_ability,
                CombatAction.wait
            ])

        self.ability_charged = False

    def to_dict(self, safe=False):
        data = Unit.to_dict(safe)

        data["ability_charged"] = self.ability_charged

    def from_dict(self, data, safe=False):
        data = Unit.from_dict(data, safe)

        self.ability_charged = data["ability_charged"]

    def _special_ability(self, monster):

        if not self.ability_charged:
            self.charged = True

        else:
            self.charged = False

            monster.current_health = math.floor( self.primary_weapon.damage * 2.5 )
            if monster.current_health < 0: monster.current_health = 0



class Rogue(Unit):
    def init(self, name):
        Unit.init(self, name,
            "Rogue",
            UnitClass.rogue,
            5000, #health
            [
                ItemClass.melee,
                ItemType.dagger
            ],
            2, #item slots
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
            5000, #health
            [
                ItemClass.magic,
                ItemType.staff
            ],
            4, #item slots
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
            5000, # health
            [
                ItemClass.magic,
                ItemType.wand
            ],
            4, #item slots
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
            5000, #health
            [
                ItemClass.magic,
                ItemType.spell_book
            ],
            4, #item slots
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
            5000, #health
            [
                ItemClass.magic,
                ItemType.alchemy_supplies
            ],
            3, #item slots
            [
                CombatAction.secondary_1,
                CombatAction.secondary_2,
                CombatAction.secondary_3,
                CombatAction.special_ability,
                CombatAction.wait
            ])




