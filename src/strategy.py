def market_quotes(mid_price, spread):
    bid = mid_price - spread / 2
    ask = mid_price + spread / 2
    return bid, ask