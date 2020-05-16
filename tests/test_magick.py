"""Tests for magick module."""

import unittest

from .. import magick


def correct_output(_filename):
    """Stub for correct output."""
    return '40x40'


def incorrect_output(_filename):
    """Stub for incorrect output."""
    return 'azaza'


# pylint: disable=protected-access
class TestMagick(unittest.TestCase):
    """Tests for magick module."""

    def setUp(self):
        """Set up."""
        self.old_function = magick._get_image_size_output

    def tearDown(self):
        """Tear down."""
        magick._get_image_size_output = self.old_function

    def test_correct_output(self):
        """Test for correct output."""
        magick._get_image_size_output = correct_output
        size = magick.get_image_size('stub')
        self.assertEqual(size, '40x40')

    def test_incorrect_output(self):
        """Test for incorrect output."""
        magick._get_image_size_output = incorrect_output
        size = magick.get_image_size('stub')
        self.assertIsNone(size)
# pylint: enable=protected-access
