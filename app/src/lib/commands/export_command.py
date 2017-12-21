
from app.src.config import config
from app.src.lib import utils

channel_base_path = config.channel_base_path

"""
 This command is reading the  out channel from configuration file and run the export steps.  
"""
def export_data():
    module = utils.import_module_path(config.output_channel.ChannelPath)
    export_channel = getattr(module, config.output_channel.ChannelName)
    import_channel_object = export_channel()
    export_steps = import_channel_object.export_steps()
    utils.run(export_channel(), export_steps)
