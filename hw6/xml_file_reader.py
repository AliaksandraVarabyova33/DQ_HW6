import xml.etree.ElementTree as ET
from hw6.file_reader import FileReader


class XmlFileReader(FileReader):
    def __init__(self, path="records.xml"):
        super().__init__(path)

    def read_records(self):
        records = ET.parse(self.file)
        self.file.close()
        return records
