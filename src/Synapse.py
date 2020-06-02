from src import node


def __init__():
    print("")


class Synapse:
    weight = 0
    buffer = 0


def pull_buffer(synapse):
    temp = synapse.buffer
    synapse.buffer = 0
    return temp


