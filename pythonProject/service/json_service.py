import json
from toolz import get_in


def read_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


