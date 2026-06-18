from src.strategy import market_quotes
from src.backtester import apply_buy, apply_sell, mark_to_market_pnl


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

def run_fixed_fill_simulation(prices, spread, bid_fills, ask_fills):
    if len(prices) != len(bid_fills) or len(prices) != len(ask_fills):
        raise ValueError (
            "prices and bid/ask fills must be of same length"
        )

    cash = 0
    inventory = 0
    history = {
        "mid_price": [],
        "cash": [],
        "inventory": [],
        "pnl": [],
    }
    for i, mid_price in enumerate(prices):
        bid, ask = market_quotes(mid_price, spread)
        
        if bid_fills[i]:
            cash, inventory = apply_buy(cash, inventory, bid)
        
        if ask_fills[i]:
            cash, inventory = apply_sell(cash, inventory, ask)
        
        pnl = mark_to_market_pnl(cash, inventory, mid_price)
        history["mid_price"].append(mid_price)
        history["cash"].append(cash)
        history["inventory"].append(inventory)
        history["pnl"].append(pnl)
    return history