from src import generate_network, populate_tree
import csv


def __init__():
    print("")


def build_from_file(filename):
    params = []
    with open(f'{filename}', 'r', newline='') as script:
        reader = csv.reader(script, delimiter=' ', quotechar='|')
        for row in reader:
            params.append(row)
    network = generate_network(params[0])
    populate_tree(network.tree, params[1])
    return network
