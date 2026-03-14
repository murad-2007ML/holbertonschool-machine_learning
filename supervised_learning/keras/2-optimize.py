#!/usr/bin/env python3
"""Script to implement ADAM optimization using keras"""

import tensorflow.keras as K


def optimize_model(network, alpha, beta1, beta2):
    """
    building neural networks with keras
    """
    ADAM = K.optimizers.Adam(lr=alpha, beta_1=beta1, beta_2=beta2)
    network.compile(optimizer=ADAM, loss='categorical_crossentropy',
                    metrics=["accuracy"])
    return None
