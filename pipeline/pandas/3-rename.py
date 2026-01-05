#!/usr/bin/env python3
"""taking input and performing"""
import pandas as pd

df = df.rename(columns={'Timestamp': "Datetime"})
df['Datetime'] = pd.date_time(df['Datetime'], unit='s')
df = df.loc[:, ['Datetime', 'Close']]
print(df.tail())
