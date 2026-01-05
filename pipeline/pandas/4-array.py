#!/usr/bin/env python3
"""high and close"""
import numpy as np


def array(df):
    """high and close"""
    return df[["High", "Close"]].tail(10).to_numpy
