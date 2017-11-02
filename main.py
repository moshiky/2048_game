
import random
from logger import Logger
from board import Board
from human_player import HumanPlayer
from random_player import RandomPlayer


def main(logger):

    # init random module
    random.seed()

    # max iterations to run
    max_iterations_to_run = 100000

    # init statistic variables
    score_list = list()
    steps_list = list()
    largest_cell_dict = dict()
    wins_counter = 0

    # run episodes
    for i in range(max_iterations_to_run):

        # log new game started
        if i % 1000 == 0:
            logger.log('game #{game_id}'.format(game_id=i))

        # init local variables
        game_board = Board(logger)
        player = RandomPlayer(logger)
        steps_counter = 0

        # monitor game
        while not game_board.is_game_over():

            # let the player play
            state_changed = player.act(game_board)
            steps_counter += 1

            # check for win condition
            if game_board.is_win_state():
                break

            # in case the board changed- add one new cell
            if state_changed:
                game_board.add_random_cell()

        # print last board state
        # game_board.print_board()

        # print message
        # if game_board.is_win_state():
        #     logger.log('WIN!!')
        #     wins_counter += 1
        # else:
        #     logger.log('GAME OVER')

        # print game score
        game_score = game_board.get_current_score()
        largest_cell_value = game_board.get_largest_cell_value()

        # logger.log('game score: {game_score}'.format(game_score=game_score))
        # logger.log('total steps: {steps_counter}'.format(steps_counter=steps_counter))
        # logger.log('largest cell: {largest_cell_value}'.format(largest_cell_value=largest_cell_value))

        # store game statistics
        score_list.append(game_score)
        steps_list.append(steps_counter)

        if str(largest_cell_value) not in largest_cell_dict.keys():
            largest_cell_dict[str(largest_cell_value)] = 0
        largest_cell_dict[str(largest_cell_value)] += 1

    # print average score
    logger.log('-- statistics --')
    logger.log('avg. score: {avg_score}'.format(avg_score=sum(score_list) / float(len(score_list))))
    logger.log('avg. steps: {avg_steps}'.format(avg_steps=sum(steps_list) / float(len(steps_list))))
    logger.log('largest cells: {largest_cells}'.format(largest_cells=largest_cell_dict))
    logger.log('total wins: {wins}'.format(wins=wins_counter))


if __name__ == '__main__':

    # create logger
    main_logger = Logger()

    # run main
    main(main_logger)
