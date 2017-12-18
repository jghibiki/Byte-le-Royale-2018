
import sys

from game.server.broadcast_server import start_server
from game.server.custom_server import CustomServer


def start(verbose=False, server_loop=False):
    server_logic = CustomServer(verbose=verbose, server_loop=server_loop)
    start_server("0.0.0.0", "8080", server_logic, verbose=verbose)
