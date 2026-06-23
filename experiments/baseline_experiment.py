import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from src.price_simulator import *
from src.simulator import run_random_fill_simulation
from src.metrics import max_drawdown
from src.strategy import market_quotes, inv_aware_quoting
from src.order_flow import is_filled

def main():
    start_price = 100
    n_steps = 100
    k = 1
    spread = 2
    seed = 43

    prices = generate_trend_path(start_price=start_price, n_steps=n_steps, drift= -0.1
                        , volatility = 1.5, seed=None)
    
    
    history = run_random_fill_simulation(prices=prices, spread=spread, k=k,
                                         seed=seed, inventory_aware=True,
                                         alpha=0.01)
    final_pnl = history["pnl"][-1]
    max_dd = max_drawdown(history["pnl"])
    max_abs_inv = max(abs(inv) for inv in history["inventory"])

    print()
    print("Results:")
    print("Final PnL:", final_pnl)
    print("Max drawdown:", max_dd)
    print("Max absolute inventory:", max_abs_inv)

    plt.plot(history["mid_price"], label="Mid price")
    plt.plot(history["inventory"], label="Inventory")
    plt.plot(history["pnl"], label="PnL")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.title("Naive aware market maker baseline")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()