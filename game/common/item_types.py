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
        CombatItem.init(self, "Sword", 100, [ DamageType.slashing ],  level, ItemType.sword)

class Dagger(CombatItem):

    def init(self, level):
        CombatItem.init(self, "Dagger", 100, [DamageType.piercing, DamageType.slashing ], level, ItemType.dagger)

class Spear(CombatItem):

    def init(self, level):
        CombatItem.init(self, "Spear", 100, [ DamageType.piercing ], level, ItemType.spear)

class Mace(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Club", 100, [ DamageType.bludgeoning ], level, ItemType.mace)


#################
# Magic Weapons #
#################

class Staff(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Staff", 100, [ DamageType.force ], level, ItemType.staff)

class Wand(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Wand", 100, [ DamageType.force ], level, ItemType.wand)

class SpellBook(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Spell Book", 100, [ DamageType.force], level, ItemType.spell_book)

class AlchemicalSupplies(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Alchemy Supplies", 0, [ DamageType.force ], level, ItemType.alchemical_supplies)


################
# Magic Spells #
################

class Fireball(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Fireball", 100, [ DamageType.fire ], level, ItemType.fire_ball)

class Thunderbolt(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Thunderbolt", 100, [ DamageType.electricity ], level, ItemType.thunderbolt)


class IceSpike(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Ice Spike", 100, [ DamageType.cold ], level, ItemType.ice_spike)


#########
# Bombs #
#########

class FireBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Fire Bomb", 100, [ DamageType.fire ], level, ItemType.fire_bomb)

class FrostBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Frost Bomb", 100, [ DamageType.cold ], level, ItemType.frost_bomb)

class ShockBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Shock Bomb", 100, [ DamageType.electricity ], level, ItemType.shock_bomb)

class AcidBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Acid Bomb", 100, [ DamageType.acid ], level, ItemType.acid_bomb)

class FlashBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Flash Bomb", 100, [ DamageType.sonic ], level, ItemType.flash_bomb)

class SpikeBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Spike Bomb", 100, [ DamageType.piercing ], level, ItemType.spike_bomb)

class ConcussionBomb(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Concussion Bomb", 100, [ DamageType.bludgeoning ], level, ItemType.concussion_bomb)

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

        ArmorItem.init(self, "Armor", ItemType.armor, level, stats[unit_class][level])


