from src import output_node, input_node, stitch_network, propagate_layers


def __init__():
    print("")


def generate_tree(input_layers, output_layers, input_num, output_num, depth):
    input_node_array = []
    output_node_array = []
    layers = []
    input_num = input_num
    output_num = output_num
    depth = depth
    for i in range(input_num):
        input_node_array.append(input_node())
    for i in range(output_num):
        output_node_array.append(output_node())
        input_layers = input_num + depth
        output_layers = output_num + depth
    layers = propagate_layers(input_layers, output_layers, input_num, output_num, layers)
    params = [input_node_array, output_node_array, input_layers, output_layers, input_num, output_num, layers]
    tree = stitch_network(params)
    return tree;