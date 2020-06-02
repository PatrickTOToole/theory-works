from src import output_node, input_node, stitch_network, propagate_layers, network_object


def __init__():
    print("")


def generate_network(input_num, output_num, depth):
    network = network_object()
    network.input_num = input_num
    network.output_num = output_num
    network.depth = depth
    for i in range(input_num):
        network.input_node_array.append(input_node())
    for i in range(output_num):
        network.output_node_array.append(output_node())
        network.input_layers = input_num + depth
        network.output_layers = output_num + depth
    network.layers = propagate_layers(network.input_layers, network.output_layers, network.input_num, network.output_num, network.layers)
    params = [network.input_node_array, network.output_node_array, network.input_layers, network.output_layers, network.input_num,
              network.output_num, network.layers]
    network.tree = stitch_network(params)
    return network;