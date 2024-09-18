from datetime import date


class Record:
    def __init__(self, text):
        self.text = text


class News(Record):
    def __init__(self, text, city):
        super().__init__(text)
        self.city = city
        self.dt = date.today()


class PrivateAd(Record):
    def __init__(self, text, expiration_date):
        super().__init__(text)
        self.expiration_date = expiration_date
        self.days_left = (expiration_date - date.today()).days


class WeatherForecast(Record):
    def __init__(self, is_rainy, is_sunny, is_windy, city):
        super().__init__("Today the following weather is expected:\nRainy: " + is_rainy + "\nWindy: " + is_windy + "\nSunny: " + is_sunny)
        self.city = city
        self.dt = date.today()
        if is_rainy == 'True' and is_windy == 'True' and is_sunny == 'False':
            self.weather_rating = 1
        elif is_rainy == 'True' and is_windy == 'False' and is_sunny == 'False':
            self.weather_rating = 2
        elif is_rainy == 'False' and is_windy == 'True' and is_sunny == 'False':
            self.weather_rating = 3
        elif is_rainy == 'False' and is_windy == 'True' and is_sunny == 'True':
            self.weather_rating = 4
        elif is_rainy == 'False' and is_windy == 'False' and is_sunny == 'False':
            self.weather_rating = 5
        else:
            self.weather_rating = 6