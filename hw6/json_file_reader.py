import json
from hw6.file_reader import FileReader


class JsonFileReader(FileReader):
    def __init__(self, path="records.json"):
        super().__init__(path)

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
