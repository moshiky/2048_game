
from random import randrange
from iplayer import IPlayer
from consts import Consts


class RandomPlayer(IPlayer):

    def a__get_selected_action(self, board):
        # print current board state
        # board.print_board()

        # return random action
        return list(Consts.KEY_TO_ACTION_MAP.values())[randrange(Consts.NUMBER_OF_ACTIONS)]
