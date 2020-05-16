"""Test for name_parser module."""

import unittest

from . import data
from .. import name_parser


class TestNameParser(unittest.TestCase):
    """Test description module."""

    def test_get_image_size(self):
        """Test get_image_size function."""
        for datum in data.INPUT:
            size = name_parser.get_image_size(datum)
            self.assertEqual(size, data.SIZES[datum])
