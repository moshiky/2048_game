
class Consts:

    BOARD_SIZE = 4

    EMPTY_CELL_VALUE = 0
    WIN_CELL_VALUE = 2048

    ACTION_UP = 'up'
    ACTION_DOWN = 'down'
    ACTION_LEFT = 'left'
    ACTION_RIGHT = 'right'

    KEY_TO_ACTION_MAP = {
        b'H': ACTION_UP,
        b'P': ACTION_DOWN,
        b'K': ACTION_LEFT,
        b'M': ACTION_RIGHT
    }

    NUMBER_OF_ACTIONS = 4
