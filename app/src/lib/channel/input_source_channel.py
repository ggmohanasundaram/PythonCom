import json

import petl
from abc import ABC, abstractmethod

from app.src.config import config

"""
 This is the super class to fetch the weather data from External Resource. 
 1. import_data - This method can be overwritten to connect with external source 
    to collect the weather data. 
 2. import_process - This method can be overwritten to fetch the required transformation from response of external source.
 3. import_write_data - The transformed data is being stored into internal data store . The data store can be used to populate
    the output data by WeatherToySimulator. Currently weatherdata.json is used as a internal storage.
"""


class InputSource(ABC):
    def __init__(self):
        self.data = None
        self.response = None

    def import_steps(self):
        import_steps = ['import_data',
                        'import_process',
                        'import_write_data']
        return import_steps

    @abstractmethod
    def import_data(self):
        return True

    @abstractmethod
    def import_process(self):
        return True

    def import_write_data(self):
        petl.tojson(self.data, config.weather_data_store_path)
        return True
