from src import Synapse


def __init__():
    print("")


# An object to store data for a singular node
class BaseNode:
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

    def btf_learn(self, weight_val, direction):
        self.weight = self.weight - (0.5 * weight_val * direction)
        weight_val = weight_val * 0.5
        for i in range(len(self.input_synapses)):
            self.input_synapses[i].btf_learn(weight_val, direction)

    def ftb_learn(self, weight_val, direction):
        self.weight = self.weight - (0.5 * weight_val * direction)
        for i in range(len(self.output_synapses)):
            self.output_synapses[i].btf_learn(weight_val, direction)