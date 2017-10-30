import random
from uuid import uuid4

from game.common.game_serializable import Serializable

class Monster(Serializable):
    def __init__(self):
        self.initialized = False


    def init(self, name, level):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.level = level
        self.damage = 5
        self.health = 5

        self.attack_state = {}

        self.initialized = True

    def from_dict(self, d, safe=False):
        """ Load obj from dict that has been deserialized from json """

        if not safe:
            # variables that should be hidden from user
            pass

        self.id = d["id"]
        self.name = d["name"]
        self.level = d["level"]
        self.damage = d["damage"]
        self.health = d["health"]
        self.attack_state = d["attack_state"]

        self.initialized = True


    def to_dict(self, safe=False):
        """ Dump obj data to a dict to prepare it for json serialization. """
        data =  {}

        if not safe:
            # variables that should be hidden from user
            pass

        data["id"] = self.id
        data["name"] = self.name
        data["level"] = self.level
        data["damage"] = self.damage
        data["health"] = self.health
        data["attack_state"] = self.attack_state

        data["monster_type"] = self.get_type()

        return data


    def attack(self, targets):
        """Define the monster's attack pattern. Default returns the id of the unit or units it is attacking"""

        # default attack pattern - randomly attack any target
        return random.choice(targets).id

    def get_type(self):
        raise Exception("{0} missing implementation of get_type()".format(self.__class__.__name__))

    def get_description(self):
        return "{0}(Level {1})".format(self.name, self.level)




