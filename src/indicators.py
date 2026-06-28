import pandas as pd
def calculate_returns(df):
    df["Daily Returns"]=df.groupby("Ticker")["Close"].pct_change()
    return df
def moving_average(df, window=50):
    df["MA"] = df.groupby("Ticker")["Close"].rolling(window).mean().reset_index(level=0, drop=True)
    return df