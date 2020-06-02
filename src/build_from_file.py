from src.generate_network import generate_network
from src.populate_network import populate_network
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
    for i in range(len(params)):
        for j in range(len(params[i])):
            params[i][j] = float(params[i][j])
    network = generate_network(params = params[0])
    populate_network(params = [network, params[1]])
    return network
