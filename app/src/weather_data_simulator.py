import random

import petl

from app.src.config import config
from app.src.lib import utils
from app.src.lib.commands.export_command import export_data
from app.src.lib.commands.import_command import import_data


def produce_weather_data(count):
    result = []
    output_data = petl.fromcsv(config.weather_data_output_path, delimiter='|')
    header = petl.header(output_data)
    result.insert(0, header)
    for key, group in petl.rowgroupby(output_data, key='Position'):
        random_index = random.randint(0, config.available_records - 1)
        group_list = list(group)
        result.append(tuple(group_list[random_index]))
    result = result[0:count]
    merged_output = ['|'.join(data) for data in result]
    merged_output = '\n'.join(merged_output)
    return merged_output


def get_weather_data(**kwargs):
    print('Welcome to Weather Data Simulator')
    output = ''
    is_import = kwargs.get('is_import')
    is_export = kwargs.get('is_export')

    count = kwargs.get('count')
    count = count if count else 10
    is_import = is_import if is_import else False
    is_export = is_export if is_export else False

    utils.load_config()
    if is_import == True:
        import_data()
    if is_export == True:
        export_data()

    output = produce_weather_data(count)
    return output
