"""Configuration class for icons updating."""

import os
from configparser import ConfigParser


_DESTINATION_NAME = 'dst'
_MAGICK_NAME = 'path'
_SOURCES_NAME = 'src'


class Config:
    """Configuration class."""

    def __init__(self, config_file=None, src=None, dst=None):
        """Constructor."""
        parser = ConfigParser()
        if config_file:
            parser.read(config_file)
        section = parser['settings'] if config_file else None
        if config_file and _MAGICK_NAME in section:
            os.environ['PATH'] += os.pathsep + \
                                  os.path.abspath(section[_MAGICK_NAME])
        if not src and config_file:
            src = section[_SOURCES_NAME]
        elif not src:
            raise RuntimeError('Source folder should be set!')
        self._src = os.path.normpath(src)
        if not dst and config_file:
            dst = section[_DESTINATION_NAME]
        elif not dst:
            raise RuntimeError('Destination folder should be set!')
        self._dst = os.path.normpath(dst)
        assert self._dst, 'Destination folder should be set!'
        assert self._src, 'Sources folder should be set!'

    def destination(self):
        """Destination folder."""
        return self._dst

    def sources(self):
        """Sources folder."""
        return self._src
