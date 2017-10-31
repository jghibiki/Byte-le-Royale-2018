import random
import json

from game.common.node import Node
from game.common.node_types import *
from game.common.trap_types import *
from game.common.monster_types import *

from game.utils.network_visualizer import visualize


###########
# The basic level structure looks something similar to this shape repeated n times based on the level number.
#   a
#  / \
# .....
# b   c   |
# |\ /|   |\
# d e f   |--> This section can be repeated multiple times to produce a longer,
# |/ \|   |/    more difficult level.
# g   h   |
# ......
#  \ /
#   i

LEVELS = 5


def random_room_type(self):
    random.choice([0, 0, 1])


def generate_sections(num, nodes):
    #   a
    #  / \
    # .....
    # b   c
    # |\ /|
    # d e f
    # |/ \|
    # g   h
    # ......
    #  \ /
    #   i

    first_right = get_random_node()
    first_left = get_random_node()

    b = first_right
    c = first_left

    nodes.append([b, c])

    for _ in range(num+1):
        d = get_random_node()
        e = get_random_node()
        f = get_random_node()

        nodes.append([d, e, f])

        b.add_node(d)
        b.add_node(e)

        c.add_node(e)
        c.add_node(f)

        g = get_random_node()

        h = get_random_node()

        d.add_node(g)

        e.add_node(g)
        e.add_node(h)

        f.add_node(h)

        nodes.append([g, h])

        b = g
        c = h


    i = Town.new_node()
    b.add_node(i)
    c.add_node(i)

    nodes.append([i])

    return nodes, first_right, first_left, i

def save(turns):

    serialized_turns = []

    for turn in turns:
        serialized_turn = []
        for node in turn:
            d = node.to_dict()
            serialized_turn.append(d)
        serialized_turns.append(serialized_turn)

    with open("game_data.json", "w") as f:
        json.dump({ "data": serialized_turns }, f, sort_keys=True, indent=4)


def load():
    unserialized_turns = []
    unserialized_nodes = []

    with open("game_data.json", "r") as f:
        data = json.load(f)["data"]

    for turn in data:
        unserialized_turn = []
        for node in turn:
            new_node = get_node(node["node_type"])
            new_node.from_dict(node)
            unserialized_turn.append(new_node)
            unserialized_nodes.append(new_node)
        unserialized_turns.append(unserialized_turn)

    for node in unserialized_nodes:
        node.load_nodes(unserialized_nodes)

    return unserialized_turns


def generate():

    nodes = []
    nodes_per_turn = []

    root = StartRoom.new_node()
    nodes.append(root)
    nodes_per_turn.append([root])

    current = root

    for i in range(LEVELS):

        # generate level
        nodes, right, left, tail = generate_sections(i, nodes_per_turn)

        current.add_node(right)
        current.add_node(left)

        current = tail


    #for turn_node in nodes_per_turn:
    #    print([ n.id[0:5] for n in turn_node ])

    save(nodes_per_turn)
    #visualize(nodes)


