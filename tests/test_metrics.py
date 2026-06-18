from src.metrics import drawdown_series, max_drawdown

def test_drawdown():
    pnl_history = [0, 3, 1, 4, -2]

    result = drawdown_series(pnl_history)

    assert result == [0, 0, -2, 0, -6]

def test_max_drawdown():
    pnl_history = [0, 3, 1, 4, -2]
    
    result = max_drawdown(pnl_history)

    assert result == -6