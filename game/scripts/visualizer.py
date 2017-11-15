from game.visualizer import start

import sys

if __name__ == "__main__":

    verbose = False
    if len(sys.argv) > 1 and sys.argv[1] == "--visualizer-verbose":
        print("Visualizer Verbosity: ON")
        verbose = True

    start(verbose)
