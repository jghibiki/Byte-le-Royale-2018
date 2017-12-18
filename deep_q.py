import tensorflow as tf
import numpy as np


class DeepQCombat:

    def __init__(self, lr, state_size, action_size):

        self.state_in = tf.placeholder(shape=[None, state_size], dtype=tf.float32, name="state_in")


        self.unit_1_hidden = tf.layers.dense(inputs=self.state_in,
                                             units=10,
                                             kernel_initializer=tf.ones_initializer(),
                                             bias_initializer=tf.zeros_initializer(),
                                             activation=tf.nn.relu)

        self.unit_1_output = tf.layers.dense(inputs=self.unit_1_hidden,
                                        units=action_size,
                                        kernel_initializer=tf.ones_initializer(),
                                        bias_initializer=tf.zeros_initializer(),
                                        activation=tf.nn.softmax)


        #self.unit_2_hidden = tf.layers.dense(inputs=self.state_in,
        #                                     units=10,
        #                                     kernel_initializer=tf.ones_initializer(),
        #                                     bias_initializer=tf.zeros_initializer(),
        #                                     activation=tf.nn.relu)

        #self.unit_2_output = tf.layers.dense(inputs=self.unit_2_hidden,
        #                                units=action_size,
        #                                kernel_initializer=tf.ones_initializer(),
        #                                bias_initializer=None,
        #                                activation=tf.nn.softmax)

        #self.unit_3_hidden = tf.layers.dense(inputs=self.state_in,
        #                                     units=10,
        #                                     kernel_initializer=tf.ones_initializer(),
        #                                     bias_initializer=tf.zeros_initializer(),
        #                                     activation=tf.nn.relu)

        #self.unit_3_output = tf.layers.dense(inputs=self.unit_3_hidden,
        #                                units=action_size,
        #                                kernel_initializer=tf.ones_initializer(),
        #                                bias_initializer=None,
        #                                activation=tf.nn.softmax)

        #self.unit_4_hidden = tf.layers.dense(inputs=self.state_in,
        #                                     units=10,
        #                                     kernel_initializer=tf.ones_initializer(),
        #                                     bias_initializer=tf.zeros_initializer(),
        #                                     activation=tf.nn.relu)

        #self.unit_4_output = tf.layers.dense(inputs=self.unit_4_hidden,
        #                                units=action_size,
        #                                kernel_initializer=tf.ones_initializer(),
        #                                bias_initializer=None,
        #                                activation=tf.nn.softmax)

        #self.unit_1_output = tf.reshape(self.unit_1_output, [-1])
        #self.unit_2_output = tf.reshape(self.unit_1_output, [-1])
        #self.unit_3_output = tf.reshape(self.unit_1_output, [-1])
        #self.unit_4_output = tf.reshape(self.unit_1_output, [-1])

        self.a = self.unit_1_output
        #self.b = self.unit_2_output
        #self.c = self.unit_3_output
        #self.d = self.unit_4_output

        self.unit_1_chosen_action = tf.argmax(self.unit_1_output, 1)
        #self.unit_2_chosen_action = tf.argmax(self.unit_2_output, 1)
        #self.unit_3_chosen_action = tf.argmax(self.unit_3_output, 1)
        #self.unit_4_chosen_action = tf.argmax(self.unit_4_output, 1)


        #self.combined_chosen_actions = tf.stack([
        #    self.unit_1_chosen_action,
        #    self.unit_2_chosen_action,
        #    self.unit_3_chosen_action,
        #    self.unit_4_chosen_action
        #], 0)

        self.target = tf.placeholder(shape=[None], dtype=tf.float32, name="target")

        self.unit_1_action = tf.placeholder(shape=[None, 5], dtype=tf.float32, name="unit_1_action")
        self.unit_2_action = tf.placeholder(shape=[None], dtype=tf.int32, name="unit_2_action")
        self.unit_3_action = tf.placeholder(shape=[None], dtype=tf.int32, name="unit_3_action")
        self.unit_4_action = tf.placeholder(shape=[None], dtype=tf.int32, name="unit_4_action")

        readout_action = tf.reduce_sum(tf.multiply(self.unit_1_output, self.unit_1_action), reduction_indices=1)
        self.loss = tf.reduce_mean(tf.square(self.target - readout_action))

        optimizer = tf.train.AdamOptimizer(learning_rate=lr)
        self.update = optimizer.minimize(self.loss)


