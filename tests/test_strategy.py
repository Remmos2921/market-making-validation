from src.strategy import inv_aware_quoting

def test_pos_max_inv():
    bid, ask = inv_aware_quoting(100,2, 0.1, 10,10)
    assert bid == None
    assert ask != None

def test_neg_max_inv():
    bid, ask = inv_aware_quoting(100,2, 0.1, -10, 10)
    assert bid != None
    assert ask == None

def test_inside_limit():
    bid, ask = inv_aware_quoting(100,2, 0.1, 5, 10)
    assert bid != None
    assert ask != None