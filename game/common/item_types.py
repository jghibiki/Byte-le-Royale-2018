from game.common.items import *
from game.common.enums import *


def get_item(item_type, level, init=False):

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
    elif item_type == ItemType.fireball:
        new_item = Fireball()
    elif item_type == ItemType.thunderbolt:
        new_item = Thunderbolt()
    elif item_type == ItemType.ice_spike:
        new_item = Thunderbolt()

    else:
        raise Exception("Invalid item type: {0}".format(item_type))

    new_item.init(level)
    return new_item

def load_item(item_type, data):

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
    elif item_type == ItemType.fireball:
        new_item = Fireball()
    elif item_type == ItemType.thunderbolt:
        new_item = Thunderbolt()
    elif item_type == ItemType.ice_spike:
        new_item = Thunderbolt()

    # utility items

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
        CombatItem.init(self, "Alchemical Supplies", 0, [ DamageType.force ], level, ItemType.alchemical_supplies)


################
# Magic Spells #
################

class Fireball(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Fireball", 100, [ DamageType.fire ], level)

class Thundrbolt(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Thunderbolt", 100, [ DamageType.electricity ], level)


class IceSpike(CombatItem):
    def init(self, level):
        CombatItem.init(self, "Ice Spike", 100, [ DamageType.cold ], level)



#################
# Utility Items #
#################

class Rope(UtilityItem):
    def init(self):
        UtilityItem.init(self, "Rope")

