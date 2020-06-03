import csv
from src.Node import Node


def __init__():
    print("")


# TODO include synapses
# Creates a network file from an existing network
def generate_network_file(network, name):
    name = str(name) + ".csv"
    gen = [network.input_num, network.output_num, network.depth]
    node_weights = []
    synapse_weights = []
    for i in range(len(network.input_node_array)):
        node_weights.append(network.input_node_array[i].weight)
        for j in range(len(network.input_node_array[i].output_synapses)):
            synapse_weights.append(network.input_node_array[i].output_synapses[j])
    for i in range(len(network.nodes)):
        for j in range(len(network.nodes[i])):
            node_weights.append(network.nodes[i][j].weight)
            for k in range(len(network.input_node_array[i][j].output_synapses)):
                synapse_weights.append(network.nodes[i][j].output_synapses[k])
    for i in range(len(network.output_node_array)):
        node_weights.append(network.output_node_array[i].weight)
        for j in range(len(network.output_node_array[i].output_synapses)):
            synapse_weights.append(network.output_node_array[i].output_synapses[j])
    with open(f'{name}', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(gen)
        writer.writerow(node_weights)
        writer.writerow(synapse_weights)
    output_file.close()
