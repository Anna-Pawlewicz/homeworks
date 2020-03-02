import json
import random


def read_names():
    with open("name_plus_surname_generators/names.json", "r") as name_file:
        json_file = name_file.read()
        names = json.loads(json_file)
        return names


def name_generator():
    names = read_names()
    result = random.choice(names)
    print(result)
    return result


name_generator()




