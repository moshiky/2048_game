
from random import randrange
from iplayer import IPlayer
from consts import Consts


class AIPlayer(IPlayer):

    def __init__(self, logger, q_net):
        # send logger to super class
        super().__init__(logger)

        # store Q function net
        self.__q_net = q_net

        # initiate transitions set
        self.__transitions = list()

    def a__get_selected_action(self, board):
        # print current board state
        board.print_board()

        # say we have neural net
        # so take current state, check for each the actions which yields maximal value
        # what do we do for first cases? we keep trace of last X transitions and update the net using them (until
        # cross validation is over Y%)
        # until the transitions set is less than X - select random actions
        # after enough games the agent will learn the correct way to play

    @staticmethod
    def __get_random_action():
        return Consts.KEY_TO_ACTION_MAP.values()[randrange(Consts.NUMBER_OF_ACTIONS)]
