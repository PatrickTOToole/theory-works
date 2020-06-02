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

