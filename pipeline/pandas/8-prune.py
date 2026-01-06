#!/usr/bin/env python3
"""remove NaN"""


def high(df):
    """remove NaN"""
    df = df.dropna(subset=["Close"])
    return df.head()
