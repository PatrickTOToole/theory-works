from src import node


def __init__():
    print("")


# Creates layers for the network
def propagate_layers(network):
    input_layers = network.input_layers
    output_layers = network.output_layers
    input_num = network.input_num
    output_num = network.output_num
    layers = network.layers
    total_layers = output_layers + input_layers
    for i in range(total_layers + 1):
        layers.append([])
    propagate_layers_auxiliary(input_num, input_layers, total_layers, layers, 0)
    layers[input_layers + 1].append([node()])
    propagate_layers_auxiliary(output_num, output_layers, total_layers, layers, 1)
    return layers


def propagate_layers_auxiliary(num, num_layers, total_layers, layers, mode):
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
                    layers[x].append([node()])
                    layers[x].append([node()])
                elif j == 0:
                    layers[x].append([node()])
                else:
                    if i > j:
                        layers[x].append([node()])
            elif num_layers < num:
                if j > (num_layers - num):
                    layers[x].append([node()])
                elif j == 0:
                    layers[x].append([node()])
                else:
                    continue
            else:
                if i > j:
                    layers[x].append([node()])
