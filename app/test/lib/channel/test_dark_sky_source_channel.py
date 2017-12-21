import unittest
from unittest import mock

from app.src import config
from app.src.config.config import Location
from app.src.lib import utils
from app.src.lib.channel.dark_sky_source_channel import DarkSkySource


class TestDarkSkySourceChannel(unittest.TestCase):
    dark_sky = None

    def setUp(self):
        self.dark_sky = DarkSkySource()

    @mock.patch('forecastio.load_forecast')
    def test_import_data_should_call_load_forecast(self, mock_forecastio):
        utils.location_list = [Location('xxx', -27.81, 333.96, 25)]
        config.APP_Key = 'abc'
        self.dark_sky.import_data()
        self.assertTrue(mock_forecastio.called)

    def test_import_process_for_None(self):
        self.dark_sky.data = None
        self.dark_sky.import_process()
        self.assertIsNotNone(self.dark_sky.data)

    def test_import_process_for_valid_data(self):
        self.dark_sky.data = {Location(PositionName='Wynyard', Latitude=-40.98, Longitude=145.72, Elevation=58): [
            {'dewPoint': 8.39, 'icon': 'partly-cloudy-night', 'cloudCover': 0.63, 'uvIndex': 0, 'temperature': 11.31,
             'windBearing': 278, 'precipIntensity': 0, 'windGust': 9.93, 'summary': 'Mostly Cloudy', 'humidity': 0.82,
             'precipProbability': 0, 'apparentTemperature': 11.31, 'time': 1503648000, 'windSpeed': 5.35,
             'pressure': 1021.96, 'ozone': 323.71},
            {'dewPoint': 8.31, 'icon': 'partly-cloudy-night', 'cloudCover': 0.74, 'uvIndex': 0, 'temperature': 10.71,
             'windBearing': 278, 'precipIntensity': 0, 'windGust': 10.03, 'summary': 'Mostly Cloudy', 'humidity': 0.85,
             'precipProbability': 0, 'apparentTemperature': 10.71, 'time': 1503651600, 'windSpeed': 5.19,
             'pressure': 1022.09, 'ozone': 323.5},
        ]}

        self.dark_sky.import_process()
        self.assertIsNotNone(self.dark_sky.data)