import numpy as np

def generate_sideways_path(start_price, n_steps, drift = 0.0
                        , volatility = 1.0, seed=None):
    
    rng = np.random.default_rng(seed)
    prices = [float(start_price)]

    for step in range(n_steps - 1):
        price_now = prices[-1]

        price_mod = volatility * rng.normal()
        next_price = price_now + drift + price_mod

        prices.append(next_price)
    
    return prices

def generate_trend_path(start_price, n_steps, drift
                        , volatility = 1.0, seed=None):
    
    rng = np.random.default_rng(seed)
    prices = [float(start_price)]

    for step in range(n_steps - 1):
        price_now = prices[-1]

        price_mod = volatility * rng.normal()
        next_price = price_now + drift + price_mod

        prices.append(next_price)
    
    return prices

def generate_volatile_path(start_price, n_steps, drift
                        , volatility, seed=None):
    rng = np.random.default_rng(seed)
    prices = [float(start_price)]

    for step in range(n_steps - 1):
        price_now = prices[-1]

        price_mod = volatility * rng.normal()
        next_price = price_now + drift + price_mod

        prices.append(next_price)
    
    return prices
    
def generate_jump_path(start_price, n_steps, jump_prob, 
                       jump_size, volatility = 1.0, drift= 1.0, seed=None):
    
    rng = np.random.default_rng(seed)
    prices = [float(start_price)]

    for step in range(n_steps - 1):
        price_now = prices[-1]

        if rng.random() < jump_prob:
            jump = jump_size
        else:
            jump = 0.0

        price_mod = volatility * rng.normal()
        next_price = price_now + drift + price_mod + jump

        prices.append(next_price)
    
    return prices