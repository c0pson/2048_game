from enum import Enum

class SIZES(int, Enum):
    CELL_WIDTH = 165
    CELL_HEIGHT = 165

class COLOR(str, Enum):
    GRAY =   '#758694'
    GREEN =  '#219C90'
    ORANGE = '#FFC700'
    RED =    '#EE4E4E'
