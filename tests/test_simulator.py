from src.simulator import run_fixed_fill_simulation

def test_fixed_fill_sim():
    prices = [100, 101, 100, 99, 100]
    spread = 2
    bid_fills = [True, False, False, True, False]
    ask_fills = [False, True, False, False, True]

    history = run_fixed_fill_simulation(prices, spread, bid_fills, ask_fills)
    
    assert len(history["mid_price"]) == len(prices)
    assert len(history["cash"]) == len(prices)
    assert len(history["inventory"]) == len(prices)
    assert len(history["pnl"]) == len(prices)