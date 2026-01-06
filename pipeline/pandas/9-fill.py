#!/usr/bin/env python3
"""filling miss values"""


def fill(df):
    """
    Removes the Weighted_Price column.
    Fills missing values in the Close column with the previous row value.
    Fills missing values in the High, Low, and Open columns with the
    corresponding Close value in the same row.
    Sets missing values in Volume_(BTC) and Volume_(Currency) to 0.
    Returns: the modified pd.DataFrame.
    """
    df.drop(columns=["Weighted_Price"], inplace=True)

    df["Close"] = df["Close"].fillna(method="pad")
    df["High"] = df["High"].fillna(df["Close"])
    df["Low"] = df["Low"].fillna(df["Close"])
    df["Open"] = df["Open"].fillna(df["Close"])

    vols = ["Volume_(BTC)", "Volume_(Currency)"]
    df[vols] = df[vols].fillna(0)

    return df
