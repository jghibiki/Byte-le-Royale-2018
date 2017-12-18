import importlib
import click

from game.client import start
from game.client.client_logic import ClientLogic
#from custom_client import CustomClient


@click.command()
@click.option("--client-verbose", is_flag=True)
@click.option("--client", default="custom_client")
def start_client(client_verbose, client):

    if client_verbose:
        print("Client Verbosity: ON")

    mod = importlib.import_module(client)

    start(ClientLogic(client_verbose, mod.CustomClient()), client_verbose)

if __name__ == "__main__":
    start_client()
