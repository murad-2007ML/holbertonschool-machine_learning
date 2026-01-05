#!/usr/bin/env python3
"""remove NaN"""


def high(df):
    """remove NaN"""
    return df.dropna(subset=["Close"], inplace=False)
