def __init__():
    print("")


# An object to store data for a singular node
class Node:
    weight = 0
    output_synapses = []
    input_synapses = []

    def process(self):
        data = 0
        for in_synapse in range(len(self.input_synapses)):
            buffer = self.input_synapses[in_synapse].pull_buffer()
            buffer = buffer * self.weight
            data += buffer
        for out_synapse in range(len(self.output_synapses)):
            self.output_synapses[out_synapse].push_buffer()

    def set_weight(self, weight):
        self.weight = weight


class Synapse:
    weight = 0.5
    buffer = 0

    def pull_buffer(self):
        temp = self.buffer
        self.buffer = 0
        temp = temp * self.weight
        return temp

    def push_buffer(self, data):
        self.buffer = data

    def set_weight(self, weight):
        self.weight = weight


# An object to store the network
class NetworkObject:
    nodes = []
    synapses = []
    input_num = 0
    output_num = 0
    depth = 0

