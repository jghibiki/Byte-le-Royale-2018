import sys

from broadcast_client import start_client
from custom_client import CustomClient


if __name__ == "__main__":

    client_logic = CustomClient()
    start_client("127.0.0.1", "8080", client_logic)

