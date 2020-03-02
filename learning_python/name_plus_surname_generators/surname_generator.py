import json
import random


def read_surnames():
    with open("name_plus_surname_generators/surnames.json", "r") as surname_file:
        json_file = surname_file.read()
        surnames = json.loads(json_file)
        return surnames


def surname_generator():
    surnames = read_surnames()
    result = random.choice(surnames)
    return result




