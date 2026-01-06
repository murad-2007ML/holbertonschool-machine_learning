#!/usr/bin/env python3
"""concat indexses with a multiindex"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearranges the MultiIndex so that Timestamp is the first level.
    Concatenates bitstamp and coinbase from 1417411980 to 1417417980.
    """
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1.loc[1417411980:1417417980]
    df2 = df2.loc[1417411980:1417417980]

    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.swaplevel(0, 1).sort_index()

    return df
