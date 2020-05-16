"""Entry point."""

import os
import shutil
import sys

from argparse import ArgumentParser

from . import image_data
from . import verbose_tools as vt
from .config import Config


def get_image_size_function(use_name_parser=False):
    """Get image size function."""
    if use_name_parser:
        from .name_parser import get_image_size
    else:
        from .magick import get_image_size

    return get_image_size


def process_file_list(folder_name, get_image_size, extension='.png'):
    """Process file list."""
    results = []
    for folder, _subfolders, files in os.walk(folder_name):
        for file in files:
            if file.endswith(extension):
                size = get_image_size(os.path.join(folder, file))
                results.append(image_data.ImageData(file, size))
        break
    return results


def _main():
    """Entry point."""
    parser = ArgumentParser(
        prog='python -m icons_updater',
        description='Update icons')
    parser.add_argument(
        '--config', '-c',
        help='Configuration file')
    parser.add_argument(
        '--destionation', '-d',
        help='Destination folder')
    parser.add_argument(
        '--source', '-s',
        help='Source folder')
    parser.add_argument(
        '--name-parser', '-n', action='store_true',
        help='Use name parser')
    parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Print detailed information')
    args = vars(parser.parse_args())
    vt.set_verbose(args['verbose'])

    config = Config(
        config_file=args.get('config', None),
        src=args.get('source', None),
        dst=args.get('destination', None)
    )

    get_image_size = get_image_size_function(args['name_parser'])

    vt.decorate('source folder')
    vt.vprint(config.sources())
    candidates = process_file_list(config.sources(), get_image_size)
    vt.decorate('candidates')
    vt.print_data(candidates)

    vt.decorate('destination folder')
    vt.vprint(config.destination())
    targets = process_file_list(config.destination(), get_image_size)
    vt.decorate('targets')
    vt.print_data(targets)

    result = image_data.find_all(targets, candidates)
    vt.decorate('result')
    for target, best_choice in result.items():
        src = os.path.join(config.sources(), best_choice)
        dst = os.path.join(config.destination(), target)
        print(f'Updated: {dst}\n    with >> {src}')
        shutil.copyfile(src, dst)


if __name__ == '__main__':
    sys.exit(_main())
