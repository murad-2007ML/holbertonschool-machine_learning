#!/usr/bin/env python3
"""taking input and performing"""
import pandas as pd


def rename(df):
    """taking input and performing"""
    df = df.rename(columns={'Timestamp': "Datetime"})
    df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')
    df = df.loc[:, ['Datetime', 'Close']]
    print(df.tail())
