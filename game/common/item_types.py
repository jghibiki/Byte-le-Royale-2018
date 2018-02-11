from game.common.items import *
from game.common.enums import *


def get_item(item_type, level, unit_class=None, init=False):

    # melee items
    if item_type == ItemType.sword:
        new_item = Sword()
    elif item_type == ItemType.dagger:
        new_item = Dagger()
    elif item_type == ItemType.mace:
        new_item = Mace()
    elif item_type == ItemType.spear:
        new_item = Spear()

    # magic items
    elif item_type == ItemType.staff:
        new_item = Staff()
    elif item_type == ItemType.wand:
        new_item = Wand()
    elif item_type == ItemType.spell_book:
        new_item = SpellBook()
    elif item_type == ItemType.alchemical_supplies:
        new_item = AlchemicalSupplies()

    # spells
    elif item_type == ItemType.fire_ball:
        new_item = Fireball()
    elif item_type == ItemType.thunderbolt:
        new_item = Thunderbolt()
    elif item_type == ItemType.ice_spike:
        new_item = IceSpike()
    elif item_type == ItemType.sonic_blast:
        new_item = SonicBlast()
    elif item_type == ItemType.magic_sword:
        new_item = MagicSword()
    elif item_type == ItemType.spear_of_light:
        new_item = SpearOfLight()
    elif item_type == ItemType.rock_smash:
        new_item = RockSmash()

    # Bombs
    elif item_type == ItemType.fire_bomb:
        new_item = FireBomb()
    elif item_type == ItemType.frost_bomb:
        new_item = FrostBomb()
    elif item_type == ItemType.shock_bomb:
        new_item = ShockBomb()
    elif item_type == ItemType.acid_bomb:
        new_item = AcidBomb()
    elif item_type == ItemType.flash_bomb:
        new_item = FlashBomb()
    elif item_type == ItemType.spike_bomb:
        new_item = SpikeBomb()
    elif item_type == ItemType.concussion_bomb:
        new_item = ConcussionBomb()
    elif item_type == ItemType.guided_bomb:
        new_item = GuidedBomb()

    elif item_type == ItemType.armor:
        new_item = Armor()

    else:
        raise Exception("Invalid item type: {0}".format(item_type))

    if unit_class is not None:
        new_item.init(level, unit_class=unit_class)
    else:
        new_item.init(level)

    return new_item

def load_item(item_type, data, unit_class=None):

    # combat items
    if item_type == ItemType.sword:
        new_item = Sword()
    elif item_type == ItemType.dagger:
        new_item = Dagger()
    elif item_type == ItemType.mace:
        new_item = Mace()
    elif item_type == ItemType.spear:
        new_item = Spear()
    elif item_type == ItemType.staff:
        new_item = Staff()
    elif item_type == ItemType.wand:
        new_item = Wand()
    elif item_type == ItemType.spell_book:
        new_item = SpellBook()
    elif item_type == ItemType.alchemical_supplies:
        new_item = AlchemicalSupplies()
    elif item_type == ItemType.fire_ball:
        new_item = Fireball()
    elif item_type == ItemType.thunderbolt:
        new_item = Thunderbolt()
    elif item_type == ItemType.ice_spike:
        new_item = IceSpike()
    elif item_type == ItemType.sonic_blast:
        new_item = SonicBlast()
    elif item_type == ItemType.magic_sword:
        new_item = MagicSword()
    elif item_type == ItemType.spear_of_light:
        new_item = SpearOfLight()
    elif item_type == ItemType.rock_smash:
        new_item = RockSmash()

    # Bombs
    elif item_type == ItemType.fire_bomb:
        new_item = FireBomb()
    elif item_type == ItemType.frost_bomb:
        new_item = FrostBomb()
    elif item_type == ItemType.shock_bomb:
        new_item = ShockBomb()
    elif item_type == ItemType.acid_bomb:
        new_item = AcidBomb()
    elif item_type == ItemType.flash_bomb:
        new_item = FlashBomb()
    elif item_type == ItemType.spike_bomb:
        new_item = SpikeBomb()
    elif item_type == ItemType.concussion_bomb:
        new_item = ConcussionBomb()
    elif item_type == ItemType.guided_bomb:
        new_item = GuidedBomb()

    # armor items
    elif item_type == ItemType.armor:
        new_item = Armor()

    else:
        raise Exception("Invalid item type: {0}".format(item_type))

    new_item.from_dict(data)

    return new_item

################
# Melee Weapon #
################

class Sword(CombatItem):

    def init(self, level):
        CombatItem.init(self,
                        "Sword",
                        [
                            832,
                            1074,
                            1278,
                            1446,
                            1582,
                            1694,
                            1798,
                            1926,
                            2142,
                            2574
                        ],
                        [ DamageType.slashing ],
                        level,
                        ItemType.sword)

class Dagger(CombatItem):

    def init(self, level):
        CombatItem.init(self,
                        "Dagger",
                        [
                            896,
                            1030,
                            1154,
                            1270,
                            1382,
                            1498,
                            1634,
                            1822,
                            2126,
                            2674
                        ],
                        [
                            DamageType.piercing,
                            DamageType.slashing
                        ],
                        level,
                        ItemType.dagger)

