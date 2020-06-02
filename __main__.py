from src import base_node, input_node, output_node
import csv


def main(argv):
    current_tree = None
    current_command = ""
    if argv[1] == "-f":
        if len(argv) > 3:
            current_tree = build_from_script(argv[2])
    elif argv[1] == "-b":
        if len(argv) == 7:
            current_tree = generate_tree(argv[2:6])
    print("Test")
    while current_command != "quit":
        current_command = str(input("TWshell>"));


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
    params = []
    with open(f'{filename}', 'r', newline='') as script:
        reader = csv.reader(script, delimiter=' ', quotechar='|')
        for row in reader:
            params.append(row)
    length = len(params)-1
    tree = generate_tree(params[:length-1])
    tree = populate_tree(tree, params[length-1:length])
    return tree

# TODO Add learning functions


def get_network_script():
    print("")


def populate_tree(tree, weights):
    return 0


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

