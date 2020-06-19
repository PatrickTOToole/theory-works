import json
from pathlib import Path
import os


def __main__():
    cwd = Path(os.path.dirname(os.path.abspath(__file__)));
    config = json.load(open(cwd / "config.json"))
    