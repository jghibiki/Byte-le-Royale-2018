
from game.common.game_serializable import Serializable

class Unit(Serializable):
    """
    A version of the unit that can be exposed to players.

    """
    def __init__(self):
        self.initialized = False

    def init(self, id,  name):
        """Manually initialize obj"""

        self.id = id
        self.name = name


    def load(self, d):
        """
        Loads data from dict into obj
        """
        self.id = d["id"]
        self.name = d["name"]

        self.initialized = True


    def toDict(self):
        """
        Dumps data from obj into dict
        """
        return {
            "id": self.id,
            "name": self.name
        }


