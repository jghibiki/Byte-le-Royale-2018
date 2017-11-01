from game.common.damage import *
from game.common.items import *

class WeaponTypes:
    # melee
    sword = 1
    dagger = 2
    club = 3
    fire_bomb = 4
    acid_bomb = 5

    # magic
    fire_ball = 6
    thunderbolt = 7
    magic_missile = 8
    ice_spike = 9


def get_item(item_class, item_type, level):

    # combat items
    if item_class == ItemClass.combat:
        if item_type == WeaponTypes.sword:
            new_item = Sword()
            new_item.init(level)
            return new_item

    # magic items
    elif item_class == ItemClass.magic:
        pass

    # utility items
    elif item_class == ItemClass.utility:
        pass



################
# Melee Weapon #
################

class Sword(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Sword", 1000, level)

    def get_type(self):
        return WeaponTypes.sword

    def damage_types(self):
        return [
            DAMAGE_TYPE.slashing
        ]
    def damage_rating():
        return

class Dagger(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Dagger", 5000, level)

    def get_type(self):
        return WeaponTypes.dagger

    def damage_types(self):
        return [
            DAMAGE_TYPE.piercing
        ]

class Club(MeleeItem):
    def init(self, level):
        MeleeItem.init(self, "Club", 1000, level)

    def get_type(self):
        return WeaponTypes.club

    def damage_types(self):
        return [
            DAMAGE_TYPE.bludgeoning
        ]

class FireBomb(MeleeItem):
    """more powerful than fireball but more expensive and you have to buy each use"""

    def init(self, level):
        MeleeItem.init(self, "Fire Bomb", 1000, level)

    def get_type(self):
        return WeaponTypes.fire_bomb

    def damage_types(self):
        return [
            DAMAGE_TYPE.fire,
            DAMAGE_TYPE.force
        ]

class AcidBomb(MeleeItem):

    def init(self, level):
        MeleeItem.init(self, "Acid Bomb", 2, level)

    def get_type(self):
        return WeaponTypes.acid_bomb

    def damage_types(self):
        return [
            DAMAGE_TYPE.acid
        ]



class Fireball(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Fireball", 2, level)

    def get_type(self):
        return WeaponTypes.fireball

    def damage_types(self):
        return [
            DAMAGE_TYPE.fire,
            DAMAGE_TYPE.force
        ]

class Thundrbolt(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Thunderbolt", 2, level)

    def get_type(self):
        return WeaponTypes.thunderbolt

    def damage_types(self):
        return [
            DAMAGE_TYPE.electricity
        ]

class MagicMissile(MagicItem):
    def init(self, level):
        MagicItem.init(self, "Magic Missile", 2, level)

    def get_type(self):
        return WeaponTypes.magic_missile

    def damage_types(self):
        return [
            DAMAGE_TYPE.force,
            DAMAGE_TYPE.bludgeoning
        ]

class IceSpike(MagicItem):
    def init(self, level):
        MagicItem.init(self, "", 2, level)

    def get_type(self):
        return WeaponTypes.ice_spike

    def damage_types(self):
        return [
            DAMAGE_TYPE.cold
        ]


#################
# Utility Items #
#################

class UtilityItemTypes:
    rope = 1

class Rope(UtilityItem):
    def init(self):
        UtilityItem.init(self, "Rope")

    def get_type(self):
        return UtilityItemTypes.rope
