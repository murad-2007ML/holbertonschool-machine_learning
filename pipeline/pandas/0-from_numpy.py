#!/usr/bin/env python3
import pandas as pd


def from_numpy(array):
    """creating dataFrame from array"""
    c_list = list('ABCDEFGH')
    reshape = c_list[:array.shape[1]]
    return pd.DataFrame(array, columns=reshape)
