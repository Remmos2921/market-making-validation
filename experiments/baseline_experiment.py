import numpy as np
import matplotlib.pyplot as plt

from src.price_simulator import *
from src.simulator import run_fixed_fill_simulation
from src.metrics import max_drawdown
from src.strategy import market_quotes
from src.order_flow import is_filled


def generate_random_fill(prices, k, spread, seed = None):
    rng = np.random.default_rng(seed)

    ask_fills = []
    bid_fills = []

    for mid_price in prices:
        bid, ask = market_quotes(mid_price, spread)

        bid_filled = is_filled(mid_price, bid, k ,rng)
        ask_filled = is_filled(mid_price, ask, k ,rng)

        bid_fills.append(bid_filled)
        ask_fills.append(ask_filled)

    return bid_fills, ask_fills


def main():
    start_price = 100
    n_steps = 100
    k = 1
    spread = 2
    seed = 42

    prices = generate_sideways_path(start_price=start_price,n_steps=n_steps,
                                    drift=0, volatility=1, seed=seed)
    

    bid_fills, ask_fills = generate_random_fill(prices=prices,
                                            spread=spread, 
                                            k=k,seed=seed)
    
    history = run_fixed_fill_simulation(prices=prices,spread=spread,
    bid_fills=bid_fills,ask_fills=ask_fills)
    final_pnl = history["pnl"][-1]
    max_dd = max_drawdown(history["pnl"])
    max_abs_inv = max(abs(inv) for inv in history["inventory"])
    fill_count = sum(bid_fills) + sum(ask_fills)

    print()
    print("Results:")
    print("Final PnL:", final_pnl)
    print("Max drawdown:", max_dd)
    print("Max absolute inventory:", max_abs_inv)
    print("Fill count:", fill_count)

    plt.plot(history["mid_price"], label="Mid price")
    plt.plot(history["inventory"], label="Inventory")
    plt.plot(history["pnl"], label="PnL")
    plt.xlabel("Step")
    plt.ylabel("Value")
    plt.title("Naive market maker baseline")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()