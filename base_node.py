import this

class BaseNode():
    weight = 1
    output_nodes = []
    input_nodes = []

    def process(input_val):
        return input_val * this.weight

    def btf_learn(weight_val, direction):
        this.weight = this.weight - (0.5 * weight_val * direction)
        weight_val = weight_val * 0.5
        for i in range(len(this.input_nodes)):
            this.input_nodes[i].btf_learn(weight_val, direction)

    def ftb_learn(weight_val, direction):
        this.weight = this.weight - (0.5 * weight_val * direction)
        for i in range(len(this.output_nodes)):
            this.output_nodes[i].btf_learn(weight_val, direction)