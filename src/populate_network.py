def __init__():
    print("")


# Populates the network with weights
def populate_network(network, node_weights, synapse_weights):
    node_total = 0
    synapse_total = 0
    for layer in range(len(network.nodes)):
        for node in range(len(network.nodes[layer])):
            network.nodes[layer][node].weight = node_weights[node_total]
            node_total += 1
            print(f"Output Synapses: {len(network.nodes[layer][node].output_synapses)}")
            print(f"layer: {layer} node: {node}")
            for synapse in range(len(network.nodes[layer][node].output_synapses)):
                network.nodes[layer][node].output_synapses[synapse].weight = synapse_weights[synapse_total]
                synapse_total += 1
    return network
