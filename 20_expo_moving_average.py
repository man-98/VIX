import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download VIX data from Yahoo Finance
vix_data = yf.download("^VIX", period="1d", interval="1m")

# Calculate the 20-period rolling average of VIX closing prices
vix_data['rolling_avg'] = vix_data['Close'].rolling(window=20).mean()

# Calculate the exponential moving average of VIX closing prices with a span of 10
vix_data['ema'] = vix_data['Close'].ewm(span=10, adjust=False).mean()

# Print the last 5 rows of the data
print(vix_data.tail())

# Plot the VIX closing prices, 20-period rolling average and exponential moving average
plt.figure(figsize=(12,6))
plt.plot(vix_data['Close'], label='VIX')
plt.plot(vix_data['rolling_avg'], label='20-period rolling avg')
plt.plot(vix_data['ema'], label='Exponential moving average')
plt.legend()
plt.title('VIX and its features')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
