from src.Node import Node


def __init__():
    print("")


# Creates layers for the network
def propagate_layers(network):
    input_layers = network.input_layers
    output_layers = network.output_layers
    input_num = network.input_num
    output_num = network.output_num
    total_layers = output_layers + input_layers
    # Generate input nodes
    network.nodes.append([])
    for i in range(network.input_num):
        network.nodes[0].append(Node)
    propagate_layers_auxiliary(input_num, input_layers, total_layers, network.nodes, 0)
    network.nodes[input_layers + 1].append(Node)
    propagate_layers_auxiliary(output_num, output_layers, total_layers, network.nodes, 1)
    for i in range(network.output_num):
        network.nodes[i].append(Node)
    return network


def propagate_layers_auxiliary(input_num, input_layers, total_layers, node_layers, mode):
    for i in range(input_num):
        for j in range(input_layers):
            node_layers.append([])
            if mode == 0:
                x = j
            else:
                x = total_layers - j
            if j == 0:
                continue
            if input_layers > input_num:
                if j < (input_layers - input_num):
                    node_layers[x].append(Node)
                    node_layers[x].append(Node)
                elif j == 0:
                    node_layers[x].append(Node)
                else:
                    if i > j:
                        node_layers[x].append(Node)
            elif input_layers < input_num:
                if j > (input_layers - input_num):
                    node_layers[x].append(Node)
                elif j == 0:
                    node_layers[x].append(Node)
                else:
                    continue
            else:
                if i > j:
                    node_layers[x].append(Node)
