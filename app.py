import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Define the index symbol for Bank Nifty on Yahoo Finance
symbol = "^NSEBANK"
st.header("Bank Nifty on Yahoo Finance : Standard deviation")
# Define the date range for the last month

button=st.button("Calculate")
if button:
  end_date = datetime.now()
  start_date = end_date - timedelta(days=30)

  # Fetch historical data for Bank Nifty
  data = yf.download(symbol, start=start_date, end=end_date)

  # Extract closing and opening prices
  closing_prices = data['Close'].values
  opening_prices = data['Open'].values

  # Calculate standard deviation for closing prices
  std_dev_closing = np.std(closing_prices)
  # Calculate standard deviation for opening prices
  std_dev_opening = np.std(opening_prices)
  st.write(f"Standard Deviation of Closing Prices: {std_dev_closing}")
  st.write(f"Standard Deviation of Opening Prices: {std_dev_opening}")
  st.dataframe(data[['Open', 'Close']])
