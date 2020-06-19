from src.build_from_file import build_from_file
from src.generate_network import generate_network
from src.generate_network_file import generate_network_file
import sys
import json
from pathlib import Path
import os
from src.commands import save_network
from src.commands import build_network

argv = sys.argv
current_network = None
c_argv = ""
cwd = Path(os.path.dirname(os.path.abspath(__file__)));
config = json.load(open(cwd / "config.json"))
if len(argv) > 1 and argv[1] == "-f":
    if len(argv) > 3:
        current_network = build_from_file(argv[2])
elif len(argv) > 1 and argv[1] == "-b":
    if len(argv) == 7:
        current_network = generate_network(argv[2:6])
while True:
    try:
        c_argv = str(input("TWshell>")).split(" ");
        for idx in range(len(c_argv)):
            if c_argv[idx] == "cn":
                c_argv[idx] = current_network
    except KeyboardInterrupt:
        print("Interrupt Detected\nTo quit, enter \"quit\"")
        continue
    if c_argv[0] in config["commands"]:
        cmd_len = len(c_argv)
        if config["commands"][c_argv[0]][1] == 0:
            exec(config["commands"][c_argv[0]][0])
        else:
            temp = config["commands"][c_argv[0]][0]
            temp += "("
            for elt in range(len(c_argv[:cmd_len - 1])):
                temp += f"{c_argv[elt]}, "
            temp += f"{c_argv[cmd_len-1]}"
            temp += ")"
            print(temp + "\n")
            exec(temp)
    else:
        continue
    """if c_argv == "build":
        current_network = generate_network(3, 3, 2)
        print("Network built")
    elif c_argv == "save network":
        if current_network is None:
            print("No current network")
        else:
            file = generate_network_file(current_network, "temp")
            print("Network saved")
    elif c_argv == "clear network":
        current_network = None
        print("Network cleared")
    elif c_argv == "build from file":
        if current_network is not None:
            print("Current network exists")
        else:
            current_network = build_from_file("temp.csv")
    elif c_argv == "quit":
        sys.exit(0)
    else:"""
