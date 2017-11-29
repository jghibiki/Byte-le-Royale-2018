from uuid import uuid4

from game.common.game_serializable import Serializable

class Node(Serializable):

    @staticmethod
    def new_node():
        n = Node()
        n.init()
        return n

    def __init__(self, node_type):
        self.initialized = False
        self.node_type = node_type


    def init(self):
        """Manually initialize node"""

        self.id = str(uuid4())
        self.initialized = True
        self.nodes = []
        self.node_ids = []
        self.resolved = False

    def from_dict(self, d, safe=False):
        """ Load node from dict that has been deserialized from json """

        self.id = d["id"]
        self.node_ids = d["node_ids"]
        self.resolved = d["resolved"]
        self.nodes = []

        self.initialized = True


    def to_dict(self, safe=False):
        """ Dump node data to a dict to prepare it for json serialization. """
        return {
            "id": self.id,
            "node_ids": self.node_ids,
            "node_type": self.node_type,
            "resolved": self.resolved
        }

    def load_nodes(self, node_list):
        self.nodes = [ None for _ in range(len(self.node_ids)) ]
        for n in node_list:
            for idx, n_id in enumerate(self.node_ids):
                if n.id == n_id:
                    self.nodes[idx] = n
                    break


    def add_node(self, node):
        self.nodes.append(node)
        self.node_ids.append(node.id)

    def get_description(self):
        raise Exception("{0} missing implementation of get_description()".format(self.__class__.__name__))




