"""Tests for Config class."""

import os
import unittest

from ..config import Config


def path(string):
    """Normalize path."""
    return os.path.normpath(string)


class TestConfig(unittest.TestCase):
    """Tests for Config class."""

    def config_file(self, filename):
        """Build configuration file."""
        return os.path.join(self.folder, filename)

    def setUp(self):
        """Set up tests."""
        folder = os.path.dirname(__file__)
        self.folder = os.path.join(folder, 'configs')

    def test_parse_data_from_config(self):
        """Test for parsing valid configuration file."""
        config_file = os.path.join(self.folder, 'correct.ini')
        config = Config(config_file)
        self.assertEqual(config.sources(), path('path/to/sources'))
        self.assertEqual(config.destination(), path('path/to/destination'))

    def test_parse_invalid_config(self):
        """Test for parsing invalid configuration file."""
        with self.assertRaises(KeyError):
            config_file = self.config_file('no_dst.ini')
            _config = Config(config_file)

        with self.assertRaises(KeyError):
            config_file = self.config_file('no_src.ini')
            _config = Config(config_file)
