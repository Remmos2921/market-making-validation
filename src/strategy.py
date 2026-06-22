def market_quotes(mid_price, spread):
    bid = mid_price - spread / 2
    ask = mid_price + spread / 2
    return bid, ask

def inv_aware_quoting(mid_price, spread,alpha, 
                      inventory, max_inventory):
    half_spread = spread/2
    reservation_price = mid_price - alpha * inventory

    bid = reservation_price - half_spread
    ask = reservation_price + half_spread

    if inventory >= max_inventory:
        bid = None
    elif inventory <= -max_inventory:
        ask = None

    return bid, ask