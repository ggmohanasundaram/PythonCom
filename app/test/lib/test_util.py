import unittest

from app.src.lib import utils
from app.src.lib.channel.dark_sky_source_channel import DarkSkySource


class TestUtil(unittest.TestCase):
    def test_load_configuration(self):
        self.assertEqual(0, len(utils.location_list))
        utils.load_config()
        self.assertGreater(len(utils.location_list), 0)

    def test__flatten_dict_should_handle_none(self):
        input = None
        output = utils.flatten(input)
        self.assertIsNone(output)

    def test__flatten_dict_should_return_list(self):
        input = {1: [1, 2, 3], 2: [1, 2, 3]}
        output = utils.flatten(input)
        self.assertEqual([1, 2, 3, 1, 2, 3], output)
