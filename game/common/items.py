from game.common.game_serializable import Serializable


class ItemClass:
    melee= 1
    magic = 2
    spell = 3
    utility = 3


########
# Item #
########

class Item(Serializable):

    def __init__(self):
        self.initialized = False

    def init(self, name, item_class, item_type):

        self.name = name
        self.item_class = item_class
        self.item_type = item_type

        self.initialized = True

    def from_dict(self, d, safe=False):
        Serializable.from_dict(self, d, safe)
        if not safe:
            pass
            # stuff to hide from user
        self.name = d["name"]
        self.item_class = d["item_class"]
        self.item_type = d["item_type"]

    def to_dict(self, safe=False):
        data = Serializable.to_dict(self, safe)
        if not safe:
            pass
            # stuff to hide from user
        data["name"] = self.name
        data["item_class"] = self.item_class
        data["item_type"] = self.item_type

        return data


###############
# Combat Item #
###############

class CombatItem(Item):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage, damage_types, level, item_class, item_type):
        Item.init(self, name, item_class, item_type)

        self.damage = damage
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
        data =  Item.from_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user

        data["damage"] = self.damage
        data["damage_types"] = self.damage_types
        data["level"] = self.level

        return data


###############
# Melee Item #
###############

class MeleeItem(CombatItem):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage, damage_types, level, item_type):
        CombatItem.init(self, name, damage, damage_types, level, ItemClass.melee, item_type)
        self.initialized = True

    def from_dict(self, d, safe=False):
        CombatItem.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user

    def to_dict(self, safe=False):
        data = CombatItem.from_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user
        return data


##############
# Magic Item #
##############

class MagicItem(CombatItem):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage, damage_types, level, item_type):
        CombatItem.init(self, name, damage, damage_types, level, ItemClass.magic, item_type)
        self.initialized = True

    def from_dict(self, d, safe=False):
        CombatItem.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user

    def to_dict(self, safe=False):
        data = CombatItem.from_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user
        return data


##############
# Magic Item #
##############

class MagicSpell(CombatItem):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage, damage_types, level, item_type):
        CombatItem.init(self, name, damage, damage_types, level, ItemClass.spell, item_type)
        self.initialized = True

    def from_dict(self, d, safe=False):
        CombatItem.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user

    def to_dict(self, safe=False):
        data = CombatItem.from_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user
        return data


################
# Utility Item #
################

class UtilityItem(Item):

    def __init__(self):
        self.initialized = False


    def init(self, name, item_class, item_type):
        Item.init(self, name, item_class, item_type)

        self.item_class = ItemClass.utility

        self.initialized = True

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user

        self.item_class = d["item_class"]


    def to_dict(self, safe=False):
        data = Item.to_dict(self, safE)

        if not safe:
            pass
            # stuff to hide from user

        data["name"] = self.name

        return data

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))







