#!/usr/bin/env python3
"""script to visualize the pd.DataFrame"""

#The column Weighted_Price should be removed
df = df.drop(columns=["Weighted_Price"])

#Rename the column Timestamp to Date
df = df.rename(columns={"Timestamp": "Date"})

#Convert the timestamp values to date values
df["Date"] = df.to_datetime(df["Date"], unit="s")

#Index the data frame on Date
df = df.set_index("Date")

#Missing values in Close should be set to the previous row value
df["Close"] = df["Close"].fillna(method="pad")

#Missing values in High, Low, Open should be set to the same row’s Close value
df["High"] = df["High"].fillna(df["Close"])
df["Low"] = df["Low"].fillna(df["Close"])
df["Open"] = df["Open"].fillna(df["Close"])

#Missing values in Volume_(BTC) and Volume_(Currency) should be set to 0
df["Volume_(BTC)"] = df["Volume_(BTC)"].fillna(0)
df["Volume_(Currency)"] = df["Volume_(Currency)"].fillna(0)

#Plot the data from 2017 and beyond at daily intervals and group the values of the same day such that:
df_2017_beyond = df[df.index >= "2017"]

df_daily = df_2017_beyond.resample("D").agg(
    {
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum",
    }
)
df.plot()
plt.show()
