from src.Node import Node


def __init__():
    print("")


# Creates layers for the network
def propagate_layers(network):
    input_layers = network.input_layers
    output_layers = network.output_layers
    input_num = network.input_num
    output_num = network.output_num
    nodes = network.nodes
    total_layers = output_layers + input_layers
    for i in range(total_layers + 1):
        nodes.append([])
    propagate_layers_auxiliary(input_num, input_layers, total_layers, nodes, 0)
    nodes[input_layers + 1].append(Node)
    propagate_layers_auxiliary(output_num, output_layers, total_layers, nodes, 1)
    return nodes


def propagate_layers_auxiliary(num, num_layers, total_layers, node_layers, mode):
    for i in range(num):
        for j in range(num_layers):
            if mode == 0:
                x = j
            else:
                x = total_layers - j
            if j == 0:
                continue
            if num_layers > num:
                if j < (num_layers - num):
                    node_layers[x].append(Node)
                    node_layers[x].append(Node)
                elif j == 0:
                    node_layers[x].append(Node)
                else:
                    if i > j:
                        node_layers[x].append(Node)
            elif num_layers < num:
                if j > (num_layers - num):
                    node_layers[x].append(Node)
                elif j == 0:
                    node_layers[x].append(Node)
                else:
                    continue
            else:
                if i > j:
                    node_layers[x].append(Node)
