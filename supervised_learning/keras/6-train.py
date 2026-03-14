#!/usr/bin/env python3
'''training data'''


import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, verbose=True, shuffle=False,
                validation_data=None, early_stopping=False,
                patience=0):
    callbacks = []
    if validation_data and early_stopping:
        early_stop = K.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=patience,
            verbose=verbose
        )
        callbacks.append(early_stop)
    history = network.fit(
        x=data,
        y=labels,
        batch_size=batch_size,
        epochs=epochs,
        verbose=verbose,
        validation_data=validation_data,
        shuffle=shuffle
    )
    return history
