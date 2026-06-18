from src.simulator import get_fixed_price_path

def test_fixed_prices():
    prices = get_fixed_price_path()

    assert prices == [100, 101, 100, 99, 100]