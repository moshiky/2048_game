
import numpy as np
import random
from consts import Consts


class Board:

    def __init__(self, logger, board_size=Consts.BOARD_SIZE):

        # store sent logger
        self.__logger = logger

        # store board size
        self.__board_size = board_size

        # init score counter
        self.__current_score = 0

        # init board cells to empty cells
        self.__board = \
            [
                [Consts.EMPTY_CELL_VALUE for i in range(self.__board_size)]
                for j in range(self.__board_size)
            ]

        # initiate board with two cells
        self.add_random_cell()
        self.add_random_cell()

    def __get_random_empty_cell_coordinates(self):
        while True:
            i = random.randrange(self.__board_size)
            j = random.randrange(self.__board_size)
            if self.__board[i][j] == Consts.EMPTY_CELL_VALUE:
                return i, j

    @staticmethod
    def __get_new_cell_value():
        if random.randrange(10) == 0:
            return 4
        else:
            return 2

    def add_random_cell(self):
        if self.__has_empty_cells():
            i, j = self.__get_random_empty_cell_coordinates()
            self.__board[i][j] = self.__get_new_cell_value()

    def perform_action(self, action):

        cells_merged = False
        state_changed = False

        if action == Consts.ACTION_UP:
            for j in range(0, self.__board_size):
                for i in range(1, self.__board_size):
                    cells_merged, last_state_changed = self.__move_cell(i, j, action, cells_merged)
                    state_changed = state_changed or last_state_changed

        if action == Consts.ACTION_DOWN:
            for j in range(0, self.__board_size):
                for i in range(self.__board_size-2, -1, -1):
                    cells_merged, last_state_changed = self.__move_cell(i, j, action, cells_merged)
                    state_changed = state_changed or last_state_changed

        if action == Consts.ACTION_LEFT:
            for i in range(0, self.__board_size):
                for j in range(1, self.__board_size):
                    cells_merged, last_state_changed = self.__move_cell(i, j, action, cells_merged)
                    state_changed = state_changed or last_state_changed

        if action == Consts.ACTION_RIGHT:
            for i in range(0, self.__board_size):
                for j in range(self.__board_size-2, -1, -1):
                    cells_merged, last_state_changed = self.__move_cell(i, j, action, cells_merged)
                    state_changed = state_changed or last_state_changed

        return state_changed

    def __move_cell(self, i, j, action, last_cells_merged):

        # move occupied cells only
        if self.__board[i][j] == Consts.EMPTY_CELL_VALUE:
            # cells not united and state not changed
            return False, False

        # initiate local variables
        keep_looking = True
        current_i = i
        current_j = j

        # set coordinates intervals according to selected action
        i_interval = \
            -1 if action == Consts.ACTION_UP else 1 if action == Consts.ACTION_DOWN else 0
        j_interval = \
            -1 if action == Consts.ACTION_LEFT else 1 if action == Consts.ACTION_RIGHT else 0

        # search for farthest empty cell
        while keep_looking:

            target_i = current_i + i_interval
            target_j = current_j + j_interval

            if -1 < target_i < self.__board_size and -1 < target_j < self.__board_size \
                    and self.__board[target_i][target_j] == Consts.EMPTY_CELL_VALUE:
                current_i = target_i
                current_j = target_j

            else:
                keep_looking = False

        # try to unite similar cells
        if not last_cells_merged:

            # calculate the coordinates of next cell is selected action direction
            next_cell_i = current_i + i_interval
            next_cell_j = current_j + j_interval

            # check whether next cell value is the same like source cell value and unite
            # if it is
            if -1 < next_cell_i < self.__board_size and -1 < next_cell_j < self.__board_size \
                    and self.__board[i][j] == self.__board[next_cell_i][next_cell_j]:
                self.__board[next_cell_i][next_cell_j] *= 2
                self.__board[i][j] = Consts.EMPTY_CELL_VALUE
                self.__current_score += self.__board[next_cell_i][next_cell_j]

                # cells united and state has changed
                return True, True

        # move cell if has where to move
        if abs(current_i - i) > 0 or abs(current_j - j) > 0:
            self.__board[current_i][current_j] = self.__board[i][j]
            self.__board[i][j] = Consts.EMPTY_CELL_VALUE

            # cells not united but state has changed
            return False, True

        else:
            # cells not united and state not changed
            return False, False

    def get_largest_cell_value(self):
        max_cell_value = 0
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__board[i][j] > max_cell_value:
                    max_cell_value = self.__board[i][j]

        return max_cell_value

    def __is_board_contains_value(self, cell_value):
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__board[i][j] == cell_value:
                    return True
        return False

    def __has_empty_cells(self):
        return self.__is_board_contains_value(Consts.EMPTY_CELL_VALUE)

    def is_win_state(self):
        return self.__is_board_contains_value(Consts.WIN_CELL_VALUE)

    def is_game_over(self):
        # game is over only in case there is no more empty cells
        if self.__has_empty_cells():
            return False

        # game is over only in case there is no more identical neighbors
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                if self.__has_identical_neighbors(i, j):
                    return False

        # no action is possible
        return True

    def __is_coordinates_valid(self, i, j):
        return -1 < i < self.__board_size and -1 < j < self.__board_size

    def __has_identical_neighbors(self, i, j):

        for i_interval in range(-1, 2):
            for j_interval in range(-1, 2):
                # check the four possible action directions and skip all others
                if abs(i_interval + j_interval) != 1:
                    continue

                # calculate target cell coordinates
                target_i = i + i_interval
                target_j = j + j_interval

                if self.__is_coordinates_valid(target_i, target_j) \
                        and self.__board[i][j] == self.__board[target_i][target_j]:
                    return True

        # no similar neighbors found
        return False

    def print_board(self):
        # initiate string
        board_as_text = '\n'

        # build board string
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                board_as_text += str(self.__board[i][j]) + '\t'
            board_as_text += '\n'

        # log board state and score
        self.__logger.log(board_as_text + 'current score: {board_score}'.format(board_score=self.__current_score))

    def get_current_score(self):
        return self.__current_score

    def vectorize_board(self):
        board_vector = np.zeros((self.__board_size * self.__board_size), dtype=np.float32)
        for i in range(self.__board_size):
            for j in range(self.__board_size):
                board_vector[i * self.__board_size + j] = self.__board[i][j] / float(Consts.WIN_CELL_VALUE)

        return board_vector
