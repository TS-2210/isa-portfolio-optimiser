import pandas as pd
def ma_strategy(df):
    df["Signal"] = 0
    df.loc[df["Close"]>df["MA"], "Signal"] = 1 #buy signal
    df.loc[df["Close"]<df["MA"], "Signal"] = -1 #sell signal
    df["Strategy Returns"] = df["Signal"].shift(1)*df["Daily Returns"]
    cumulative_strategy_returns = (1+df["Strategy Returns"]).cumprod() #cumulative returns of strategy
    return cumulative_strategy_returns