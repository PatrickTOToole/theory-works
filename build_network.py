import base_node
import input_node
import output_node

def main(num_input, num_output, max_input, max_output, accuracy):
    input_node_array = []
    output_node_array = []
    for i in range(num_input):
        input_node_array.append(input_node())
    for i in range(num_output):
        output_node_array.append(output_node())