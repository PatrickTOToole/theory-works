def __init__():
    print("")


class BaseNode():
    weight = 1
    output_nodes = []
    input_nodes = []

    def process(self, weight, input_val):
        return input_val * weight

    def btf_learn(self, node, weight_val, direction):
        node.weight = node.weight - (0.5 * weight_val * direction)
        weight_val = weight_val * 0.5
        for i in range(len(node.input_nodes)):
            node.input_nodes[i].btf_learn(weight_val, direction)

    def ftb_learn(self, node, weight_val, direction):
        node.weight = node.weight - (0.5 * weight_val * direction)
        for i in range(len(node.output_nodes)):
            node.output_nodes[i].btf_learn(weight_val, direction)