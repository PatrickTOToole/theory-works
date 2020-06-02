from src import Node


def __init__():
    print("")


class Synapse:
    weight = 0
    buffer = 0

    def pull_buffer(self):
        temp = self.buffer
        self.buffer = 0
        temp = temp * self.weight
        return temp

    def push_buffer(self, data):
        self.buffer = data


