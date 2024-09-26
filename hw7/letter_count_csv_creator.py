import csv

class LetterCSV:

    def __init__(self, path = "letters_counter.csv"):
        self.file = open(path, "w", newline='')
        self.path = path


    def create_file(self, letters):
        headers = ['LETTER', 'COUNT', 'UPPER_COUNT', 'PERCENTAGE']
        writer = csv.DictWriter(self.file, fieldnames=headers)
        writer.writeheader()
        for i in letters:
            writer.writerow({'LETTER': i[0], 'COUNT': i[1], 'UPPER_COUNT': i[2], 'PERCENTAGE': i[3]})