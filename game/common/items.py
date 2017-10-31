from game.common.damage import *
from game.common.game_serializable import Serializable

class CombatItem(Serializable):

    def __init__(self):
        self.initialized = False


    def init(self, name, damage, level):

        self.name = name
        self.damage = damage
        self.level = level

        self.initialized = True

    def from_dict(self, d, safe=False):

        if not safe:
            pass
            # stuff to hide from user

        self.name = d["name"]
        self.damage = d["damage"]
        self.level = d["level"]


    def to_dict(self, safe=False):
        data =  {}

        if not safe:
            pass
            # stuff to hide from user

        data["name"] = self.name
        data["damage"] = self.damage
        data["level"] = self.level

        return data


    def damage_types(self):
        raise Exception("{0} missing implementation of damage_types(self)".format(self.__class__.__name__))

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))


################
# Melee Weapon #
################

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


class MeleeWeapon(CombatItem):
    def init(self, name, damage, level):
        CombatItem.init(self, name, damage, level)

    def from_dict(self, d, safe=False):
        CombatItem.from_dict(self, d, safe)

    def to_dict(self, safe=False):
        return CombatItem.to_dict(self, d, safe)

class Sword(MeleeWeapon):

    def init(self, level):
        MeleeWeapon.init(self, "Sword", 1000, level)

    def get_type(self):
        return WeaponTypes.sword

    def damage_types(self):
        return [
            DAMAGE_TYPE.slashing
        ]
    def damage_rating():
        return

class Dagger(MeleeWeapon):

    def init(self, level):
        MeleeWeapon.init(self, "Dagger", 5000, level)

    def get_type(self):
        return WeaponTypes.dagger

    def damage_types(self):
        return [
            DAMAGE_TYPE.piercing
        ]

class Club(MeleeWeapon):
    def init(self, level):
        MeleeWeapon.init(self, "Club", 1000, level)

    def get_type(self):
        return WeaponTypes.club

    def damage_types(self):
        return [
            DAMAGE_TYPE.bludgeoning
        ]

class FireBomb(MeleeWeapon):
    """more powerful than fireball but more expensive and you have to buy each use"""

    def init(self, level):
        MeleeWeapon.init(self, "Fire Bomb", 1000, level)

    def get_type(self):
        return WeaponTypes.fire_bomb

    def damage_types(self):
        return [
            DAMAGE_TYPE.fire,
            DAMAGE_TYPE.force
        ]

class AcidBomb(MeleeWeapon):

    def init(self, level):
        MeleeWeapon.init(self, "Acid Bomb", 2, level)

    def get_type(self):
        return WeaponTypes.acid_bomb

    def damage_types(self):
        return [
            DAMAGE_TYPE.acid
        ]


################
# Magic Spells #
################

class MagicSpell(CombatItem):

    def init(self, name, damage, level):
        CombatItem.init(self, name, damage, level)

    def from_dict(self, d, safe=False):
        CombatItem.from_dict(self, d, safe)

    def to_dict(self, safe=False):
        return CombatItem.to_dict(self, d, safe)

class Fireball(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Fireball", 2, level)

    def get_type(self):
        return WeaponTypes.fireball

    def damage_types(self):
        return [
            DAMAGE_TYPE.fire,
            DAMAGE_TYPE.force
        ]

class Thundrbolt(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Thunderbolt", 2, level)

    def get_type(self):
        return WeaponTypes.thunderbolt

    def damage_types(self):
        return [
            DAMAGE_TYPE.electricity
        ]

class MagicMissile(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "Magic Missile", 2, level)

    def get_type(self):
        return WeaponTypes.magic_missile

    def damage_types(self):
        return [
            DAMAGE_TYPE.force,
            DAMAGE_TYPE.bludgeoning
        ]

class IceSpike(MagicSpell):
    def init(self, level):
        MagicSpell.init(self, "", 2, level)

    def get_type(self):
        return WeaponTypes.ice_spike

    def damage_types(self):
        return [
            DAMAGE_TYPE.cold
        ]

