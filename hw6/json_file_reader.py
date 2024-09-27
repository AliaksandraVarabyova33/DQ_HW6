import os
import json

class JsonFileReader:
    def __init__(self, path="records.json"):
        self.file = open(path, "r")
        self.path = path

    def read_records(self):
        records_as_a_dict = json.load(self.file)
        records_as_a_list = list(records_as_a_dict.values())
        self.file.close()
        return records_as_a_list

    def read_parameters(self, records):
        parameters = []
        for i in records:
            for j in i:
                parameters.append(j)
        return parameters

    def remove_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f"File '{self.path}' deleted successfully.")