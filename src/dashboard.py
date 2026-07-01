import streamlit as st
import pandas as pd
import plotly.express as px
from config import TICKERS
st.title("ISA Portfolio Optimiser")
st.write("This application allows you to optimise your ISA portfolio using historical stock price data.")
st.sidebar.header("Settings")
#input ticker
st.sidebar.subheader("Select ETFs")
tickers = st.sidebar.multiselect("Tickers", options=TICKERS, default=["AAPL", "MSFT", "GOOGL", "AMZN"])
risk=st.sidebar.slider(
    "Risk tolerance",
    1,
    10,
    5
)
