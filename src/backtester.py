## Part 3
def apply_buy(cash, inventory, price):
    cash = cash - price
    inventory = inventory + 1
    return cash, inventory


def apply_sell(cash, inventory, price):
    cash = cash + price
    inventory = inventory - 1
    return cash, inventory


def mark_to_market_pnl(cash, inventory, mid_price):
    return cash + inventory * mid_price
