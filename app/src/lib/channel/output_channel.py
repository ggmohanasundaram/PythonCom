from abc import ABC, abstractmethod

import petl

from app.src.config import config
from app.src.lib import utils

"""
 This is the super class to get the weather data from internal data store and populate the output. 
 1. export_data - This method can be overwritten to connect with any internal weather data source. 
 2. export_process - This method can be overwritten to do the required transformation of internal data.
 3. export_write_data - The transformed data is being stored into any format base on client format
"""


class OutPutChannel(ABC):
    def __init__(self):
        self.data = None

    def export_steps(self):
        import_steps = ['export_data',
                        'export_process',
                        'export_write_data']
        return import_steps

    def export_data(self):
        try:
            self.data = petl.fromjson(config.weather_data_store_path)
        except Exception as e:
            print('Problem in collecting Data from data store: %s' % str(e))
            return False
        return True

    @abstractmethod
    def export_process(self):
        return True

    @abstractmethod
    def export_write_data(self):
        return True
