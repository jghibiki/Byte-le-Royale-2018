import random

from game.common.game_serializable import Serializable

class Monster(Serializable):
    def __init__(self):
        self.initialized = False


    def init(self, name, level):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.level = level

        self.attack_state = {}

        self.initialized = True

    def fromDict(self, d):
        """ Load obj from dict that has been deserialized from json """

        self.id = d["id"]
        self.name = d["name"]
        self.level = d["level"]
        self.attack_state = d["attack_state"]

        self.initialized = True


    def toDict(self):
        """ Dump obj data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "attack_state": self.attack_state,
        }



    def attack(self, targets):
        """Define the monster's attack pattern. Default returns the id of the unit or units it is attacking"""

        # default attack pattern - randomly attack any target
        return random.choice(targets).id





