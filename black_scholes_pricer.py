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

# Function to price a butterfly spread using call options
def butterfly_spread_call(S, K1, K2, K3, T, r, sigma):
    call_price1 = black_scholes_call(S, K1, T, r, sigma)
    call_price2 = black_scholes_call(S, K2, T, r, sigma)
    call_price3 = black_scholes_call(S, K3, T, r, sigma)
    return [call_price1,call_price2,call_price3]



# Example parameters
S = np.linspace(50, 150, 100)  # Spot price
K = 100  # Strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility


# Calculations:

# Calculate call prices
call_prices = black_scholes_call(S, K, T, r, sigma)

# Calculate put prices
put_prices = black_scholes_put(S, K, T, r, sigma)

# Calculate payoff of a call option
payoff_call = np.maximum(S - K, 0)

# calculate payoff of a put option
payoff_put = np.maximum(K - S, 0)

# Calculate the profit pattern for the call option
call_profit = payoff_call - call_prices

# Calculate the profit pattern for the put option
put_profit = payoff_put - put_prices


# Plots:

# Plotting call option price, payoff, and profit
plt.figure(figsize=(10, 6))
plt.plot(S, call_prices, label='Call Option Price')
plt.plot(S, payoff_call, 'r--', label='Payoff of a call')
#plt.plot(S, call_profit, 'g--', label='Profit')
plt.xlabel('Spot Price')
plt.ylabel('Price / Profit')
plt.title('Call Option Price and Payoff')
plt.legend()
plt.grid(True)
plt.show()

# Plotting put option price, payoff, and profit
plt.figure(figsize=(10, 6))
plt.plot(S, put_prices, label='Put Option Price')
plt.plot(S, payoff_put, 'r--', label='Payoff of a put')
#plt.plot(S, put_profit, 'g--', label='Profit')
plt.xlabel('Spot Price')
plt.ylabel('Price / Profit')
plt.title('Put Option Price and Payoff')
plt.legend()
plt.grid(True)
plt.show()




#Pricing a butterfly spread

# Example parameters
S = np.linspace(50, 150, 100)  # Spot price
K1 = 90  # Lower strike price
K2 = 100  # Middle strike price
K3 = 110  # Upper strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate
sigma = 0.2  # Volatility




# Calculate butterfly spread prices
butterfly_calls = butterfly_spread_call(S, K1, K2, K3, T, r, sigma)
butterfly_prices = butterfly_calls[0] - 2 * butterfly_calls[1] + butterfly_calls[2]

# Adjust the spot price to 100 for butterfly spread pricing
S=100

# Calculate butterfly spread prices at S=100
butterfly_calls_at_100 = butterfly_spread_call(S, K1, K2, K3, T, r, sigma)

butterfly_prices_at_100 = np.full(100,butterfly_calls_at_100[0] - 2 * butterfly_calls_at_100[1] + butterfly_calls_at_100[2])

S = np.linspace(50, 150, 100)
# Calculate the profit pattern for the butterfly spread
butterfly_payoff = np.maximum(S - K1, 0) - 2 * np.maximum(S - K2, 0) + np.maximum(S - K3, 0)
butterfly_profit = butterfly_payoff - butterfly_prices_at_100




# Plotting butterfly spread price, payoff, and profit
plt.figure(figsize=(10, 6))
#plt.plot(S, butterfly_prices, label='Butterfly Spread Price')
plt.plot(S, butterfly_payoff, 'r--', label='Payoff')
plt.plot(S, butterfly_profit, 'g--', label='Profit')
plt.xlabel('Spot Price')
plt.ylabel('Price / Profit')
plt.title('Butterfly Spread Price, Payoff, and Profit')
plt.legend()
plt.grid(True)
plt.show()


# Plotting butterfly spread payoff
plt.figure(figsize=(10, 6))
#plt.plot(S, butterfly_prices, label='Butterfly Spread Price')
plt.plot(S, butterfly_payoff, 'r--', label='Payoff')
#plt.plot(S, butterfly_profit, 'g--', label='Profit')
plt.xlabel('Payoff')
plt.ylabel('Price / Profit')
plt.title('Butterfly Spread Payoff')
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


# Straddle spread