import random

from game.common.node import Node
from game.common.trap_types import *
from game.common.monster_types import *
from game.common.enums import *


def weighted_choice(dist):
    total = sum(dist)
    r = random.uniform(0, total)
    upto = 0
    for i, w in enumerate(dist):
        if upto + w >= r:
            return i
        upto += w


def difficulty_distribution(level):

    dist = [1.0, 0.0, 0.0]

    if level is 1:
        dist = [ 0.75, 0.20, 0.5 ]
    if level is 2:
        dist = [ 0.75, 0.20, 0.5 ]
    if level is 3:
        dist = [ 0.75, 0.20, 0.5 ]

    # little harder
    if level is 4:
        dist = [ 0.75, 0.13, 0.12 ]
    if level is 5:
        dist = [ 0.75, 0.13, 0.12 ]
    if level is 6:
        dist = [ 0.75, 0.13, 0.12 ]

    # harder
    if level is 7:
        dist = [ 0.50, 0.25, 0.25 ]
    if level is 8:
        dist = [ 0.50, 0.25, 0.25 ]
    if level is 9:
        dist = [ 0.50, 0.25, 0.25 ]

    # even harder
    if level is 9:
        dist = [ 0.34, 0.33, 0.33 ]
    if level is 10:
        dist = [ 0.34, 0.33, 0.35 ]
    if level is 11:
        dist = [ 0.34, 0.33, 0.33 ]

    if level > 11:
        dist = [ 0.34, 0.33, 0.33 ]

    w = weighted_choice(dist)
    return w + level



def get_random_node(level):
    node_type = random.choice([
        NodeType.monster,
        NodeType.trap
    ])

    if node_type == NodeType.monster:
        return MonsterRoom.new_node(level)
    elif node_type == NodeType.trap:
        return TrapRoom.new_node(level)

def get_node(node_type):
    if node_type == NodeType.monster:
        return MonsterRoom()
    elif node_type == NodeType.trap:
        return TrapRoom()
    elif node_type == NodeType.town:
        return Town()
    elif node_type == NodeType.start:
        return StartRoom()
    elif node_type == NodeType.end:
        return EndRoom()


class StartRoom(Node):
    @staticmethod
    def new_node():
        node = StartRoom()
        node.init()
        return node

    def __init__(self):
        Node.__init__(self, NodeType.start)

    def get_description(self):
        return "Start Room"

    def init(self):
        Node.init(self)
        self.resolved = True #always resolved so we move on immediately

class EndRoom(Node):
    @staticmethod
    def new_node():
        node = EndRoom()
        node.init()
        return node

    def __init__(self):
        Node.__init__(self, NodeType.end)

    def get_description(self):
        return "End Room"

    def init(self):
        Node.init(self)
        self.resolved = True #always resolved so we move on immediately


class Town(Node):
    @staticmethod
    def new_node():
        node = Town()
        node.init()
        return node

    def __init__(self):
        Node.__init__(self, NodeType.town)

    def get_description(self):
        return "You see a town"


class MonsterRoom(Node):
    @staticmethod
    def new_node(level):
        node = MonsterRoom()
        node.init(level)
        return node

    def __init__(self):
        Node.__init__(self, NodeType.monster)

    def init(self, level):
        Node.init(self)

        self.monster = get_random_monster( difficulty_distribution(level) )
        self.monster.init(level)

    def from_dict(self, d, safe=False):
        Node.from_dict(self, d, safe=safe)

        self.monster = get_monster(d["monster"]["monster_type"])
        self.monster.from_dict(d["monster"])

    def to_dict(self, safe=False):
        data = Node.to_dict(self, safe=safe)

        data["monster"] = self.monster.to_dict()

        return data

    def get_description(self):
        return "A {} stands guard.".format(self.monster.get_description())



class TrapRoom(Node):
    @staticmethod
    def new_node(level):
        node = TrapRoom()
        node.init(level)
        return node

    def __init__(self):
        Node.__init__(self, NodeType.trap)

    def init(self, level):
        Node.init(self)

        self.trap = get_random_trap()
        self.trap.init( difficulty_distribution(level) )

    def from_dict(self, d, safe=False):
        Node.from_dict(self, d, safe=safe)

        self.trap = get_trap(d["trap"]["trap_type"])
        self.trap.from_dict(d["trap"])

    def to_dict(self, safe=False):
        data = Node.to_dict(self, safe=safe)

        data["trap"] = self.trap.to_dict()

        return data

    def get_description(self):
        return "A {} spans the room.".format(self.trap.get_description())

