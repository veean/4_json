import json
import os


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
        while True:
        filepath = input('Enter filepath for json file : ')
        if not filepath:
            print('Try again : ')
        else:
            pretty_print_json(load_data(filepath))
            break
