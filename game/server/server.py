import sys

from broadcast_server import start_server
from custom_server import CustomServer


if __name__ == "__main__":

    server_logic = CustomServer()
    start_server("0.0.0.0", "8080", server_logic)

