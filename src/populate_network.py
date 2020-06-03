def __init__():
    print("")


# Populates the network with weights
def populate_network(network, node_weights, synapse_weights):
    node_total = 0
    synapse_total = 0
    for i in range(len(network.input_node_array)):
        network.input_node_array[i].weight = node_weights[i]
        node_total += 1
        for j in range(len(network.input_node_array[i].output_synapses)):
            network.input_node_array[i].output_synapses[j].weight = synapse_weights[synapse_total]
    for i in range(len(network.nodes)):
        for j in range(len(network.nodes[i])):
            network.nodes[i][j].weight = node_weights[node_total]
            node_total += 1
            for k in range(len(network.nodes[i][j].output_synapses)):
                network.nodes[i][j].output_synapses[k].weight = synapse_weights[synapse_total]
    for i in range(len(network.output_node_array)):
        network.output_node_array[i].weight = node_weights[node_total]
        node_total += 1
        for j in range(len(network.output_node_array[i].output_synapses)):
            network.output_node_array[i].output_synapses[j].weight = synapse_weights[synapse_total]
    return network
