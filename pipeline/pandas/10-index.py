#!/usr/bin/env python3
"""setting new index"""


def index(df):
    """
    Sets the Timestamp column as the index of the dataframe.
    Returns: the modified pd.DataFrame.
    """
    df = df.set_index("Timestamp")
    return df
