from game.common.game_serializable import Serializable

class Node(Serializable):

    def __init__(self):
        self.initialized = False


    def init(self):
        """Manually initialize node"""

        self.id = str(uuid4())
        self.initialized = True
        self.left = None
        self.right = None

    def fromDict(self, d):
        """ Load node from dict that has been deserialized from json """

        self.id = d["id"]

        self.left = d["left"]
        self.right = d["right"]

        self.initialized = True


    def toDict(self):
        """ Dump node data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "left": self.left,
            "right": self.right
        }
