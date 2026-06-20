from src.order_flow import fill_probability, is_filled
import numpy as np

def test_filled():
    assert fill_probability(mid_price=100, quote_price=100, k=1) == 1

def test_probability_between_zero_and_one():
    p = fill_probability(mid_price=100, quote_price=105, k=1)

    assert 0 <= p <= 1

def test_same_seed_filled():
    rng1 = np.random.default_rng(seed=42)
    rng2 = np.random.default_rng(seed=42)

    results1 = is_filled(100, 100.5, 1, rng1)
    results2 = is_filled(100, 100.5, 1, rng2)

    assert results1 == results2