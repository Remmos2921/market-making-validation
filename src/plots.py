import matplotlib.pyplot as plt

from price_simulator import *


prices = generate_volatile_path(
    start_price=100,n_steps=50,
    drift=0,volatility=10,seed=42)

plt.plot(prices)
plt.xlabel("Time step")
plt.ylabel("Price")
plt.title("volatile price path")
plt.show()

