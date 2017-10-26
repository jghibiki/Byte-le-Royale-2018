
import random

from game.common.game_serializable import Serializable

class Trap(Serializable):
    def __init__(self):
        self.initialized = False


    def init(self, _type, level):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.type = _type
        self.level = level

        self.initialized = True

    def from_dict(self, d):
        """ Load obj from dict that has been deserialized from json """

        self.id = d["id"]
        self.type = d["type"]
        self.level = d["level"]

        self.initialized = True


    def to_dict(self):
        """ Dump obj data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "type": self.name,
            "level": self.level
        }


    def attempt_clear(self, units):
        raise Exception("{0} missing implementation of attempt_clear()".format(self.__class__.__name__))

