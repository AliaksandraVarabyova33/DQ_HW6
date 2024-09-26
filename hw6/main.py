from hw6.file_creator import FileCreator
from hw6.record_creator import RecordCreator
from hw6.user_input import UserInput
from hw6.file_reader import FileReader


class Main:
    file_creator = FileCreator()
    file_reader = FileReader()
    file_creator.add_record_to_file(RecordCreator().create_record(UserInput().record_type_input()))
    # file_creator.add_records_to_file(RecordCreator().create_records_from_file(file_reader))
    # file_reader.remove_file()
    file_creator.update_csv()








