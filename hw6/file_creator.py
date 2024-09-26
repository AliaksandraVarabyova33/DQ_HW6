from hw7.counter import Counter
from hw7.letter_count_csv_creator import LetterCSV
from hw7.text_file_parser import FileParser
from hw7.word_count_csv_creator import WordCSV


class FileCreator:
    def __init__(self):
        self.file = open("newsfeed.txt", "a")

    # adding this method in scope of the 7th hometask to generate new csv files every time new record is added
    def update_csv(self):
        file_parser = FileParser()
        word_csv = WordCSV()
        letter_csv = LetterCSV()
        word_csv.create_file(Counter().count_words(file_parser.read_words()))
        letter_csv.create_file(Counter().count_letters(file_parser.read_letters()))
        file_parser.close_file()

    def add_record_to_file(self, record):
        if record.__class__.__name__ == "News":
            self.file.write("News:\n" + record.text + "\n" +record.city + ", " + str(record.dt) + "\n--------------------\n\n")
        elif record.__class__.__name__ == "PrivateAd":
            self.file.write("PrivateAd:\n" + record.text + "\n" + "Actual till: " + str(record.expiration_date) + ", days left: " + str(record.days_left) + "\n--------------------\n\n")
        else:
            self.file.write("Weather Forecast:\n" + record.text + "\n" + "Weather rating: " + str(record.weather_rating) + "\n" + record.city + ", " + str(record.dt) + "\n--------------------\n\n")
        self.file.close()

    def add_records_to_file(self, records):
        for record in records:
            self.add_record_to_file(record)
        self.file.close()

