from src import generate_tree, populate_tree
import csv


def __init__():
    print("")


def build_from_script(filename):
    params = []
    with open(f'{filename}', 'r', newline='') as script:
        reader = csv.reader(script, delimiter=' ', quotechar='|')
        for row in reader:
            params.append(row)
    length = len(params)-1
    tree = generate_tree(params[:length-1])
    tree = populate_tree(tree, params[length-1:length])
    return tree
