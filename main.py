import base_node
import input_node
import output_node


def main(argv):
    if argv[1] == "-f":
        if len(argv) > 3:
            build_from_script(argv[2])
    elif argv[1] == "-b":
        if len(argv) == 7:
            generate_tree(argv[2:6])


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


def stitch_network(input_node_array, output_node_array, input_layers, output_layers, input_num, output_num, layers):
    return 0;


def build_from_script(filename):
    script = open(filename, "r")
    gen_params = []
    populate_params = []
    generate_tree(gen_params)
    populate_tree(populate_params)


def get_network_script():
    print("")


def populate_tree(weights):
    print("")


def propagate_layers(input_layers, output_layers, input_num, output_num, layers):
    total_layers = output_layers + input_layers
    for i in range(total_layers + 1):
        layers.append([])
    propagate_layers_auxiliary(input_num, input_layers, total_layers, layers, 0)
    layers[input_layers + 1].append([base_node])
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

