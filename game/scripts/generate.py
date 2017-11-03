from game.utils.generate_game import generate

import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        generate(num)
    else:
        generate()

