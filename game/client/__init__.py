import sys

from game.client.broadcast_client import start_client
from game.client.custom_client import CustomClient

def start(client):
    start_client("127.0.0.1", "8080", client)

