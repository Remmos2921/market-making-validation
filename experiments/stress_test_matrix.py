from src.simulator import *
from src.strategy import *
from src.price_simulator import *
from src.metrics import *

import pandas as pd
import numpy as np

START_PRICE = 100
N_STEPS = 100
SPREAD = 2
K = 1
SEEDS = range(20)
ALPHA = 0.01

def make_sideways(seed):
    return generate_sideways_path(
        start_price=START_PRICE,
        n_steps=N_STEPS,
        drift=0.0,
        volatility=0.5,
        seed=seed,
    )


def make_uptrend(seed):
    return generate_trend_path(
        start_price=START_PRICE,
        n_steps=N_STEPS,
        drift=0.05,
        volatility=0.5,
        seed=seed,
    )


def make_volatility_shock(seed):
    return generate_volatility_shock_path(
        start_price=START_PRICE, 
        n_steps=N_STEPS, 
        base_volatility=0.5,
        shock_volatility=2,
        shock_start=50,
        shock_end=70, 
        drift=0,
        seed=seed 
    )

def make_downward_jump(seed):
    return  generate_trend_path(
        start_price=START_PRICE,
        n_steps=N_STEPS,
        drift=-0.05,
        volatility=1.5,
        seed=seed
    )

SCENARIOS = {
    "sideways": make_sideways,
    "uptrend": make_uptrend,
    "volatility shock": make_volatility_shock,
    "downward jump": make_downward_jump,
}

STRATEGIES = {
    "Naive": {
        "inventory_aware": False,
        "alpha": 0.0,
    },
    "Inventory-aware": {
        "inventory_aware": True,
        "alpha": ALPHA,
    },
}

def summarize_history(history):

    final_pnl = history["pnl"][-1]
    max_dd = abs(max_drawdown(history["pnl"]))
    max_abs_inv = max(abs(inv) for inv in history["inventory"])

    return final_pnl, max_dd, max_abs_inv

def run_experiments():

    row = []

    for scenario, scenario_type in SCENARIOS.items():
        for seed in SEEDS:
            prices = scenario_type(seed)

            for strategy, strategy_type in STRATEGIES.items():
                history = run_random_fill_simulation(
                    prices=prices,
                    spread=SPREAD,
                    k=K,
                    seed=seed,
                    inventory_aware=strategy_type["inventory_aware"],
                    alpha=strategy_type["alpha"]
                )

                final_pnl, max_dd, max_abs_inventory = summarize_history(history)

                row.append({
                    "scenario": scenario,
                    "strategy": strategy,
                    "seed": seed,
                    "final_pnl": final_pnl,
                    "max_dd": max_dd,
                    "max_abs_inventory": max_abs_inventory,
                })

    results = pd.DataFrame(row)
    
    return results

def build_summary_matrix(results):
    matrix = (
        results
        .groupby(["scenario", "strategy"])
        .agg(
            final_pnl_mean=("final_pnl", "mean"),
            final_pnl_min=("final_pnl", "min"),
            final_pnl_max=("final_pnl", "max"),
            max_dd_mean=("max_dd", "mean"),
            max_abs_inv_mean=("max_abs_inventory", "mean"),
            max_abs_inv_max=("max_abs_inventory", "max"),
        )
        .reset_index()
    )

    matrix["Observation"] = ""

    return matrix

def main():
    raw_results = run_experiments()
    matrix = build_summary_matrix(raw_results)

    print("\nRaw results:")
    print(raw_results.head())

    print("\nStress-test matrix:")
    print(matrix)


if __name__ == "__main__":
    main()