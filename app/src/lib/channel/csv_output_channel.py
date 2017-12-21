from collections import OrderedDict
from datetime import datetime

import petl

from app.src.config import config
from app.src.lib.channel.output_channel import OutPutChannel


def construct_postion(rec):
    str_position = list(map(lambda x: str(x), rec))
    return ','.join(str_position)


rain = ['drizzle', 'rain', 'cloudy', 'cast']
sunny = ['clear']


def populate_summary(rec):
    if rec:
        rec = rec.lower()
        if len(list(filter(lambda x: x in rec, rain))) > 0:
            return 'Rain'
        elif len(list(filter(lambda x: x in rec, sunny))) > 0:
            return 'Sunny'
        else:
            return 'Snow'


class CSVOutputChannel(OutPutChannel):
    def __init__(self):
        super().__init__()

    def export_process(self):
        total = petl.nrows(self.data)
        if self.data and total > 0:
            mappings = OrderedDict()
            mappings['Location'] = 'location'
            mappings['Position'] = 'position', lambda rec: construct_postion(rec)
            mappings['Local Time'] = 'time', lambda rec: datetime.fromtimestamp(rec).strftime("%Y-%m-%d %H:%M:%S")
            mappings['Conditions Time'] = 'summary', lambda rec: populate_summary(rec)
            mappings['Temperature'] = 'temperature'
            mappings['Pressure'] = 'pressure'
            mappings['Humidity'] = 'humidity', lambda rec: int(rec * 100)
            self.data = petl.fieldmap(self.data, mappings)
            return True

        else:
            print('Data store doesnt have historic Data. Please run import and export Job')
            return False


    def export_write_data(self):
        petl.tocsv(self.data, config.weather_data_output_path, delimiter='|')
        return True
