import csv
from os import write


class WordCSV:

    def __init__(self, path = "words_counter.csv"):
        self.file = open(path, "w", newline='')
        self.path = path


    def create_file(self, words):
        headers = ['WORD', 'COUNT']
        writer = csv.DictWriter(self.file, fieldnames=headers, delimiter=":")
        writer.writeheader()
        for i in words:
            writer.writerow({'WORD': i[0], 'COUNT': i[1]})
