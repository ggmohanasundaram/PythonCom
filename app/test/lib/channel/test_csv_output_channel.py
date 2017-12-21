import unittest

from app.src.lib.channel.csv_output_channel import CSVOutputChannel, populate_summary


class TestCSVOutputChannel(unittest.TestCase):
    csv_source = None

    def setUp(self):
        self.csv_source = CSVOutputChannel()

    def test_populate_summary_for_none(self):
        summary = populate_summary('hello cloudy')
        self.assertEqual('Rain', summary)

        summary = populate_summary('clear')
        self.assertEqual('Sunny', summary)

        summary = populate_summary('None')
        self.assertEqual('Snow', summary)
