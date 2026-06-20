# Dev Log

## Session 1 (16/06-26)

### Goal

Understand the simplest market-making accounting example.

### What I did
LAB 1-2 completed
I wrote a simple code that buys and sells an item for a small profit. Information about cash and inventory is recorded.

### Problems

None sofar

## Session 2 (17/06-26)

### Goal
LAB 3-4 completed
Implementing functions, understanding the testing environment and how to use the tests

### What I did
Wrote functions that represented buying/selling assets and computing PnL. `assert` checks whether a result is what I expect. If the result is wrong, the test fails.
I also learned that pytest only finds test functions if their names start with `test_`.


### Problems 

Was quite long ago that i wrote function so had to look up basic syntax. File structure was wrong when trying to understand what the test environment was used for. When executing pytest it checks for files with functions that start with "test" and sees if the code runs as expected. My file names didnt have test in the beginning. 

## Session 3 (17/06-26)

### Goal
LAB 4-6 completed
Add bid/ask quotes. Strategy for what to buy and sell at. Introduce spread = ask - bid.

### What I did
Wrote a simple strategy that calculates bid and ask prices from a mid price and a fixed spread. Then I connected this strategy to the accounting functions by buying at the bid and selling at the ask.

In this simple example, the final PnL equals the spread because inventory ends at zero and the market maker buys at 99 and sells at 101.

### Problems
Went smooth no real issues.

## Session 4 (17/06-26)
LAB 7 completed "Done with the first part"
### Goal

Create a list of fixed prices and try to understand why its better to have fixed than random prices

### What I did

Created a list of different midprices and used same same tool `assert` as before to check that the list is correct. Jumping through the list is like jumping through time. Fixed prices are better than random prices at this stage because they make the simulation predictable. This allows me to manually verify the PnL and accounting logic. If I used random prices too early, it would be harder to know whether unexpected results came from a bug or from randomness.

### Problems

Problems were mainly understanding where to stop. I wanted to create a forloop that looped over each midprice and then computed a pnl for each midprice/time .

## Session 5 (18/06-26)

### Goal
Lab 8 Completed
Build the smallest possible function that connects price, quotes, fills,
accounting, and PnL. No randomness yet.

### What I did

Created a small function that had two boolean variable bid_filled and ask_filled. If True market maker buys/sells at bid/ask prices.

### Problems

Understanding general structure of where to write the functions. General structure of the run_one_step function. 

## Session 6 (18/06-26)

### Goal
Lab 9-10 Completed

Turn one step into a loop over a fixed price path while keeping every fill 
predetermined and testable. Store what happens at each step so that later metrics and plots are based on data, not guesses.

### What I did

Created a fixed price list and added a list for when to bid/ask of boolean values. Subsequent orders were logged in a dictionary after each iteration of the loop. Enumerate was used save indexes for later logical statements.

### Problems

Understanding how enumerate works and using the index that the loop is currently on for later use was a big help but hard to understand. Was a long time ago that i used dictionaries so that was a challenge to grip in the beginning but now i understand that dict = {"key" = [values]   }.


## Session 7 (19/06-26)

### Goal
Lab 11 completed
Measure not only whether the final PnL is positive, but how painful the path was on the way there

### What I did

Built functions to test drawdown and maximum drawdown. Drawdown in this instance is how much is our current pnl value differs from the maximum pnl value. Maximum drawdown is just the absolute maximum drawdown value.

### Problems
Main problem was understanding what drawdown value is and the purpose of it. 

## Session 8 (20/06-26)
Lab 12

### Goal
Replace manually specified fills with random but reproducible fill events. 

### What I did
Create a quote distance from a negative exponential function. The value from this function is compared to a random generated number between 0 and 1. If this number is larger then the quote will be filled

### Problems
Understanding the difference between is_filled and fill_probability.

