"""ImageMagick wrapper."""


import re
import subprocess


RX_IMAGE_SIZE = re.compile(r'\d+x\d+')


def _get_image_size_output(filename):
    """Get image size output."""
    cmd = ['identify', '-ping', '-format', '%wx%h', filename]
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, _stderr = proc.communicate()
    return stdout.decode()


def get_image_size(filename):
    """Get image size."""
    output = _get_image_size_output(filename)
    match = RX_IMAGE_SIZE.fullmatch(output)
    return match.group(0) if match else None
