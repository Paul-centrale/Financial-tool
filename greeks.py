import yfinance as yf
import pandas as pd

# Get the S&P 500 stock data
sp500 = yf.Ticker("^GSPC")

# Get historical market data
hist = sp500.history(period="max")

# Save the historical data to a pandas DataFrame
df = pd.DataFrame(hist)

# Print the historical data
print(hist)
