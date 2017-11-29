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


    def init(self, name, class_name, unit_class, max_health, primary_weapon_type):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.class_name = class_name
        self.unit_class = unit_class

        self.health = max_health
        self.current_health = self.health

        self.combat_action = CombatAction.none
        self.combat_action_target_1 = None
        self.combat_action_target_2 = None

        self.invigorated = False

        self.primary_weapon = get_item(primary_weapon_type, 1)

        self.initialized = True

    def from_dict(self, d, safe=False):
        """ Load obj from dict that has been deserialized from json """

        if not safe:
            # values that should not be exposed to user
            self.current_health = d["current_health"]

        # these values should have matching properties on game.safe.user.
        self.id = d["id"]
        self.name = d["name"]

        self.class_name = d["class_name"]
        self.unit_class = d["unit_class"]

        self.combat_action = d["combat_action"]
        self.combat_action_target_1 = d["combat_action_target_1"]
        self.combat_action_target_2 = d["combat_action_target_2"]

        self.invigorated = d["invigorated"]

        self.health = d["health"]

        self.primary_weapon = load_item(
            d["primary_weapon"][0],
            d["primary_weapon"][1])

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
        data["unit_class"] =  self.unit_class

        data["combat_action"] = self.combat_action
        data["combat_action_target_1"] = self.combat_action_target_1
        data["combat_action_target_2"] = self.combat_action_target_2

        data["invigorated"] = self.invigorated

        data["health"] = self.health
        data["current_health"] = self.current_health

        data["primary_weapon"] = [
            self.primary_weapon.item_type,
            self.primary_weapon.to_dict()
        ]


        return data

    def summary(self):
        percent_health = self.current_health / float(self.health)
        bar_size = 50
        percent_bar = math.floor( bar_size * percent_health)

        out = "{0}:".format(self.name).rjust(15)

        out += "({0:04d}/{1:04d})[{2}]".format(
                self.current_health,
                self.health,
                ("="*percent_bar).ljust(bar_size, " ")).rjust(65)

        return out

    def reset_health(self):
        self.current_health = self.health

    def _special_ability(self):
        raise Exception("{0} missing implementation of _special_ability()".format(self.__class__.__name__))



    ## PUBLIC Methods

    def special_ability(self):
        self.current_combat_action = CombatAction.special_ability

    def attack(self):
        self.current_combat_action = CombatAction.primary_weapon

    def wait(self):
        self.current_combat_action = CombatAction.wait

    def is_alive(self):
        return self.current_health > 0




