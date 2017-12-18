import click

from game.server import start
from game.client.custom_client import CustomClient


@click.command()
@click.option("--server-verbose", is_flag=True)
@click.option("--server-loop", is_flag=True)
def start_server(server_verbose, server_loop):

    if server_verbose:
        print("Server Verbosity: ON")

    start(server_verbose, server_loop)

if __name__ == "__main__":
    start_server()
