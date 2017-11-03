
import abc


class IPlayer(object, metaclass=abc.ABCMeta):

    def __init__(self, logger):
        self.__logger = logger

    @abc.abstractmethod
    def a__get_selected_action(self, board):
        raise NotImplementedError('__get_selected_action')

    def act(self, board):
        # let the player choose next action
        selected_action = self.a__get_selected_action(board)

        # apply the selected action on the board and return its return value-
        # whether the board state changed or not
        return selected_action, board.perform_action(selected_action)
