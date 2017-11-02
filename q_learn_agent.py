
import numpy as np
from q_table_net import QTableNet
from consts import Consts


class QLearnAgent:

    def __init__(self, logger, alpha=0.1, gamma=0.9):
        self.__logger = logger

        # set learning params
        self.__alpha = alpha
        self.__gamma = gamma

        # create q net
        raise Exception('NOT REALLY WORKING')
        self.__q_table = QTableNet(logger)

        # initiate samples set
        self.__samples = list()

    def add_sample(self, updated_state, updated_action, reward, next_state):
        # we want to calculate build sample in the such form:
        #   x (net input)   =   (s, a)
        #   y (net output)  =   Q(s, a) + alpha*(r + gamma*(max_a' Q(s',a')) - Q(s,a))

        # calculate max_a' Q(s',a')
        max_st_at = None
        for action in Consts.ACTION_CODES.keys():
            pair_value = self.__q_table.predict(next_state, action)

            if pair_value > max_st_at or max_st_at is None:
                max_st_at = pair_value

        # calculate Q(s,a)
        q_s_a = self.__q_table.predict(updated_state, updated_action)

        # calculate y
        expected_value = q_s_a + self.__alpha * (reward + self.__gamma * max_st_at - q_s_a)

        # add sample
        updated_state_action = np.append(updated_state, Consts.ACTION_CODES[updated_action])
        if len(self.__samples) == Consts.TRAJECTORY_MAX_LENGTH:
            self.__samples = self.__samples[Consts.SHRINK_FACTOR:]

        self.__samples.append((updated_state_action, expected_value))

        # train table
        self.__train_table()

    def __train_table(self):
        self.__q_table.train(self.__samples)
