from src import build_from_file, generate_network
import sys

argv = sys.argv
current_tree = None
current_command = ""

if len(argv) > 1 and argv[1] == "-f":
    if len(argv) > 3:
        current_tree = build_from_file(argv[2])
elif len(argv) > 1 and argv[1] == "-b":
    if len(argv) == 7:
        current_tree = generate_network(argv[2:6])
while current_command != "quit":
    current_command = str(input("TWshell>"));


# TODO Add learning functions









