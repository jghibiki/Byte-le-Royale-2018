from game.server import start
from game.client.custom_client import CustomClient

import sys

if __name__ == "__main__":

    verbose = False
    if len(sys.argv) > 1 and sys.argv[1] == "--server-verbose":
        print("Server Verbosity: ON")
        verbose = True

    start(verbose)
