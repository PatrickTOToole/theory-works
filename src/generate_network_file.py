import csv


def __init__():
    print("")


# Creates a network file from an existing network
def generate_network_file(network, name):
    name = str(name) + ".csv"
    gen = [network.input_num, network.output_num, network.depth]
    node_weights = []
    synapse_weights = []
    for i in range(len(network.nodes)):
        for j in range(len(network.nodes[i])):
            node_weights.append(network.nodes[i][j].weight)
            for k in range(len(network.nodes[i][j].output_synapses)):
                synapse_weights.append(network.nodes[i][j].output_synapses[k].weight)
    with open(f'{name}', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(gen)
        writer.writerow(node_weights)
        writer.writerow(synapse_weights)
    output_file.close()
