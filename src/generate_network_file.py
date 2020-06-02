import csv
from src.Node import Node


def __init__():
    print("")


# Creates a network file from an existing network
def generate_network_file(network, name):
    name = str(name) + ".csv"
    gen = [network.input_num, network.output_num, network.depth]
    populate = []
    for i in range(len(network.input_node_array)):
        populate.append(network.input_node_array[i].weight)
    for i in range(len(network.nodes)):
        for j in range(len(network.nodes[i])):
            populate.append(network.nodes[i][j].weight)
    for i in range(len(network.output_node_array)):
        populate.append(network.output_node_array[i].weight)
    with open(f'{name}', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(gen)
        writer.writerow(populate)
    output_file.close()
