import requests
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import datetime
from datetime import time
import maya

# results = [temp, temp_max, temp_min, feels_like, temp_kf, clouds, status, sunrise, sunset]
class Weather:
    def getWeather(self):
        # r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London,GB&appid=99f3aa348c13b09abf198eb14c90b6aa')
        # print(r.text)

        owm = OWM('')
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place('State College')
        w = observation.weather

        results = []

        temp = w.temperature('fahrenheit')
        for x in temp:
            results.append(temp.get(x))
        results.append(w.clouds)


        wind = w.wind(unit='miles_hour')
        results.append(round(wind['speed']))

        results.append(w.status)
        results.append(datetime.datetime.strftime(maya.parse(w.sunrise_time(timeformat='date')).datetime(to_timezone='US/Eastern', naive=True), "%I:%M%p"))
        results.append(datetime.datetime.strftime(maya.parse(w.sunset_time(timeformat='date')).datetime(to_timezone='US/Eastern', naive=True), "%I:%M%p"))
        print(results)

weather = Weather()
weather.getWeather()