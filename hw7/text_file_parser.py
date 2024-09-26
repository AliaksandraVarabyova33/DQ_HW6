import re

class FileParser:
    def __init__(self, path=r"C:\Users\Aliaksandra_Varabyov\PycharmProjects\DQ_HW6\hw6\newsfeed.txt"):
        self.file = open(path, "r")
        self.path = path
        self.text = self.file.read()

    def read_words(self):
        words_pattern = '[a-z]+'
        text = self.text.lower()
        words = re.findall(words_pattern, text)
        return words

    def read_letters(self):
        letters_pattern = '[a-zA-Z]'
        text = self.text
        letters = re.findall(letters_pattern, text)
        return letters

    def close_file(self):
        self.file.close()