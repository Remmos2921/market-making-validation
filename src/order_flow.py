import numpy as np

def fill_probability(mid_price, quote_price,k):
    delta = abs(quote_price - mid_price)
    fill_prob = np.exp(-k * delta)
    return fill_prob

def is_filled(mid_price, quote_price, k, rng: np.random.Generator):
    rnd_num = rng.random()
    probability = fill_probability(mid_price, quote_price, k)
    filled = rnd_num < probability
    return filled