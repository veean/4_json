import json
import os


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True))


if __name__ == '__main__':
    print('Enter filepath for json file : ')
    filepath = str(input())
    if not filepath:
        print('Try again : ')
    pretty_print_json(load_data(filepath))
