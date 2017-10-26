from uuid import uuid4

from game.common.game_serializable import Serializable
from game.safe.unit import Unit as ClientUnit


class Unit(Serializable):
    def __init__(self):
        self.initialized = False


    def init(self, name):
        """Manually initialize obj"""

        self.id = str(uuid4())
        self.name = name

        self.initialized = True

    def fromDict(self, d, safe=False):
        """ Load obj from dict that has been deserialized from json """

        if not safe:
            # values that should not be exposed to user
            pass

        # these values should have matching properties on game.safe.user.
        self.id = d["id"]
        self.name = d["name"]


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

        return data

