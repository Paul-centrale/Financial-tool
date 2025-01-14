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

# Black-Scholes formula for put option price
def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

# Example parameters
S = np.linspace(50, 150, 100)  # Spot price
K = 100  # Strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility

# Calculate call prices
call_prices = black_scholes_call(S, K, T, r, sigma)

# Calculate put prices
put_prices = black_scholes_put(S, K, T, r, sigma)

# Calculate payoff of a call option
payoff_put = np.maximum(S - K, 0)
#calculate payoff of a put option
payoff_call = np.maximum(K - S, 0)

# Plotting
plt.figure(figsize=(10, 6))
#plt.plot(S, call_prices, label='Call Option Price')
plt.plot(S, put_prices, label='Put Option Price')
#plt.plot(S, payoff_pull, 'r--', label='Payoff')
plt.plot(S, payoff_call, 'r--', label='Payoff')
plt.xlabel('Spot Price')
plt.ylabel('Price')
plt.title('Put Option Price and Payoff')
plt.legend()
plt.grid(True)
plt.show()