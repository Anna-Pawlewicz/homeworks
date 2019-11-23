# Create a dictionary (in your file) of four person from our course and the name of the group they belong to.
# When you run your program it should ask the user to enter a name, and return the name of the group of that person back to them.
# It should look something like this:
# >>>Welcome to the pydqz1-group-infromator, I can tell you where those users belong to:

import json


class Informatory:

    def __init__(self):
        self.dictionary = {}

    def read_file(self, file_name):
        with open(file_name, 'r') as f:
            json_file = f.read()
            self.dictionary = json.loads(json_file)

    def message(self):
        name = input(
            "Welcome to the pydqz1-group-informatory,If You enter the student name I can tell you which group it belongs to:")
        if name in self.dictionary:
            group = self.dictionary[name]
            print(group)
        else:
            print("There is no such student.")


informatory = Informatory()
informatory.read_file('students.json')
informatory.message()
