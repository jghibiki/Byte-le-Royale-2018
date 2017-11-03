from game.client import start
from custom_client import CustomClient

import sys

if __name__ == "__main__":

    verbose = False
    if len(sys.argv) > 1 and sys.argv[1] == "--client-verbose":
        print("Client Verbosity: ON")
        verbose = True

    start(CustomClient(verbose), verbose)
