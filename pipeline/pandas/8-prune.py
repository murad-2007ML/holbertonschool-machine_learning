#!/usr/bin/env python3
"""remove NaN"""


def prune(df):
    """remove NaN"""
    df = df.dropna(subset=["Close"])
    return df
