from src.generate_network import generate_network
from src.generate_network_file import generate_network_file


def __init__():
    print("")


def build_network(*args):
    if len(args) != 3:
        print("Invalid arguments\nUsage: build: <num inputs> <num outputs> <depth>")
        return -1
    else:
        return generate_network(*args)


def save_network(*args):
    if len(args) != 2:
        print("Invalid arguments\nUsage: save <filename>")
        return -1
    else:
        if args[0] is None:
            print("No current network")
            return -1
        else:
            print(f"Network saved as {generate_network_file(*args)}")

