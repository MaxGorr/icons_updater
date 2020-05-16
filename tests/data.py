"""Test data."""

# Input file names from the real case
INPUT = [
    'Icon-29x29.png', 'Icon-29x29@2x.png', 'Icon-29x29@3x.png',
    'icon-40@2x.png', 'Icon-40x40.png',
    'Icon-40x40@2x.png', 'Icon-40x40@3x.png',
    'Icon-60x60@2x.png', 'Icon-60x60@3x.png',
    'Icon-76x76.png', 'Icon-76x76@2x.png',
    'Icon-83.5x83.5@2x.png',
    'wtf_Icon_58update 1024.png',
]

SIZES = {
    'Icon-29x29.png': '29x29',
    'Icon-29x29@2x.png': '58x58',
    'Icon-29x29@3x.png': '87x87',
    'icon-40@2x.png': '80x80',
    'Icon-40x40.png': '40x40',
    'Icon-40x40@2x.png': '80x80',
    'Icon-40x40@3x.png': '120x120',
    'Icon-60x60@2x.png': '120x120',
    'Icon-60x60@3x.png': '180x180',
    'Icon-76x76.png': '76x76',
    'Icon-76x76@2x.png': '152x152',
    'Icon-83.5x83.5@2x.png': '167x167',
    'wtf_Icon_58update 1024.png': '1024x1024',
}

RESULT = [
    'AppIcon1024.png',

    'AppIcon29x29.png', 'AppIcon29x29@2x.png', 'AppIcon29x29@2x~ipad.png',
    'AppIcon29x29@3x.png', 'AppIcon29x29~ipad.png',

    'AppIcon40x40@2x.png', 'AppIcon40x40@2x~ipad.png', 'AppIcon40x40@3x.png',
    'AppIcon40x40~ipad.png',

    'AppIcon60x60@2x.png', 'AppIcon60x60@3x.png',

    'AppIcon76x76@2x~ipad.png', 'AppIcon76x76~ipad.png',

    'AppIcon83.5x83.5@2x~ipad.png',
]

CANDIDATES = {
    'AppIcon1024.png'         : {'wtf_Icon_58update 1024.png'},
    'AppIcon29x29.png'        : {'Icon-29x29.png'},
    'AppIcon29x29@2x.png'     : {'Icon-29x29@2x.png'},
    'AppIcon29x29@2x~ipad.png': {'Icon-29x29@2x.png'},
    'AppIcon29x29@3x.png'     : {'Icon-29x29@3x.png'},
    'AppIcon29x29~ipad.png'   : {'Icon-29x29.png'},
    'AppIcon40x40@2x.png'     : {'icon-40@2x.png', 'Icon-40x40@2x.png'},
    'AppIcon40x40@2x~ipad.png': {'icon-40@2x.png', 'Icon-40x40@2x.png'},
    'AppIcon40x40@3x.png'     : {'Icon-40x40@3x.png', 'Icon-60x60@2x.png'},
    'AppIcon40x40~ipad.png'   : {'Icon-40x40.png'},
    'AppIcon60x60@2x.png'     : {'Icon-40x40@3x.png', 'Icon-60x60@2x.png'},
    'AppIcon60x60@3x.png'     : {'Icon-60x60@3x.png'},
    'AppIcon76x76@2x~ipad.png': {'Icon-76x76@2x.png'},
    'AppIcon76x76~ipad.png'   : {'Icon-76x76.png'},
    'AppIcon83.5x83.5@2x~ipad.png': {'Icon-83.5x83.5@2x.png'},
}

BEST_CHOICE = {
    'AppIcon1024.png'         : 'wtf_Icon_58update 1024.png',
    'AppIcon29x29.png'        : 'Icon-29x29.png',
    'AppIcon29x29@2x.png'     : 'Icon-29x29@2x.png',
    'AppIcon29x29@2x~ipad.png': 'Icon-29x29@2x.png',
    'AppIcon29x29@3x.png'     : 'Icon-29x29@3x.png',
    'AppIcon29x29~ipad.png'   : 'Icon-29x29.png',
    'AppIcon40x40@2x.png'     : 'Icon-40x40@2x.png',
    'AppIcon40x40@2x~ipad.png': 'Icon-40x40@2x.png',
    'AppIcon40x40@3x.png'     : 'Icon-40x40@3x.png',
    'AppIcon40x40~ipad.png'   : 'Icon-40x40.png',
    'AppIcon60x60@2x.png'     : 'Icon-60x60@2x.png',
    'AppIcon60x60@3x.png'      : 'Icon-60x60@3x.png',
    'AppIcon76x76@2x~ipad.png' : 'Icon-76x76@2x.png',
    'AppIcon76x76~ipad.png'    : 'Icon-76x76.png',
    'AppIcon83.5x83.5@2x~ipad.png' : 'Icon-83.5x83.5@2x.png',
}
