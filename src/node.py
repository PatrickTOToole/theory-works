def __init__():
    print("")


# An object to store data for a singular node
class BaseNode:
    weight = 0
    output_nodes = []
    input_nodes = []

    def process(self, input_val):
        return input_val * self.weight

    def btf_learn(self, weight_val, direction):
        self.weight = self.weight - (0.5 * weight_val * direction)
        weight_val = weight_val * 0.5
        for i in range(len(self.input_nodes)):
            self.input_nodes[i].btf_learn(weight_val, direction)

    def ftb_learn(self, weight_val, direction):
        self.weight = self.weight - (0.5 * weight_val * direction)
        for i in range(len(self.output_nodes)):
            self.output_nodes[i].btf_learn(weight_val, direction)