import math

from game.common.game_serializable import Serializable
from game.common.enums import *


########
# Item #
########

class Item(Serializable):

    def __init__(self):
        self.initialized = False

    def init(self, name, item_type):

        self.name = name
        self.item_type = item_type

        self.initialized = True

    def from_dict(self, d, safe=False):
        if not safe:
            pass
            # stuff to hide from user
        self.name = d["name"]
        self.item_type = d["item_type"]

    def to_dict(self, safe=False):
        data = {}

        if not safe:
            pass
            # stuff to hide from user
        data["name"] = self.name
        data["item_type"] = self.item_type

        return data


###############
# Combat Item #
###############

class CombatItem(Item):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage_table, damage_types, level, item_type, damage_scale=0.5):
        Item.init(self, name, item_type)

        self.damage = damage_table[level-1]
        self.damage_types = damage_types
        self.level = level

        self.initialized = True

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user
        self.damage = d["damage"]
        self.damage_types = d["damage_types"]
        self.level = d["level"]


    def to_dict(self, safe=False):
        data =  Item.to_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user

        data["damage"] = self.damage
        data["damage_types"] = self.damage_types
        data["level"] = self.level

        return data



################
# Utility Item #
################

class UtilityItem(Item):

    def __init__(self):
        self.initialized = False


    def init(self, name, item_type):
        Item.init(self, name, item_type)

        self.initialized = True

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user


    def to_dict(self, safe=False):
        data = Item.to_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user

        data["name"] = self.name

        return data

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))




##############
# Armor Item #
##############


class ArmorItem(Item):

    def __init__(self):
        super().__init__()
        self.initialized = False


    def init(self, name, item_type, level, health):
        Item.init(self, name, item_type)

        self.initialized = True
        self.health = health

        self.level = level

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        self.level = d["level"]
        self.health = d["health"]



    def to_dict(self, safe=False):
        data = Item.to_dict(self, safe)

        data["name"] = self.name
        data["level"] = self.level
        data["health"] = self.health

        return data


