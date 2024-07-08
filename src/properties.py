from enum import Enum

class SIZES(int, Enum):
    CELL_WIDTH = 165
    CELL_HEIGHT = 165

class COLOR(str, Enum):
    GRAY =   '#758694'
    GREEN =  '#219C90'
    ORANGE = '#FFC700'
    RED =    '#EE4E4E'
    TILE_0 =    '#B7C4CF'
    TILE_2 =    '#D5A3A8'
    TILE_4 =    '#F38181'
    TILE_8 =    '#F8B286'
    TILE_16 =   '#FCE38A'
    TILE_32 =   '#F3F1AD'
    TILE_64 =   '#EAFFD0'
    TILE_128 =  '#EAFFD0'
    TILE_256 =  '#C0F0D2'
    TILE_512 =  '#95E1D3'
    TILE_1024 = '#7CC2B5'
    TILE_2048 = '#62A296'
    TEXT_1 =     '#2E333C'
    BACKGROUND = '#222831'
    FOREGROUND = '#393E46'
    ACCENT =     '#FFD369'
    TEXT_2 =     '#EEEEEE'
