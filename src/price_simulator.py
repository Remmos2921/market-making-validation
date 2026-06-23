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

def generate_volatility_shock_path(start_price, n_steps,
                                   base_volatility, shock_volatility,
                                   shock_start,shock_end,
                                   drift=0.0, seed=None):
    
    rng = np.random.default_rng(seed)
    prices = [float(start_price)]

    for step in range(n_steps - 1):
        price_now = prices[-1]

        if shock_start <= step < shock_end:
            volatility = shock_volatility
        else:
            volatility = base_volatility

        price_change = drift + volatility * rng.normal()
        next_price = price_now + price_change

        prices.append(next_price)

    return prices