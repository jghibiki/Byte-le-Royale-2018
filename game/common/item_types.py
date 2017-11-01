from game.common.damage import *
from game.common.items import *

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

def get_item(item_class, item_type, level, init=False):

    # melee items
    if item_class == ItemClass.melee:
        if item_type == ItemType.sword:
            new_item = Sword()
        elif item_type == ItemType.dagger:
            new_item = Dagger()
        elif item_type == ItemType.mace:
            new_item = Mace()
        elif item_type == ItemType.spear:
            new_item = Spear()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))

    # magic items
    elif item_class == ItemClass.magic:
        if item_type == ItemType.staff:
            new_item = Staff()
        elif item_type == ItemType.wand:
            new_item = Wand()
        elif item_type == ItemType.spell_book:
            new_item = SpellBook()
        elif item_type == ItemType.alchemical_supplies:
            new_item = AlchemicalSupplies()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))

    # magic spells
    elif item_class == ItemClass.spell:
        if item_type == ItemType.fireball:
            new_item = Fireball()
        elif item_type == ItemType.thunderbolt:
            new_item = Thunderbolt()
        elif item_type == ItemType.ice_spike:
            new_item = Thunderbolt()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))


    # utility items
    elif item_class == ItemClass.utility:
        pass

    else:
        raise Exception("Invalid item class: {0}".format(item_class))

    new_item.init(level)
    return new_item

def load_item(item_class, item_type, data):

    # combat items
    if item_class == ItemClass.melee:
        if item_type == ItemType.sword:
            new_item = Sword()
        elif item_type == ItemType.dagger:
            new_item = Dagger()
        elif item_type == ItemType.mace:
            new_item = Mace()
        elif item_type == ItemType.mace:
            new_item = Mace()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))

    # magic items
    elif item_class == ItemClass.magic:
        if item_type == ItemType.staff:
            new_item = Staff()
        elif item_type == ItemType.wand:
            new_item = Wand()
        elif item_type == ItemType.spell_book:
            new_item = SpellBook()
        elif item_type == ItemType.alchemical_supplies:
            new_item = AlchemicalSupplies()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))

    elif item_class == ItemClass.spell:
        if item_type == ItemType.fireball:
            new_item = Fireball()
        elif item_type == ItemType.thunderbolt:
            new_item = Thunderbolt()
        elif item_type == ItemType.ice_spike:
            new_item = Thunderbolt()
        else:
            raise Exception("Invalid item type: {0}".format(item_type))

    # utility items
    elif item_class == ItemClass.utility:
        pass

    else:
        raise Exception("Invalid item class: {0}".format(item_class))

    new_item.from_dict(data)
    return new_item

################
# Melee Weapon #
################

class Sword(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Sword", 100, [ DamageType.slashing ],  level, ItemType.sword)

class Dagger(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Dagger", 100, [DamageType.percing, DamageType.slashing ], level, ItemType.dagger)

class Spear(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Spear", 100, [ DamageType.piercing ], level, ItemType.spear)

class Mace(MeleeItem):
    def init(self, level):
        MeleeItem.init(self, "Club", 100, [ DamageType.bludgeoning ], level, ItemType.mace)


#################
# Magic Weapons #
#################

class Staff(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Staff", 100, [ DamageType.force ], level, ItemType.staff)

class Wand(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Wand", 100, [ DamageType.force ], level, ItemType.wand)

class SpellBook(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Spell Book", 100, [ DamageType.force], level, ItemType.spell_book)

class AlchemicalSupplies(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Alchemical Supplies", 100, [ DamageType.force ], level, ItemType.alchemical_supplies)


################
# Magic Spells #
################

class Fireball(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Fireball", 100, [ DamageType.fire ], level)

class Thundrbolt(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Thunderbolt", 100, [ DamageType.electricity ], level)


class IceSpike(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Ice Spike", 100, [ DamageType.cold ], level)



#################
# Utility Items #
#################

class Rope(UtilityItem):
    def init(self):
        UtilityItem.init(self, "Rope")

