"""File name parsing module."""


import os
import re


RX_MULTIPLIER = re.compile(r'@(\d)x')  # @2x or @3x
# for base names
RX_SIZE_RULES = [
    re.compile(r'((?:\d|\.)+)x((?:\d|\.)+)'),  # 76x76 or 83.5x83.5
    re.compile(r'((?:\d|\.)+)(?:@\dx)?$'),     # Icon-40@2x.png or img_1024.png
]


def get_image_size(filename: str):
    """Build description from file name.

    Examples:
    >>> get_image_size('Icon-76x76.png')
    '76x76'
    >>> get_image_size('Icon-76x76@2x.png')
    '152x152'
    >>> get_image_size('Icon-83.5x83.5@2x.png')
    '167x167'
    >>> get_image_size('Icon-40@2x.png')
    '80x80'
    >>> get_image_size('ololo_1024.png')
    '1024x1024'
    """
    basename, _ = os.path.splitext(filename)

    match = RX_MULTIPLIER.search(basename)
    multiply = int(match.group(1)) if match else 1

    width = None
    height = None
    for regexp in RX_SIZE_RULES:
        match = regexp.search(basename)
        if match:
            groups = match.groups()
            count = len(groups)
            if count > 1:
                width = int(float(groups[0]) * multiply)
                height = int(float(groups[1]) * multiply)
            else:
                width = height = int(float(groups[0]) * multiply)
            break

    if width and height:
        return 'x'.join(map(str, [width, height]))

    return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
