import csv


def __init__():
    print("")


# Creates a network file from an existing network
def generate_network_file(network, name):
    name = str(name) + ".csv"
    gen = [network.input_num, network.output_num, network.depth]
    populate = []
    for i in range(len(network.tree)):
        for j in range(len(network.tree[i])):
            populate.append(network.tree[i][j])
    with open(f'{name}', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(gen)
        writer.writerow(populate)
    return output_file
