from src.Synapse import Synapse


def __init__():
    print("")


# Stitches network input and output
def stitch_network(network):
    for layer_num in range(network.depth * 2 + 3):
        if layer_num == 0:
            for node_num in range(network.input_num):
                for synapse_num in range(len(network.nodes[0])):
                    print("added synapse")
                    network.nodes[layer_num][node_num].output_synapses.append(Synapse)
        elif layer_num == 1 and layer_num <= network.depth:
            for node_num in range(len(network.nodes[0])):
                for previous_nodes in range(network.input_num):
                    network.nodes[layer_num][node_num].input_synapses.append(network.nodes[layer_num-1][previous_nodes].output_synapses[node_num])
                    network.nodes[layer_num][node_num].output_synapses.append(Synapse)
        elif layer_num <= network.depth * 2 + 1:
            for node_num in range(len(network.nodes[layer_num])):
                for previous_nodes in range(len(network.nodes[layer_num - 1])):
                    network.nodes[layer_num][node_num].input_synapses.append(network.nodes[layer_num - 1][previous_nodes].output_synapses[node_num])
                    network.nodes[layer_num][node_num].output_synapses.append(Synapse)
        else:
            for node_num in range(network.output_num):
                for previous_nodes in range(len(network.nodes[layer_num - 1])):
                    network.nodes[layer_num][node_num].input_synapses.append(network.nodes[layer_num - 1][previous_nodes].output_synapses[node_num])
    return network
