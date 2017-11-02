
import msvcrt
from iplayer import IPlayer
from consts import Consts


class HumanPlayer(IPlayer):

    def a__get_selected_action(self, board):
        # print current board state
        board.print_board()

        # let the player choose next action
        while True:
            # read key stroke
            pressed_key = msvcrt.getch()

            # check for Ctrl+C
            if pressed_key == b'\x03':
                raise Exception('Keyboard interrupt (Ctrl+C)')

            # check if this is arrow key prefix
            if pressed_key == b'\xe0':
                # get next key (should be an arrow)
                pressed_key = msvcrt.getch()

            # verify the key is supported
            if pressed_key in Consts.KEY_TO_ACTION_MAP.keys():
                # map key to related action
                selected_action = Consts.KEY_TO_ACTION_MAP[pressed_key]

                # log selected action
                self.__logger.log(selected_action)

                return selected_action
