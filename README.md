## Quick project summary

A market maker continuously posts bid and ask quotes around a mid-price. 
If the bid is filled, the market maker buys and inventory increases. 
If the ask is filled, the market maker sells and inventory decreases.

This project simulates that process and tracks:

* cash
* inventory
* mark-to-market PnL
* drawdown
* maximum inventory exposure
* strategy behavior under stress scenarios

## How to run the code

If the user wants a stress-test matrix run:
python -m experiments.stress_test_matrix

If the user wants to se a plot of a simulation given a Naive or inventory aware strategy. 
Locate the baseline_experimets file and change the paramaters to your liking and then run:
python -m experiments.baseline_experiment


## Short explanation of the strategy
The project compares two strategies:

* Naive market maker
Posts symmetric bid and ask quotes around the mid-price.
* nventory-aware market maker
Adjusts quotes based on current inventory in order to reduce excessive long or short exposure.

## Assumptions and Limitations

This project uses a simplified market-making model. Prices are simulated rather than based on real market data, 
and fills are generated from a simple probability model.

The simulator does not include a real order book, queue position, latency, transaction fees, or slippage. 
Trades also use fixed size, and the strategy does not forecast future price movements.

The results should therefore be interpreted as a learning and validation exercise, 
not as evidence of a profitable trading strategy.


Link/reference to report