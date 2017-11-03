
import numpy as np
from consts import Consts


class QLearnAgent:

    def __init__(self, logger, q_table, alpha=0.1, gamma=0.9):
        self.__logger = logger

        # set learning params
        self.__alpha = alpha
        self.__gamma = gamma

        # create q net
        self.__q_table = q_table

        # initiate samples set
        self.__inputs = None
        self.__outputs = np.array([])

    def add_sample(self, updated_state, updated_action, reward, next_state, is_final_state):
        # we want to calculate build sample in the such form:
        #   x (net input)   =   (s, a)
        #   y (net output)  =   Q(s, a) + alpha*(r + gamma*(max_a' Q(s',a')) - Q(s,a))

        # calculate max_a' Q(s',a')
        if not is_final_state:
            max_st_at = None
            for action in Consts.ACTION_CODES.keys():
                pair_value = self.__q_table.predict(next_state, action)

                if max_st_at is None or pair_value > max_st_at:
                    max_st_at = pair_value
        else:
            max_st_at = 0.0

        # calculate Q(s,a)
        q_s_a = self.__q_table.predict(updated_state, updated_action)

        # calculate y
        expected_value = q_s_a + self.__alpha * (reward + self.__gamma * max_st_at - q_s_a)

        # add sample
        updated_state_action = np.append(updated_state, Consts.ACTION_CODES[updated_action])

        if self.__inputs is None:
            self.__inputs = updated_state_action.reshape(1, len(updated_state_action))

        else:
            if len(self.__inputs) == Consts.TRAJECTORY_MAX_LENGTH:
                self.__inputs = self.__inputs[Consts.SHRINK_FACTOR:]
                self.__outputs = self.__outputs[Consts.SHRINK_FACTOR:]

            self.__inputs = np.vstack([self.__inputs, updated_state_action])

        self.__outputs = np.append(self.__outputs, [expected_value])

        # train table
        if len(self.__inputs) > int(0.2 * Consts.TRAJECTORY_MAX_LENGTH):
            self.__train_table()

    def __train_table(self):
        if self.__inputs is not None and len(self.__inputs) > 0:
            self.__q_table.train(self.__inputs, self.__outputs)
