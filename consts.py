
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

    TRAJECTORY_MAX_LENGTH = 1e5
    SHRINK_FACTOR = 1e2

    ACTION_CODES = {
        ACTION_UP: 0.0,
        ACTION_DOWN: 0.25,
        ACTION_LEFT: 0.5,
        ACTION_RIGHT: 1.0
    }
