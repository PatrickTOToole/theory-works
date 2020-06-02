from src import node, stitch_network, propagate_layers, network_object


def __init__():
    print("")


# Generates and stitches unpopulated network
def generate_network(input_num, output_num, depth):
    network = network_object()
    network.input_num = input_num
    network.output_num = output_num
    network.depth = depth
    for i in range(input_num):
        network.input_node_array.append(node())
    for i in range(output_num):
        network.output_node_array.append(node())
        network.input_layers = input_num + depth
        network.output_layers = output_num + depth
    network.layers = propagate_layers(network)
    network.tree = stitch_network(network)
    return network;