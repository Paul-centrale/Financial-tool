import sys
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# Black-Scholes formula for call option price
def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

# Function to price a butterfly spread using call options
def butterfly_spread_call(S, K1, K2, K3, T, r, sigma):
    call_price1 = black_scholes_call(S, K1, T, r, sigma)
    call_price2 = black_scholes_call(S, K2, T, r, sigma)
    call_price3 = black_scholes_call(S, K3, T, r, sigma)
    butterfly_price = call_price1 - 2 * call_price2 + call_price3
    return butterfly_price

# Example parameters
S = np.linspace(50, 150, 100)  # Spot price
K = 100  # Strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate call prices
call_prices = black_scholes_call(S, K, T, r, sigma)

# Calculate payoff
payoff = np.maximum(S - K, 0)

# Calculate the profit pattern for the call option
call_profit = call_prices - payoff

# Plotting call option price, payoff, and profit
plt.figure(figsize=(10, 6))
plt.plot(S, call_prices, label='Call Option Price')
plt.plot(S, payoff, 'r--', label='Payoff')
plt.plot(S, call_profit, 'g--', label='Profit')
plt.xlabel('Spot Price')
plt.ylabel('Price / Profit')
plt.title('Call Option Price, Payoff, and Profit')
plt.legend()
plt.grid(True)
plt.show()

# Example parameters
S = np.linspace(50, 150, 100)  # Spot price
K1 = 90  # Lower strike price
K2 = 100  # Middle strike price
K3 = 110  # Upper strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate butterfly spread prices
butterfly_prices = butterfly_spread_call(S, K1, K2, K3, T, r, sigma)

# Calculate the profit pattern for the butterfly spread
butterfly_payoff = np.maximum(S - K1, 0) - 2 * np.maximum(S - K2, 0) + np.maximum(S - K3, 0)
butterfly_profit = butterfly_prices - butterfly_payoff

# Plotting butterfly spread price, payoff, and profit
plt.figure(figsize=(10, 6))
plt.plot(S, butterfly_prices, label='Butterfly Spread Price')
plt.plot(S, butterfly_payoff, 'r--', label='Payoff')
plt.plot(S, butterfly_profit, 'g--', label='Profit')
plt.xlabel('Spot Price')
plt.ylabel('Price / Profit')
plt.title('Butterfly Spread Price, Payoff, and Profit')
plt.legend()
plt.grid(True)
plt.show()

# Plotting butterfly spread profit pattern separately
plt.figure(figsize=(10, 6))
plt.plot(S, butterfly_profit, 'g--', label='Butterfly Spread Profit')
plt.xlabel('Spot Price')
plt.ylabel('Profit')
plt.title('Butterfly Spread Profit Pattern')
plt.legend()
plt.grid(True)
plt.show()