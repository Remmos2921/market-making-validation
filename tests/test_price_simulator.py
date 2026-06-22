from src.price_simulator import *

def test_len_path():
    prices = generate_sideways_path(100,100,0,1,42)
    assert len(prices) == 100

def test_same_param_path():
    prices_1 = generate_jump_path(100,100,1,0.1,10,1,42)
    prices_2 = generate_jump_path(100,100,1,0.1,10,1,42)

    assert prices_1 == prices_2

def test_start_price_path():
    prices = generate_volatile_path(100,100,1,1,44)

    assert prices[0] == 100

def test_jump_path():
    """
    Test jump_prob = 0, price does not change.
    """
    prices = generate_jump_path(100,4,0,10,0,0,55)

    assert prices == [100,100,100,100]

def test_jump_path():
    """
    Test jump_prob = 1. Price adds jump_size to each new price 
    """
    prices = generate_jump_path(100,4,1,40,0,0,55)

    assert prices == [100,140,180,220]
    
