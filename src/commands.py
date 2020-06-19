from src.generate_network import generate_network
from src.generate_network_file import generate_network_file


def __init__():
    print("")


def build_network(*args):
    if len(args) != 4:
        print(f"Invalid arguments {len(args)}\nUsage: build: <num inputs> <num outputs> <depth>")
        return -1
    else:
        return generate_network(*args[1:])


def save_network(*args):
    if len(args) != 3:
        print(f"Invalid arguments {len(args)}\nUsage: save <network> <filename>")
        return -1
    else:
        if args[0] is None:
            print("No current network")
            return -1
        else:
            print(f"Network saved as {generate_network_file(*args[1:])}")

