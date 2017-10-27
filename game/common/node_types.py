import random

from game.common.node import Node
from game.common.trap_types import *
from game.common.monster_types import *


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

    def init(self):
        Node.init(self)

        lvl = random.randint(1,5)
        self.monster = get_random_monster()
        self.monster.init(lvl)

    def from_dict(self, d, safe=False):
        Node.from_dict(self, d, safe=safe)

        self.monster = get_monster(d["monster"]["monster_type"])
        self.monster.from_dict(d["monster"])

    def to_dict(self, safe=False):
        data = Node.to_dict(self, safe=safe)

        data["monster"] = self.monster.to_dict()

        return data



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

    def init(self):
        Node.init(self)

        lvl = random.randint(1,5)
        self.trap = get_random_trap()
        self.trap.init(lvl)

    def from_dict(self, d, safe=False):
        Node.from_dict(self, d, safe=safe)

        self.trap = get_trap(d["trap"]["trap_type"])
        self.trap.from_dict(d["trap"])

    def to_dict(self, safe=False):
        data = Node.to_dict(self, safe=safe)

        data["trap"] = self.trap.to_dict()

        return data

