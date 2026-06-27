import yfinance as yf
import pandas as pd
from config import TICKERS
from database import get_connection

def download_stock_data():
    stock_data = []
    for ticker in TICKERS:
        stock = yf.download(ticker, start="2021-01-01", end=None)
        stock.reset_index(inplace=True) #this makes date a column instead of index
        stock["Ticker"] = ticker
        stock_data.append(stock)
    return pd.concat(stock_data) #so that all data is in one dataframe
def save_to_db(df):
    conn = get_connection()
    df.to_sql("stock_prices", conn, if_exists="replace", index=False)

if __name__ == "__main__":
    stock_data = download_stock_data()
    save_to_db(stock_data)