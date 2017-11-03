from game.common.node_types import *

def draw_child(node, indent_level=0):
    if node is not None:
        print("{0}+-{1}".format("| "*indent_level, node.id[0:5]))

        if len(node.node_ids) == 2:
            draw_child(node.nodes[0], indent_level+1)
            draw_child(node.nodes[1], indent_level+1)
        elif len(node.node_ids) == 1:
            draw_child(node.nodes[0], indent_level+1)


def draw_subtree(turns, formatter=None, first=False, last=False):
    if not formatter: formatter = lambda t: t.id[0:5]

    turn_no = 0

    for turn_no in range(len(turns)):
        turn = turns[turn_no]

        if len(turn) == 1:
            print("      {0}      ".format(
                formatter(turn[0]) ))
            if not last:
                print("        |")
                print("  +------------+")
                print("  |            |")

        elif len(turn) == 2:
            print("{0}        {1}".format(
                formatter(turn[0]) ,
                formatter(turn[1]) ))

            print("  |            |")

            if turn_no < len(turns) and len(turns[turn_no + 1]) == 1 :
                print("  +-----+------+")
                print("        |       ")
            else:
                print("  +----+ +-----+")
                print("  |    | |     |")

        elif len(turn) == 3:
            print("{0} {1}  {2}".format(
                formatter(turn[0]) ,
                formatter(turn[1]) ,
                formatter(turn[2]) ))
            print("  |    | |     |")
            print("  +----+ +-----+")
            print("  |            |")



        if turn_no < len(turns)-2 :
            turn_no += 1
        elif turn_no < len(turns)-1 :
            turn_no += 1
            last = True



def visualize(turns):

    #draw_child(node_list[0])

    draw_subtree(turns, 0, first=True)

    print()
    print("-"*20)
    print()

    def convert(t):
        if isinstance(t, MonsterRoom):
            return ("  M  ")
        elif isinstance(t, TrapRoom):
            return ("  T  ")
        elif isinstance(t, Town):
            return ("  R  ")
        elif isinstance(t, EndRoom):
            return ("  E  ")
        elif isinstance(t, StartRoom):
            return ("  S  ")
        else:
            return ("  o  ")

    draw_subtree(turns, formatter=convert, first=True)







