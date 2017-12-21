import os
from importlib import import_module

from app.src.config import config

location_list = []


def load_config():
    locations = config.Locations
    location_list.extend(flatten(locations))


def flatten(dict):
    if dict:
        return [location for locations in dict.values() for location in locations]


def import_module_path(path):
    try:
        channel_path = os.path.join(config.channel_base_path, path)
        channel_path, ext = os.path.splitext(channel_path)
        modname = ".".join(channel_path.split("/"))
        module = import_module(modname)
    except Exception as e:
        print('Problem in connecting to dark sky: %s' % str(e))
        return None
    return module


def run(module, steps):
    for step in steps:
        mod = getattr(module, step)
        result = mod()
        if not result:
            print('The step %s Failed' % step)
            return
        print('The step {step} result is {result} '.format(step=step, result=result))
