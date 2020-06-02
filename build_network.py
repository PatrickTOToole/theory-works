import base_node
import input_node
import output_node

def main(num_input, num_output, max_input, max_output, depth):
    input_node_array = []
    output_node_array = []
    layers = []
    input_num = num_input
    output_num = num_output
    for i in range(num_input):
        input_node_array.append(input_node())
    for i in range(num_output):
        output_node_array.append(output_node())
        input_layers = input_num + depth
        output_later = output_num + depth


def generate_tree(input_node_array, output_node_array, input_layers, output_layers, input_num, output_num, layers):
    for i in range(len(input_node_array)):
        propagate_input_node(input_node_array[i], input_layers, input_num, 0, layers)

def propagate_input_node(input_node, input_layers, input_num, layer, layers):
    print("")


def propagate_layers(input_layers, output_layers, input_num, output_num, layers):
    total_layers = output_layers + input_layers
    for i in range(total_layers + 1):
        layers.append([])
    for i in range(input_num):
        for j in range(input_layers):
            if j == 0:
                continue
            if input_layers > input_num:
                if j < (input_layers - input_num):
                    layers[j].append([base_node()])
                    layers[j].append([base_node()])
                elif j == 0:
                    layers[j].append([base_node()])
    layers[input_layers + 1].append([base_node])
    for i in range(output_num):
        for j in range(output_layers):
            if j == 0:
                continue
            if output_layers > output_num:
                if j < (output_layers - output_num):
                    layers[total_layers - j].append([base_node()])
                    layers[total_layers - j].append([base_node()])
                elif j == 0:
                    layers[total_layers - j].append([base_node()])
