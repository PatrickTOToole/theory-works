from src.generate_network import generate_network
from src.populate_network import populate_network
from src.stitch_network import stitch_network
import csv


def __init__():
    print("")


# Builds a network from a file
def build_from_file(filename):
    params = []
    with open(f'{filename}', 'r', newline='') as script:
        reader = csv.reader(script, delimiter=' ', quotechar='|')
        for row in reader:
            params.append(row)
    for i in range(len(params[0])):
        params[0][i] = int(params[0][i])
    for i in range(len(params[1])):
        params[1][i] = float(params[1][i])
    for i in range(len(params[2])):
        params[2][i] = float(params[2][i])
    network = generate_network(params[0][0], params[0][1], params[0][2])
    populate_network(network, params[1], params[2])
    return network
