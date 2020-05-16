"""Test for descriptions."""

import unittest

from . import data
from .. import name_parser
from ..image_data import ImageData, find_all


def make_image_data(filename):
    """Make ImageData object."""
    size = name_parser.get_image_size(filename)
    return ImageData(filename, size)


class TestDescription(unittest.TestCase):
    """Test description module."""
    def setUp(self):
        """Set up tests."""
        self._data = {
            'Icon-29x29~ipad.png': ImageData('Icon-29x29~ipad.png', '29x29'),
            'Icon-40x40.png': ImageData('Icon-40x40.png', '40x40'),
            'icon-40@2x.png': ImageData('icon-40@2x.png', '80x80'),
            'Icon-40x40@2x~ipad.png': ImageData('Icon-40x40@2x~ipad.png',
                                                '80x80'),
            'Icon-40x40@2x.png': ImageData('Icon-40x40@2x.png', '80x80'),
            'Icon-40x40@3x.png': ImageData('Icon-40x40@3x.png', '120x120'),
            'Icon-60x60@2x.png': ImageData('Icon-60x60@2x.png', '120x120'),
            'Icon-83.5x83.5@2x.png': ImageData('Icon-83.5x83.5@2x.png',
                                               '167x167'),
            'Icon-83.5x83.5@2x~ipad.png': ImageData(
                'Icon-83.5x83.5@2x~ipad.png', '167x167'),
            'wtf_Icon_58update 1024.png': ImageData(
                'wtf_Icon_58update 1024.png', '1024x1024'),
        }

    def test_choose(self):
        """Test choose and filter_candidates functions."""
        input_data = list(map(make_image_data, data.INPUT))
        for result in data.RESULT:
            image = make_image_data(result)

            filtered = image.filter_candidates(input_data)
            filenames = set(map(lambda x: x.filename, filtered))
            self.assertEqual(filenames, data.CANDIDATES[result])

            best = image.choose(filtered)
            self.assertEqual(best, data.BEST_CHOICE[result])

    def test_equal(self):
        """Test for equal method."""
        datum1 = ImageData('Icon-40x40@2x.png', '80x80')
        data1_eq = [
            ImageData('icon-40@2x.png', '80x80'),
            ImageData('AppIcon40x40@2x.png', '80x80'),
            ImageData('AppIcon40x40@2x~ipad.png', '80x80'),
        ]
        for datum in data1_eq:
            self.assertTrue(datum1.equal(datum))

        datum2 = ImageData('Icon-40x40@3x.png', '80x80')
        data2_eq = [
            ImageData('icon-60@2x.png', '80x80'),
            ImageData('AppIcon60x60@2x.png', '80x80'),
            ImageData('AppIcon60x60@2x~ipad.png', '80x80'),
        ]
        for datum in data2_eq:
            self.assertTrue(datum2.equal(datum))

        data_neq = [
            ImageData('Icon-40x40.png', '40x40'),
            ImageData('Icon-83.5x83.5@2x.png', '167x167'),
            ImageData('azaza_Icon_58update 1024.png', '1024x1024')
        ]
        for datum in data_neq:
            self.assertFalse(datum1.equal(datum))
            self.assertFalse(datum2.equal(datum))

    def test_find_all(self):
        """Test find_all function."""
        targets = list(map(make_image_data, data.RESULT))
        candidates = list(map(make_image_data, data.INPUT))
        best = find_all(targets, candidates)
        self.assertEqual(best, data.BEST_CHOICE)
