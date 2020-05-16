"""Make test images."""

import os
import sys

from PIL import Image, ImageDraw


FILE_NAME = 'image.png'
OFFSET = 5
SIZES = [
    40, 60, 80
]


def draw_image(file_name, size, is_new=True, is_opaque=False):
    """Draw image."""
    mode = 'RGB' if is_opaque else 'RGBA'
    image = Image.new(mode, (size, size), 'yellow')
    draw = ImageDraw.Draw(image)
    ellipse = (OFFSET, OFFSET, size-OFFSET, size-OFFSET)
    color = 'green' if is_new else 'red'
    draw.ellipse(ellipse, fill=color)
    image.save(file_name)


def path():
    """Get path."""
    return os.path.dirname(__file__)


def _main():
    """Entry point."""
    new_dir = os.path.join(path(), 'new')
    old_dir = os.path.join(path(), 'old')
    os.makedirs(new_dir, exist_ok=True)
    os.makedirs(old_dir, exist_ok=True)
    for size in SIZES:
        new = os.path.join(new_dir, f'new_{size}.png')
        draw_image(new, size, True)
        old = os.path.join(old_dir, f'old_{size}.png')
        draw_image(old, size, False)


if __name__ == '__main__':
    sys.exit(_main())
