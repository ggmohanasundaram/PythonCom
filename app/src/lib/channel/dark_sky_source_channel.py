import petl
from app.src.lib import utils
from app.src.lib.channel.input_source_channel import InputSource
import forecastio
from app.src.config import config

"""
    1. This is a subclass of Input source channel
    2. This channel is used to collect the weather data via Dark sky api and store into internal storage
    Currently weather data.json is being used as a internal storage
"""


class DarkSkySource(InputSource):
    def __init__(self):
        super().__init__()
        self.hourly_data = {}

    def import_data(self):
        for location in utils.location_list:
            try:
                print('Download data from Dark Sky Source')
                forecast = forecastio.load_forecast(config.APP_Key, location.Latitude, location.Longitude, units='si')
                forecast_hourly_data = forecast.hourly().data
                self.hourly_data[location] = [hour_data.d for hour_data in forecast_hourly_data]
            except Exception as e:
                print('Problem in connecting to dark sky: %s' % str(e))
                return False
        return True

    def import_process(self):
        self.data = self.hourly_data
        [list(map(lambda value: value.update(
            {'location': key.PositionName, 'position': (key.Latitude, key.Longitude, key.Elevation)}), values)) for
         key, values in self.data.items()]

        weather_data = [value for key, values in self.data.items() for value in values]

        self.data = petl.fromdicts(weather_data)

        self.data = petl.cut(self.data,
                             'location', 'position', 'time', 'summary', 'temperature', 'pressure', 'humidity')

        return True
