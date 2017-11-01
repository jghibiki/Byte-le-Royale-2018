from game.common.game_serializable import Serializable


class ItemClass:
    combat = 1
    magic = 2
    utility = 3


########
# Item #
########

class Item(Serializable):

    def __init__(self):
        self.initialized = False

    def init(self, name):

        self.name = name
        self.initialized = True

    def from_dict(self, d, safe=False):
        Serializable.from_dict(self, d, safe)
        if not safe:
            pass
            # stuff to hide from user
        self.name = d["name"]

    def to_dict(self, safe=False):
        data = Serializable.to_dict(self, safe)
        if not safe:
            pass
            # stuff to hide from user
        data["name"] = self.name
        return data

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))

###############
# Combat Item #
###############

class MeleeItem(Item):

    def __init__(self):
        self.initialized = False

    def init(self, name, damage, level):
        Item.init(self, name)

        self.damage = damage
        self.level = level
        self.item_class = ItemClass.combat

        self.initialized = True

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user
        self.damage = d["damage"]
        self.level = d["level"]


    def to_dict(self, safe=False):
        data =  Item.from_dict(self, safe)

        if not safe:
            pass
            # stuff to hide from user

        data["damage"] = self.damage
        data["level"] = self.level

        return data


    def damage_types(self):
        raise Exception("{0} missing implementation of damage_types(self)".format(self.__class__.__name__))

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))


##############
# Magic Item #
##############

class MagicItem(Item):

    def __init__(self):
        self.initialized = False


    def init(self, name):
        Item.init(self, name)

        self.item_class = ItemClass.magic

        self.initialized = True

    def from_dict(self, d, safe=False):
        Item.from_dict(self, d, safe)

        if not safe:
            pass
            # stuff to hide from user


    def to_dict(self, safe=False):
        data = Item.to_dict(self, safE)

        if not safe:
            pass
            # stuff to hide from user

        return data

    def get_types():
        raise Exception("{0} missing implementation of get_types()".format(self.__class__.__name__))


################
# Utility Item #
################

class UtilityItem(Item):

    def __init__(self):
        self.initialized = False


    def init(self, name):
        Item.init(self, name)

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







