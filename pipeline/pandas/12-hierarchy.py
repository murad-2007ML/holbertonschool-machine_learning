#!/usr/bin/env python3
"""concat indexses with a multiindex"""
index = __import__('10-index').index
import pandas as pd


def hierarchy(df1, df2):
    """
    Rearranges the MultiIndex so that Timestamp is the first level.
    Concatenates the bitstamp and coinbase tables from timestamps 1417411980 to 1417417980, inclusive.
    Adds keys to the data, labeling rows from df2 as bitstamp and rows from df1 as coinbase.
    Ensures the data is displayed in chronological order
    """
    df1 = df1.loc[
        (df1["Timestamp"] >= 1417411980) & (df1["Timestamp"]) <= 1417417980]
    df2 = df2.loc[
        (df2["Timestamp"] >= 1417411980) & (df2["Timestamp"]) <= 1417417980]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.sort_index()
    return df
