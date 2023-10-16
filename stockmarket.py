import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Input for the stock symbol
stock_symbol = input("Enter a Stock Symbol: ")

# Input for the time period
#time_period = input("Enter a time period: ")

# Get today's date
today = date.today()

# Convert today's date to a string
d1 = today.strftime("%Y-%m-%d")
end_date = d1

# Calculate the start date as one year ago from today
d2 = date.today() - timedelta(days=365)
d2 = d2.strftime("%Y-%m-%d")
start_date = d2

# Download stock data using yfinance
data = yf.download(stock_symbol, start=start_date, end=end_date, progress=False)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low",
             "Close", "Adj Close", "Volume"]].round(2)
data.reset_index(drop=True, inplace=True)
print(data.tail())

# Create a candlestick chart
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"],
                        high=data["High"], low=data["Low"], close=data["Close"])])
figure.update_layout(title="Stock Price Analysis for " + stock_symbol, xaxis_rangeslider_visible=False)
figure.show()

# Create a bar chart for the closing prices
figure1 = px.bar(data, x = "Date", y= "Close")
figure1.show()

# Create a line chart for closing prices with a rangeslider
figure2 = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Rangeslider')
figure2.update_xaxes(rangeslider_visible=True)
figure2.show()

# Create a line chart for closing prices with time period selectors
figure3 = px.line(data, x='Date', y='Close', title='Stock Market Analysis with Time Period Selectors')

figure3.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
figure3.show()
