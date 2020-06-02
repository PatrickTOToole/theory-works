def __init__():
    print("")


# Populates the network with weights
def populate_network(network, weights):
    total = 0
    for i in range(len(network.input_node_array)):
        network.input_node_array[i].weight = weights[i]
        total += 1
    for i in range(len(network.nodes)):
        for j in range(len(network.nodes[i])):
            network.nodes[i][j].weight = weights[total]
            total += 1
    for i in range(len(network.output_node_array)):
        network.output_node_array[i].weight = weights[total]
        total += 1
    return network