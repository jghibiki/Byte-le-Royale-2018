import random

from game.common.node import Node


class NODE_TYPES:
    monster = 1
    trap = 2
    town = 3
    start = 4

def get_random_node():
    node_type = random.choice([
        NODE_TYPES.monster,
        NODE_TYPES.trap
    ])

    if node_type == NODE_TYPES.monster:
        return MonsterNode.new_node()
    elif node_type == NODE_TYPES.trap:
        return TrapNode.new_node()

def get_node(node_type):
    if node_type == NODE_TYPES.monster:
        return MonsterNode()
    elif node_type == NODE_TYPES.trap:
        return TrapNode()
    elif node_type == NODE_TYPES.town:
        return TownNode()
    elif node_type == NODE_TYPES.start:
        return StartNode()


class StartNode(Node):
    @staticmethod
    def new_node():
        node = StartNode()
        node.init()
        return node

    def get_type(self):
        return NODE_TYPES.start

class TownNode(Node):
    @staticmethod
    def new_node():
        node = TownNode()
        node.init()
        return node

    def get_type(self):
        return NODE_TYPES.town


class MonsterNode(Node):
    @staticmethod
    def new_node():
        node = MonsterNode()
        node.init()
        return node

    def get_type(self):
        return NODE_TYPES.monster


class TrapNode(Node):
    @staticmethod
    def new_node():
        node = TrapNode()
        node.init()
        return node

    def get_type(self):
        return NODE_TYPES.trap


