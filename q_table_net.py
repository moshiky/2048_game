
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from consts import Consts


class QTableNet:

    def __init__(self, logger):
        self.__logger = logger

        # define learning parameters
        self.__max_train_epochs = 100
        self.__batch_size = 10
        self.__train_target_accuracy = 0.7

        self.__learning_rate = 0.1
        self.__decay = 1e-5
        self.__momentum = 0.03

        # initiate net member
        self.__net = self.__create_net()

    def __create_net(self):
        # build model
        model = Sequential()
        model.add(Dense(input_shape=(17,), units=34, activation='relu'))
        model.add(Dense(34, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # compile model
        sgd_optimizer = SGD(lr=self.__learning_rate, decay=self.__decay, momentum=self.__momentum)
        model.compile(loss='mean_squared_error', optimizer=sgd_optimizer, metrics=['accuracy'])

        # return model
        return model

    def train(self, x_train, y_train):# x_samples, y_samples):
        # x_samples array element structure:
        # np array, shape= (18), 17 first cells are the state, last one is the action

        # split sets to train and test sets
        # x_train, x_test, y_train, y_test = train_test_split(x_samples, y_samples, test_size=0.3, random_state=None)

        # train net using samples
        for i in range(self.__max_train_epochs):
            self.__logger.log('epoch #{epoch_id}'.format(epoch_id=i))
            train_history = self.__net.fit(x_train, y_train, nb_epoch=1, batch_size=self.__batch_size)
            if train_history.history['acc'][-1] > self.__train_target_accuracy:
                break

        # # log net accuracy
        # net_accuracy = self.__net.evaluate(x_test, y_test)
        # self.__logger.log('net accuracy: {accuracy}'.format(accuracy=net_accuracy))

    def predict(self, state, action):
        # convert params to net input structure
        state_action = np.append(state, Consts.ACTION_CODES[action])

        # return net prediction (=expected return for (s,a))
        return self.__net.predict(state_action.reshape(1, len(state_action)))[0][0]
