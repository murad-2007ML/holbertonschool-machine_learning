#!/usr/bin/env python3
'''
creating new layers
'''

import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambd):
    """
    prev is a tensor containing the output of the previous layer
    n is the number of nodes the new layer should contain
    activation is the activation function that should be used on the layer
    lambtha is the L2 regularization parameter
    """
    layer = tf.keras.layers.Dense(
        n,
        activation=activation
        kernel_initializer=tf.keras.initializers.VarianceScaling(
            scale=2.0,
            mode='fan_avg'
        ),
    kernel_regularizer=tf.keras.regularizers.L2(lambd)
    )
    return layer(prev)
