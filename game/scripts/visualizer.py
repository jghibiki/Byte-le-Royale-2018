import sys

from game.visualizer import start

import click

@click.command()
@click.option("--verbose", is_flag=True)
@click.option("--log-path", default="./game_log")
@click.option("--gamma", default=1.0)
def start_visualizer(verbose, log_path, gamma):

    start(verbose, log_path, gamma)

if __name__ == "__main__":

    start_visualizer()
