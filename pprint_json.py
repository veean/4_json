import json


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as file_handler:
		return json.load(file_handler)


def pretty_print_json(data):
	for json_unit in data:
		pprint.pprint(json_unit)


if __name__ == '__main__':
    pass
