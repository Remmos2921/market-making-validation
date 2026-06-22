import numpy as np
from src.strategy import market_quotes, inv_aware_quoting
from src.backtester import apply_buy, apply_sell, mark_to_market_pnl
from src.order_flow import is_filled


def run_one_step(mid_price, spread, bid_filled, ask_filled):
    cash = 0
    inventory = 0
    
    bid, ask = market_quotes(mid_price, spread)

    if bid_filled:
        cash, inventory = apply_buy(cash, inventory, bid)
    
    if ask_filled:
        cash, inventory = apply_sell(cash, inventory, ask)

    pnl = mark_to_market_pnl(cash, inventory, mid_price)
    
    return cash, inventory, pnl

def run_random_fill_simulation(prices,spread,k,seed=None,inventory_aware=False,alpha=0.0):
    cash = 0
    inventory = 0
    max_inventory = 3
    rng = np.random.default_rng(seed)

    history = {
        "mid_price": [],
        "bid": [],
        "ask": [],
        "bid_fill": [],
        "ask_fill": [],
        "cash": [],
        "inventory": [],
        "pnl": [],
    }
    for mid_price in prices:

        if inventory_aware:
            bid, ask = inv_aware_quoting(mid_price=mid_price,
                                         spread=spread, alpha=alpha, 
                                         inventory=inventory,max_inventory=max_inventory)
        else:
            bid, ask = market_quotes(mid_price=mid_price, spread=spread)
        
        if bid is not None:
            bid_filled = is_filled(mid_price, bid, k, rng)
        else:
            bid_filled = False

        if ask is not None:
            ask_filled = is_filled(mid_price, ask, k, rng)
        else:
            ask_filled = False

        if bid_filled:
            cash, inventory = apply_buy(cash, inventory, bid)
        
        if ask_filled:
            cash, inventory = apply_sell(cash, inventory, ask)
        
        pnl = mark_to_market_pnl(cash, inventory,mid_price)

        history["mid_price"].append(mid_price)
        history["bid"].append(bid)
        history["ask"].append(ask)
        history["bid_fill"].append(bid_filled)
        history["ask_fill"].append(ask_filled)
        history["cash"].append(cash)
        history["inventory"].append(inventory)
        history["pnl"].append(pnl)

    return history