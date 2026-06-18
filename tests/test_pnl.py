from src.backtester import apply_buy, apply_sell, mark_to_market_pnl
from src.strategy import market_quotes

def test_market_quote_strategy():
    cash = 0
    inventory = 0

    mid_price = 100
    spread = 2
    bid, ask = market_quotes(mid_price, spread)
    cash, inventory = apply_buy(cash, inventory, bid)
    cash, inventory = apply_sell(cash, inventory, ask)

    pnl = mark_to_market_pnl(cash, inventory, mid_price)

    assert ask == 101
    assert bid == 99
    assert cash == 2
    assert inventory == 0
    assert pnl == 2
