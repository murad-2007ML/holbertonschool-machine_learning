#!/usr/bin/env python3
"""Script to laber vector to one hot in Keras"""

import tensorflow.keras as K


def one_hot(labels, classes=None):
    """
    one_hot matrix
    """
    One_hot = K.utils.to_caterogical(labels, 
                                     num_classes=classes
                                     )
    return One_hot
