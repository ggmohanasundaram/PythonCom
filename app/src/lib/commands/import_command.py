from app.src.config import config
from app.src.lib import utils

channel_base_path = config.channel_base_path

"""
 This command is reading the  input channel from configuration file and run the import steps.
"""

def import_data():
    module = utils.import_module_path(config.input_channel.ChannelPath)
    import_channel = getattr(module, config.input_channel.ChannelName)
    import_channel_object = import_channel()
    import_steps = import_channel_object.import_steps()
    utils.run(import_channel(), import_steps)
