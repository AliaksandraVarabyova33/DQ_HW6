
from hw6.records import News, PrivateAd, WeatherForecast
from hw6.user_input import UserInput
from datetime import date
import xml.etree.ElementTree as ET


class RecordCreator:
    @staticmethod
    def create_record(record_type):
        if record_type == 1:
            return News(UserInput.text_input(), UserInput.city_input())
        elif record_type == 2:
            return PrivateAd(UserInput.text_input(), UserInput.expiration_date_input())
        else:
            weather_parameters = UserInput.weather_parameters_input()
            return WeatherForecast(weather_parameters[0].capitalize(), weather_parameters[1].capitalize(), weather_parameters[2].capitalize(), UserInput.city_input())

    @staticmethod
    def create_records_from_file(file_reader):
        records = file_reader.read_records()
        parameters = file_reader.create_parameters(records)
        records = []
        for i in parameters:
            if int(i[0]) == 1:
                records.append(News(i[1], i[2]))
            elif int(i[0]) == 2:
                year,month,day = map(int, i[2].split('-'))
                records.append(PrivateAd(i[1], date(year,month,day )))
            else:
                records.append(WeatherForecast(i[1], i[2], i[3], i[4]))
        return records

    @staticmethod
    def create_records_from_json_file(json_file_reader):
        records_from_file = json_file_reader.read_records()
        parameters = json_file_reader.read_parameters(records_from_file )
        records = []
        for i in parameters:
            if int(i["type"]) == 1:
                records.append(News(i["text"], i["city"]))
            elif int(i["type"]) == 2:
                year, month, day = map(int, i["expiration_date"].split('-'))
                records.append(PrivateAd(i["text"], date(year, month, day)))
            else:
                records.append(WeatherForecast(str(i["is_rainy"]), str(i["is_windy"]), str(i["is_sunny"]), i["city"]))
        return records

    @staticmethod
    def create_records_from_xml_file(xml_file_reader):
        xml_file = xml_file_reader.read_records()
        root = xml_file.getroot()
        records = []
        for element in root:
            if int(element.get('type')) == 1:
                records.append(News(element.text, element.get('city')))
            elif int(element.get('type')) == 2:
                year, month, day = map(int, element.get('expiration_date').split('-'))
                records.append(PrivateAd(element.text, date(year, month, day)))
            else:
                is_rainy = "not_defined"
                is_windy = "not_defined"
                is_sunny = "not_defined"
                for sub_element in element:
                    if sub_element.tag == 'is_rainy':
                        is_rainy = sub_element.text
                    elif sub_element.tag == 'is_windy':
                        is_windy = sub_element.text
                    else:
                        is_sunny = sub_element.text
                records.append(WeatherForecast(is_rainy, is_windy, is_sunny, element.get('city')))
        return records

