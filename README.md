# Volatile_Stock_Watcher

The code uses the requests package in Python to access the https://finnhub.io free stock price API and query stock prices for specific tech stocks. The program defines several functions that perform different tasks such as:

```get_stock_price(stock_symbol):```
Returns the latest price for a given stock symbol.


```get_latest_price(lst_of_stocks):```

Gets the latest price for a list of stocks and returns a dictionary of the stock symbol and its corresponding price.

```make_req_for_volatile_stock(stock_symbol):```

Returns the percentage change of a given stock symbol from yesterday and stores it in a dictionary called volatile_stock_dict.

```get_most_volatile_stock(stock_symbol_list):```

Finds the most volatile stock between Apple, Amazon, Netflix, Facebook, and Google based on the percentage change from yesterday and returns the corresponding percentage change. The function also stores the stock symbol, percentage change, current price, and yesterday's price in a list called most_volatile_stock.

```save_to_file():```

Saves the most_volatile_stock list to a CSV file called most_volatile_stock.csv.
The code at the end of the file runs the get_latest_price, get_most_volatile_stock, and save_to_file functions and prints the latest stock prices and the percentage change of the most volatile stock.
