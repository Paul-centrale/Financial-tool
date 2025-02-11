import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



# Get the S&P 500 stock data
sp500 = yf.Ticker("^GSPC")

# Get historical market data
hist = sp500.history(period="max", interval="1d")

# Save the historical data to a pandas DataFrame
df = pd.DataFrame(hist)

# Compute the delta of the stock price
df['Delta'] = df['Close'].diff()

# Select a random date
random_date = df.sample().index[0]
spot_price = df.loc[random_date, 'Close']

# Parameters for ATM call option
K = spot_price  # Strike price
T = 30 / 365  # Time to maturity in years (30 days)
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

# Black-Scholes formula for call option price
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    delta = norm.cdf(d1)
    return call_price, delta

# Calculate call price and delta
call_price, delta = black_scholes_call(spot_price, K, T, r, sigma)

# Calculate call prices and deltas for the 2-month scale
start_date = random_date - pd.Timedelta(days=30)
end_date = random_date + pd.Timedelta(days=30)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')
call_prices = []
deltas = []

for date in date_range:
    spot_price = df.loc[date, 'Close'] if date in df.index else np.nan
    if not np.isnan(spot_price):
        call_price, delta = black_scholes_call(spot_price, K, T, r, sigma)
        call_prices.append(call_price)
        deltas.append(delta)
    else:
        call_prices.append(np.nan)
        deltas.append(np.nan)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(date_range, call_prices, label='Call Option Price')
plt.plot(date_range, deltas, label='Delta', color='g')
plt.axvline(x=random_date, color='r', linestyle='--', label='Random Date')
plt.xlabel('Date')
plt.ylabel('Call Price / Delta')
plt.title('ATM Call Option Price and Delta over 2 Months')
plt.legend()
plt.grid(True)
plt.savefig('call_option_price_and_delta.pdf')  # Save the plot as a PDF
plt.show()

# Print the historical data with delta
print(df)

