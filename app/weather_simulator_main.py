import os
import sys

sys_path_append = sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from app.src.weather_data_simulator import get_weather_data

def main():
    print(get_weather_data(count=10))
    print('-------')
    print(get_weather_data(is_export=True))
    print('------')
    print(get_weather_data(count=20, is_import=True, is_export=True))

if __name__ == '__main__':
    main()
