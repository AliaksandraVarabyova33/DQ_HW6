from hw6.file_reader import FileReader
from hw6.json_file_reader import JsonFileReader
from hw6.record_creator import RecordCreator
from hw6.user_input import UserInput
from hw6.xml_file_reader import XmlFileReader
from hw7.counter import Counter
from hw7.letter_count_csv_creator import LetterCSV
from hw7.text_file_parser import FileParser
from hw7.word_count_csv_creator import WordCSV


class FileCreator:
    def __init__(self):
        self.file = open("newsfeed.txt", "a")
        self.record_creator = RecordCreator()
        self.user_input = UserInput()
        self.file_reader = None

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

    def add_records_to_file(self, records):
        for record in records:
            self.add_record_to_file(record)

    def add_to_file(self):
        w_type = int(input("Select method of adding data to file:\nEnter 1 for Manual Input, 2 for Input From File, 3 for Input From JSON file, 4 for Input From XML"))
        if w_type == 1:
            self.add_record_to_file(self.record_creator.create_record(self.user_input.record_type_input()))
        elif w_type == 2:
            self.file_reader = FileReader()
            self.add_records_to_file(self.record_creator.create_records_from_file(self.file_reader))
        elif w_type == 3:
            self.file_reader = JsonFileReader()
            self.add_records_to_file(self.record_creator.create_records_from_json_file(self.file_reader))
        else:
            self.file_reader = XmlFileReader()
            self.add_records_to_file(self.record_creator.create_records_from_xml_file(self.file_reader))
        return w_type

    def update_newsfeed(self):
        w_type = self.add_to_file()
        self.file.close()
        if w_type == 2 or w_type == 3 or w_type == 4:
            self.file_reader.remove_file()
        self.update_csv()




