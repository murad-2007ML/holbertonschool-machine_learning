#!/usr/bin/env python3
"""remove NaN"""
import pandas as pd


def high(df):
    """remove NaN"""
    return df.dropna(subset=["Close"], inplace=False)
