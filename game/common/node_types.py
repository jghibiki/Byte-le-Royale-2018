import random

from game.common.node import Node


class NODE_TYPES:
    monster = 1
    trap = 2

def get_random_node():
    node_type = random.choice([
        NODE_TYPES.monster,
        NODE_TYPES.trap
    ])

    if node_type == NODE_TYPES.monster:
        return MonsterNode.new_node()
    elif node_type == NODE_TYPES.trap:
        return TrapNode.new_node()



class TownNode(Node):
    @staticmethod
    def new_node():
        node = TownNode()
        node.init()
        return node


class MonsterNode(Node):
    @staticmethod
    def new_node():
        node = MonsterNode()
        node.init()
        return node


class TrapNode(Node):
    @staticmethod
    def new_node():
        node = TrapNode()
        node.init()
        return node



