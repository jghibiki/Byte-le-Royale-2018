import math

from uuid import uuid4

from game.common.game_serializable import Serializable
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


    def init(self, name):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.damage = 500
        self.cumulative_damage = 0
        self.defense = 0
        self.health = 5000
        self.current_health = self.health

        self.items = []

        self.initialized = True

    def fromDict(self, d, safe=False):
        """ Load obj from dict that has been deserialized from json """

        if not safe:
            # values that should not be exposed to user
            pass

        # these values should have matching properties on game.safe.user.
        self.id = d["id"]
        self.name = d["name"]

        self.damage = d["damage"]
        self.defense = d["defense"]
        self.cumulative_damage = d["cumulative_damage"]
        self.health = d["health"]
        self.current_health = d["current_health"]

        self.items = d["items"]

        self.initialized = True


    def toDict(self, safe=False):
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

        data["attack"] = self.attack
        data["defense"] = self.defense
        data["cumulative_damage"] = self.cumulative_damage
        data["health"] = self.health

        data["items"] = self.items #TODO: serialize items

        return data

    def summary(self):
        percent_health = self.current_health / float(self.health)
        bar_size = 8
        percent_bar = math.floor( bar_size * percent_health)


        out = "{0}: ({1:04d}/{2:04d})[{3}]".format(
                self.name,
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






