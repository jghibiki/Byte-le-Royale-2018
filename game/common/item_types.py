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
        new_item = Thunderbolt()

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
                                #   1       2      3      4      5      6      7      8      9     10
            UnitClass.knight:    [ 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000],
            UnitClass.brawler:   [ 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000],
            UnitClass.pikeman:   [ 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000],
            UnitClass.rogue:     [ 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000],
            UnitClass.sorcerer:  [ 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000],
            UnitClass.magus:     [ 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000],
            UnitClass.wizard:    [ 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000],
            UnitClass.alchemist: [ 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000]
        }

        ArmorItem.init(self, "Armor", ItemType.armor, level, stats[unit_class][level-1])



