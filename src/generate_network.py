from src.Node import Node
from src.propagate_layers import propagate_layers
from src.stitch_network import stitch_network
from src.network_object import NetworkObject


def __init__():
    print("")


# Generates and stitches unpopulated network
def generate_network(input_num, output_num, depth):
    network = NetworkObject()
    network.input_num = input_num
    network.output_num = output_num
    network.depth = depth
    for i in range(input_num):
        network.input_node_array.append(Node)
    for i in range(output_num):
        network.output_node_array.append(Node)
        network.input_layers = input_num + depth
        network.output_layers = output_num + depth
    network = propagate_layers(network)
    print(f"First layer {network.input_node_array}")
    print(f"Second layer {network.nodes[0]}")
    network = stitch_network(network)

    return network
