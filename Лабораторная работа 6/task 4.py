import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(INPUT_FILE, delimiter = None, new_line = None):
    if new_line is None:
        new_line = '\n'
    if delimiter is None:
        delimiter = ','
    with open(INPUT_FILE) as opencsv:
        result = []
        for index, line in enumerate(opencsv):
            fields = line.strip(new_line).split(delimiter)

            if index == 0:
                heads = fields
                continue

            result.append({})

            for i, _ in enumerate(heads):
                result[-1][heads[i]] = fields[i]
    return result


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
