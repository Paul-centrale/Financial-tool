import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
time = np.linspace(0, 1, 250)  # Time from 0 to 1 year
underlying_scenarios = {
    "Series 1": 1 + 0.1 * np.sin(2 * np.pi * time),  # Simulated path 1
    "Series 2": 1 + 0.2 * time,                     # Simulated path 2
    "Series 3": 1 - 0.1 * np.sin(2 * np.pi * time)  # Simulated path 3
}

# Black-Scholes formulas for Delta and Gamma
def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def delta(S, K, T, r, sigma):
    return norm.cdf(d1(S, K, T, r, sigma))

def gamma(S, K, T, r, sigma):
    return norm.pdf(d1(S, K, T, r, sigma)) / (S * sigma * np.sqrt(T))

# Strike price, interest rate, and volatility
strike_price = 1.0
volatility = 0.2
risk_free_rate = 0.05
time_to_expiry = 1

# Calculate Delta and Gamma for each series
deltas = {}
gammas = {}
for name, path in underlying_scenarios.items():
    deltas[name] = delta(path, strike_price, time_to_expiry, risk_free_rate, volatility)
    gammas[name] = gamma(path, strike_price, time_to_expiry, risk_free_rate, volatility)

# Plot Figure 5.4: Path of the underlying asset
plt.figure(figsize=(10, 6))
for name, series in underlying_scenarios.items():
    plt.plot(time, series * 100, label=name)  # Convert to percentages
plt.title("Figure 5.4: Scenarios for the Path of the Underlying Asset")
plt.xlabel("Time to Expiry")
plt.ylabel("Underlying Price (%)")
plt.legend()
plt.grid()
plt.show()

# Plot Figure 5.5: Delta
plt.figure(figsize=(10, 6))
for name, delta_values in deltas.items():
    plt.plot(time, delta_values * 100, label=f"Delta {name.split()[-1]}")  # Convert to percentages
plt.title("Figure 5.5: Deltas of an ATM Option Based on Underlying Paths")
plt.xlabel("Time to Expiry")
plt.ylabel("Delta (%)")
plt.legend()
plt.grid()
plt.show()

# Plot Figure 5.7: Gamma
plt.figure(figsize=(10, 6))
for name, gamma_values in gammas.items():
    plt.plot(time, gamma_values, label=f"Gamma {name.split()[-1]}")
plt.title("Figure 5.7: Scenarios for Gamma Based on Underlying Paths")
plt.xlabel("Time to Expiry")
plt.ylabel("Gamma")
plt.legend()
plt.grid()
plt.show()