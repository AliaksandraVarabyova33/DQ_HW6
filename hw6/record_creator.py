from hw6.records import News, PrivateAd, WeatherForecast
from hw6.user_input import UserInput
from datetime import date


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