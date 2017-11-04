import math

from uuid import uuid4

from game.common.game_serializable import Serializable
from game.common.item_types import *
from game.safe.unit import Unit as ClientUnit


class Unit(Serializable):
    def __init__(self):
        self.initialized = False
        self.name = "Unammed"

    def __repr__(self):
        return "<{0} is a {1}.{2} at {3}>".format(
                self.name,
                self.__class__.__module__,
                self.__class__.__name__,
                hex(id(self)) )

    __str__ = __repr__


    def init(self, name, class_name,  max_health, primary_weapon_types):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.class_name = class_name

        self.health = max_health
        self.current_health = self.health

        self.items = [
            get_item(*primary_weapon_types, 1)
        ]

        self.initialized = True

    def from_dict(self, d, safe=False):
        """ Load obj from dict that has been deserialized from json """

        if not safe:
            # values that should not be exposed to user
            pass

        # these values should have matching properties on game.safe.user.
        self.id = d["id"]
        self.name = d["name"]

        self.class_name = d["class_name"]

        self.health = d["health"]
        self.current_health = d["current_health"]

        # load items
        self.items = []
        for item in d["items"]:
            i = load_item(item[0], item[1], item[2])
            self.items.append(item)




        self.initialized = True


    def to_dict(self, safe=False):
        """
        Dump obj data to a dict to prepare it for json serialization.

        The `safe` flag toggles safe mode. Safe mode

        """

        data = {}

        if not safe:
            # values that should not be exposed to user
            pass

        # these values should have matching properties on game.safe.user.
        data["id"] = self.id
        data["name"] =  self.name
        data["class_name"] =  self.class_name

        data["health"] = self.health

        data["items"] = []
        for item in self.items:
            i = [ item.item_class, item.item_type, item.to_dict() ]

        return data

    def summary(self):
        percent_health = self.current_health / float(self.health)
        bar_size = 50
        percent_bar = math.floor( bar_size * percent_health)


        out = "{0}({1}): ({2:04d}/{3:04d})[{4}]".format(
                self.name,
                self.class_name,
                self.current_health,
                self.health,
                ("="*percent_bar).ljust(bar_size, " "))

        return out

    def is_alive(self):
        return self.current_health > 0

    def select_combat_action(self, target):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None

    def reset_health(self):
        self.current_health = self.health






