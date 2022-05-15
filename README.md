# icons\_updater

__icons_updater__ - is a small utility for updating project icons. In some cases a customer might provide icons in a wrong format, wrong sizes or wrong names. This utility helps to solve problems connected with the last case.

## Usage

To find the most suitable icon, it is required to find icon's size. There are two ways for __icons_updater__ to reach this purpose:

- using [__ImageMagick__][magick] tool,
- using filename parsing.

The biggest filename parsing's advantage is that no third party tools are required. For example, in __iOS__ applications the icon size is encoded in filenames: `icon_16x16.png` or `icon_16x16@2x.png`. Originally the tool was made for this platform.

__ImageMagick__ is used by default. This tool is universal, but requires an individual installation and additional settings, if it is not in the system paths.

There are two ways to pass the parameters to __icons_updater__:

- through arguments;
- through a configuration file, which is also passed as an argument.

Arguments has a higher priority than parameters from the configuration file.

### Arguments

Following arguments are supported:

- `--config`, `-c` - configuration file path;
- `--destination`, `-d` - folder with project's icons;
- `--source`, `-s` - folder with new icons;
- `--name-parser`, `-n` - use filename parsing.

### Configuration file

The single section is __settings__. Following settings are available:

- `path` - path to __ImageMagick__ (if __ImageMagick__ is not in the system paths);
- `dst` - path to project's icons;
- `src` - path to new icons.

### Examples

The configuration file is not used, and __ImageMagick__ is not in the system paths:

```bash
>> cd path/to/data/icons
>> add_to_path path/to/apps/imagemagick
>> python -m icons_updater -d path/to/projects/cool_game/icons -s icons_for_new_version
```

The same with configuration file using. File:

```ini
[settings]

path = path/to/apps/imagemagick
dst = path/to/projects/cool_game/icons
```

Commands:

```bash
>> cd path/to/data/icons
>> python -m icons_updater -c cool_game.cfg -s icons_for_new_version
```

[magick]: https://imagemagick.org/
