from src.build_from_file import build_from_file
from src.generate_network import generate_network
from src.generate_network_file import generate_network_file
import sys

argv = sys.argv
current_network = None
current_command = ""


if len(argv) > 1 and argv[1] == "-f":
    if len(argv) > 3:
        current_network = build_from_file(argv[2])
elif len(argv) > 1 and argv[1] == "-b":
    if len(argv) == 7:
        current_network = generate_network(argv[2:6])
while current_command != "quit":
    current_command = str(input("TWshell>"));
    if current_command == "build new":
        current_network = generate_network(3, 3, 2)
    if current_command == "save network":
        if current_network is None:
            print("No current network")
        else:
            file = generate_network_file(current_network, "temp")










