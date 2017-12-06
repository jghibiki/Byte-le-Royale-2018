from uuid import uuid4
import random

from game.common.game_serializable import Serializable

class Trap(Serializable):
    def __init__(self):
        self.initialized = False


    def init(self, name, level):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name
        self.level = level

        self.initialized = True

    def from_dict(self, d):
        """ Load obj from dict that has been deserialized from json """

        self.id = d["id"]
        self.name = d["name"]
        self.level = d["level"]

        self.initialized = True


    def to_dict(self):
        """ Dump obj data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "trap_type": self.get_type()
        }


    def attempt_clear(self, units):
        raise Exception("{0} missing implementation of attempt_clear()".format(self.__class__.__name__))


    def get_type(self):
        raise Exception("{0} missing implementation of get_type()".format(self.__class__.__name__))

    def get_description(self):
        return "{0}".format(self.name)

