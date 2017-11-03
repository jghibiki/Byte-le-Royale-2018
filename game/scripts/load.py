from game.common.node_types import *
from game.utils.network_visualizer import visualize
from game.utils.generate_game import load


nodes = load()

visualize(nodes)
