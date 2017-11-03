
import numpy as np
from random import randrange
from iplayer import IPlayer
from consts import Consts


class AIPlayer(IPlayer):

    def __init__(self, logger, q_net):
        # send logger to super class
        super().__init__(logger)

        # store Q function net
        self.__q_net = q_net

    def a__get_selected_action(self, board):

        # get current state
        current_state = board.vectorize_board()

        # check value function for each possible action
        highest_value = None
        best_action_list = list()
        for action in Consts.ACTION_CODES.keys():
            pair_value = self.__q_net.predict(current_state, action)

            if highest_value is None or pair_value >= highest_value:
                if highest_value is None or pair_value > highest_value:
                    best_action_list = list()
                    highest_value = pair_value
                best_action_list.append(action)

        # return one of best actions
        if highest_value is not None:
            return best_action_list[randrange(len(best_action_list))]

        else:
            return self.__get_random_action()

    @staticmethod
    def __get_random_action():
        return list(Consts.KEY_TO_ACTION_MAP.values())[randrange(Consts.NUMBER_OF_ACTIONS)]
