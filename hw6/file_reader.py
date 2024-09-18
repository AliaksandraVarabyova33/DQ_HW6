from hw4.hw3 import format_lines
import os

class FileReader:
    def __init__(self, path="records.txt"):
        self.file = open(path, "r")
        self.path = path

    def read_records(self):
        records = self.file.read().split("+++")
        self.file.close()
        return records

    def create_parameters(self, records):
      parameters = []
      for i in records:
            values = []
            tmp = i.strip().split("\n")
            for i in tmp:
                values.append(format_lines(i))
            parameters.append(values)
      return parameters

    def remove_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            print(f"File '{self.path}' deleted successfully.")


