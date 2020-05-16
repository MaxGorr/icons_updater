"""Image description module."""


import difflib
import os
from typing import List

from . import verbose_tools as vt


def find_all(targets: List['ImageData'], candidates: List['ImageData']):
    """Find the best candidate for each target."""
    result = dict()
    vt.decorate('processing')
    for target in targets:
        vt.vprint(f'Target: {target}')
        filtered = target.filter_candidates(candidates)
        vt.vprint(f'- Filtered: {filtered}')
        best = target.choose(filtered)
        result[target.filename] = best
    return result


class ImageData:
    """Image data."""
    filename: str   # filename.ext
    extension: str  # ext
    size: str       # YYxZZ

    def __init__(self, filename, size):
        """Constructor."""
        self.filename = filename
        self.extension = os.path.splitext(filename)[1][1:]
        self.size = size

    def __repr__(self):
        """Representation."""
        return '::'.join([self.filename, self.size])

    def __str__(self):
        """String cast."""
        return self.filename

    def choose(self, candidates: List['ImageData']):
        """Choose the best candidate."""
        count = len(candidates)
        if count == 0:
            return None
        if count == 1:
            return candidates[0].filename

        filenames = list(map(lambda x: x.filename, candidates))
        best = difflib.get_close_matches(str(self), filenames)
        return best[0] if best else None

    def equal(self, that: 'ImageData'):
        """Compare image data.

        Returns true if images have the same extension and size.
        """
        return (self.extension == that.extension and
                self.size == that.size)

    def filter_candidates(self, candidates: List['ImageData']):
        """Filter candidates."""
        return list(filter(self.equal, candidates))
