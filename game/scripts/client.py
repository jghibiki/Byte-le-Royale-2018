from game.client import start
from game.client.client_logic import ClientLogic
from custom_client import CustomClient

import sys

if __name__ == "__main__":

    verbose = False
    if len(sys.argv) > 1 and sys.argv[1] == "--client-verbose":
        print("Client Verbosity: ON")
        verbose = True

    start(ClientLogic(verbose, CustomClient()), verbose)
