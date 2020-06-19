from src.propagate_layers import propagate_layers
from src.stitch_network import stitch_network
from src.classes import NetworkObject


def __init__():
    print("")


# Generates and stitches unpopulated network
def generate_network(input_num, output_num, depth):
    network = NetworkObject()
    network.input_num = input_num
    network.output_num = output_num
    network.depth = depth
    network.input_layers = input_num + depth
    network.output_layers = output_num + depth
    network = propagate_layers(network)
    network = stitch_network(network)

    return network
