"""Verbose tools."""

VERBOSE = False


def decorate(string):
    """Decorate output."""
    if VERBOSE:
        size = len(string) + 6
        print(size * '-')
        print(f'-- {string} --')
        print(size * '-')


def print_data(data):
    """Print ImageData list."""
    if VERBOSE:
        string_list = list(map(str, data))
        print('\n'.join(string_list))


def set_verbose(verbose_value: bool):
    """Set verbose level."""
    global VERBOSE
    VERBOSE = verbose_value


def vprint(*var_list, **var_dict):
    """Wrapper for print function."""
    if VERBOSE:
        print(*var_list, **var_dict)
