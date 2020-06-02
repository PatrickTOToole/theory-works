from src import base_node


def __init__():
    print("")


def propagate_layers(input_layers, output_layers, input_num, output_num, layers):
    total_layers = output_layers + input_layers
    for i in range(total_layers + 1):
        layers.append([])
    propagate_layers_auxiliary(input_num, input_layers, total_layers, layers, 0)
    layers[input_layers + 1].append([base_node()])
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
                    layers[x].append([base_node()])
                    layers[x].append([base_node()])
                elif j == 0:
                    layers[x].append([base_node()])
                else:
                    if i > j:
                        layers[x].append([base_node()])
            elif num_layers < num:
                if j > (num_layers - num):
                    layers[x].append([base_node()])
                elif j == 0:
                    layers[x].append([base_node()])
                else:
                    continue
            else:
                if i > j:
                    layers[x].append([base_node()])
