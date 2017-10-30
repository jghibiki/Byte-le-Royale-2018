from game.common.node_types import *
from game.utils.network_visualizer import visualize
from game.utils.generate_game import load


turns = load()

num_turns = len(turns)

current_turn = turns.pop(0)
current_node = current_turn[0]

monsters_faced = 0
traps_faced = 0

i = 1

while i<num_turns-2:
    print()
    print("#"*10)
    print("Turn: {}".format(i))
    print("#"*10)

    # handle current room

    if isinstance(current_node, Town):

        print("Town")
        print("Press Enter to continue...")
        input()

    elif isinstance(current_node, MonsterRoom):
        monsters_faced += 1
        print("Combat against {}".format(current_node.monster.get_description()))
        print("Press enter to continue")
        input()

    elif isinstance(current_node, TrapRoom):
        traps_faced += 1
        print("Navgating trap {}".format(current_node.trap.get_description()))
        print("Press enter to continue")
        input()


    # Decision time

    if len(current_node.nodes) == 1:
        s = None
        while s != "f":
            print()
            print("You see a door.")
            print("f: {}".format(current_node.nodes[0].get_description()))
            s = input("Direction: ")
        current_node = current_node.nodes[0]

    elif len(current_node.nodes) == 2:
        sides = ["l", "r"]

        s = None
        while s not in sides:
            print()
            print("You see two doors.")
            for side, node in zip(sides, current_node.nodes):
                print("{}: {}".format(side, node.get_description()))
            s = input("Direction: ")

        current_node = current_node.nodes[sides.index(s)]

    i += 1

print()
print("#"*20)
print("End of Run")
print("#"*20)
print("{} Monsters Killed".format(monsters_faced))
print("{} Traps Evaded".format(traps_faced))