class Spear(CombatItem):

    def init(self, level):
        CombatItem.init(self,
                        "Spear",
                        [
                            1019,
                            1178,
                            1344,
                            1527,
                            1741,
                            2019,
                            2426,
                            3088,
                            4262,
                            6460
                        ],
                        [
                            DamageType.piercing
                        ],
                        level,
                        ItemType.spear)

class Mace(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Mace",
                        [
                            483,
                            632,
                            959,
                            1086,
                            1171,
                            1497,
                            1684,
                            1732,
                            2022,
                            2268,
                        ],
                        [
                            DamageType.bludgeoning
                        ],
                        level,
                        ItemType.mace)


#################
# Magic Weapons #
#################

class Staff(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Staff",
                        [
                            200,
                            400,
                            600,
                            800,
                            1000,
                            1200,
                            1400,
                            1600,
                            1800,
                            2000
                        ],
                        [ DamageType.force ],
                        level,
                        ItemType.staff)

class Wand(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Wand",
                        [
                            428,
                            436,
                            522,
                            789,
                            1176,
                            1512,
                            1670,
                            1690,
                            1737,
                            1952
                        ],
                        [
                            DamageType.force
                        ],
                        level,
                        ItemType.wand)

class SpellBook(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Spell Book",
                        [
                            482,
                            579,
                            642,
                            762,
                            949,
                            1205,
                            1517,
                            1793,
                            2002,
                            2164
                        ],
                        [
                            DamageType.force
                        ],
                        level,
                        ItemType.spell_book)

class AlchemicalSupplies(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Alchemy Supplies",
                        [
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0,
                            0
                        ],
                        [
                            DamageType.force
                        ],
                        level,
                        ItemType.alchemical_supplies)


################
# Magic Spells #
################

class Fireball(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Fireball",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.fire
                        ],
                        level,
                        ItemType.fire_ball)

class Thunderbolt(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Thunderbolt",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.electricity
                        ],
                        level,
                        ItemType.thunderbolt)


class IceSpike(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Ice Spike",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.cold
                        ],
                        level,
                        ItemType.ice_spike)


class SonicBlast(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Sonic Blast",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.sonic
                        ],
                        level,
                        ItemType.sonic_blast)

class MagicSword(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Magic Sword",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.slashing
                        ],
                        level,
                        ItemType.magic_sword)

class SpearOfLight(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Spear Of Light",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.piercing
                        ],
                        level,
                        ItemType.spear_of_light)

class RockSmash(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Rock Smash",
                        [
                            150,
                            300,
                            450,
                            600,
                            750,
                            900,
                            1050,
                            1200,
                            1350,
                            1500
                        ],
                        [
                            DamageType.bludgeoning
                        ],
                        level,
                        ItemType.rock_smash)


#########
# Bombs #
#########

class FireBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Fire Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.fire
                        ],
                        level,
                        ItemType.fire_bomb)

class FrostBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Frost Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.cold
                        ],
                        level,
                        ItemType.frost_bomb)

class ShockBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Shock Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.electricity
                        ],
                        level,
                        ItemType.shock_bomb)

class AcidBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Acid Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.acid
                        ],
                        level,
                        ItemType.acid_bomb)

class FlashBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Flash Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.sonic
                        ],
                        level,
                        ItemType.flash_bomb)

class SpikeBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Spike Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.piercing
                        ],
                        level,
                        ItemType.spike_bomb)


class GuidedBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Guided Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.precision
                        ],
                        level,
                        ItemType.guided_bomb)

class ConcussionBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self,
                        "Concussion Bomb",
                        [
                            468,
                            681,
                            728,
                            748,
                            908,
                            1244,
                            1631,
                            1897,
                            1982,
                            1991
                        ],
                        [
                            DamageType.bludgeoning
                        ],
                        level,
                        ItemType.concussion_bomb)

#################
# Utility Items #
#################

class Rope(UtilityItem):
    def init(self):
        UtilityItem.init(self, "Rope")

###############
# Armor Items #
###############

class Armor(ArmorItem):
    def init(self, level, unit_class):
        stats = {
                                #   1      2      3      4      5      6      7      8      9     10
            UnitClass.knight:    [18750, 20625, 22500, 24375, 26250, 28125, 30000, 31875, 33750, 35625],
            UnitClass.brawler:   [16875, 18750, 20625, 22500, 24375, 26250, 28125, 30000, 31875, 33750],
            UnitClass.pikeman:   [17812, 19687, 21562, 23437, 25312, 27187, 29062, 30937, 32812, 34687],
            UnitClass.rogue:     [14375, 16250, 18125, 20000, 21875, 23750, 25625, 27500, 29375, 31250],
            UnitClass.sorcerer:  [11250, 13125, 15000, 16875, 18750, 20625, 22500, 24375, 26250, 28125],
            UnitClass.magus:     [10625, 12500, 14375, 16250, 18125, 20000, 21875, 23750, 25625, 27500],
            UnitClass.wizard:    [12187, 14062, 15937, 17812, 19687, 21562, 23437, 25312, 27187, 29062],
            UnitClass.alchemist: [13437, 15312, 17187, 19062, 20937, 22812, 24687, 26562, 28437, 30312]
        }

        ArmorItem.init(self, "Armor", ItemType.armor, level, stats[unit_class][level-1])



