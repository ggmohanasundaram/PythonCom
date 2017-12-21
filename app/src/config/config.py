# The Locations are Dict and has list of positions

import os
from collections import namedtuple

# Position is a tuple (PositionName, Latitude,Longitude,Elevation)
Location = namedtuple('Location', ['PositionName', 'Latitude', 'Longitude', 'Elevation'])

# Channel is a tuple (ChannelType, ClassName,Path)
Channel = namedtuple('Channel', ['Type', 'ChannelName', 'ChannelPath'])

weather_data_store_path = os.path.join(os.path.dirname(__file__), '../lib/data/weatherdata.json')
weather_data_output_path = os.path.join(os.path.dirname(__file__), '../lib/data/output.csv')

Locations = {
    'NSW': [
        Location('Sydney', -33.86, 151.20, 17),
        Location('Wynyard', -40.98, 145.72, 58),
        Location('Westmead', -33.80, 150.98, 41),
        Location('Newcastle', -32.92, 151.77, 13),
        Location('PendleHill', -33.80, 150.95, 52),
        Location('Chatswood', -33.79, 151.18, 98),
        Location('Parramatta', -33.81, 151.00, 12),
        Location('Hornsby', -33.70, 151.09, 191),
        Location('Waitara', -33.70, 151.10, 171),
        Location('Strathfield', -33.88, 151.08, 38)
    ],

    'VIC': [
        Location('Melbourne', -37.81, 144.96, 25),
        Location('Carlton', -37.80, 144.96, 45),
        Location('Docklands', -37.81, 144.94, 10),
        Location('Flemington', -37.78, 144.92, 18),
        Location('Kensington', -33.91, 151.22, 25),
        Location('Southbank', -37.82, 144.95, 4),
        Location('North Melbourne', -37.79, 144.94, 10),
        Location('South Wharf', -37.82, 144.95, 4),
        Location('South Yarra', -37.84, 144.98, 17),
        Location('West Melbourne', -37.80, 144.92, 3),
    ],
    'QLD': [
        Location('Bowen Hills', -27.44, 153.03, 9),
        Location('Brisbane', -27.47, 153.02, 28),
        Location('East Brisbane', -27.48, 153.05, 13),
        Location('Fortitude Valley', -27.45, 153.03, 21),
        Location('Herston', -27.44, 153.02, 31),
        Location('Highgate Hill', -27.48, 153.01, 58),
        Location('Kangaroo Point', -27.46, 153.03, 2),
        Location('Newstead', -27.44, 153.04, 4),
        Location('Paddington', -27.46, 153.00, 29),
        Location('Red Hill', -27.45, 153.00, 37),
    ],

}

channel_base_path = 'app.src.lib.channel'
input_channel = Channel('Input', 'DarkSkySource', 'dark_sky_source_channel.py')
output_channel = Channel('Output', 'CSVOutputChannel', 'csv_output_channel.py')

APP_Key = ''
available_records = 48 # Darksky hourly api provides 48 hours data per position