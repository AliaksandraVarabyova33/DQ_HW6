from hw7.counter import Counter
from hw7.letter_count_csv_creator import LetterCSV
from hw7.text_file_parser import FileParser
from hw7.word_count_csv_creator import WordCSV


class Main:
    file_parser = FileParser()
    word_csv = WordCSV()
    letter_csv = LetterCSV()
    word_csv.create_file(Counter().count_words(file_parser.read_words()))
    letter_csv.create_file(Counter().count_letters(file_parser.read_letters()))
    file_parser.close_file()

