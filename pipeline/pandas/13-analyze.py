#!/usr/bin/env python3
"""computing describtive statistics"""
import pandas as pd


def analyze(df):
    """Computes descriptive statistics for all columns except the Timestamp column.
    Returns a new pd.DataFrame containing these statistics
    """
    df = df.drop(columns="TimeStamp").describe()
    return df
