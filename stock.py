"""
Use htpps:finnhub.io free stock price API to query stock price 
for specific tech stocks. Use the `requests` package in Python.
"""

import requests
import csv

csv_header =[]
volatile_stock_dict =dict()
most_volatile_stock = [] #declared as an array to get the max value of it

def get_stock_price(stock_symbol) : #destructuring. Asssigning return values to the declared method
     data, response = make_request(stock_symbol)
     return data['c'] if response.status_code == 200 else 'Access Denied'

"""
Get the lates price for Apple, Netflix, Facebook, Google
"""

def get_latest_price(list_of_stocks):
    stock_prices ={}
    #for every item in the list, look up it's price

    fro stock in list_of_stocks:
    #Append the item name and it's stock price to the dictionary

    stock_prices[stock] = get_stock_price(stock)
    #return the dictionary
    return stock_prices
"""
Between Apple, Amazon, Netflix, Facebook, Google: find the stock
that has moved the most percentage points from yesterday.
"""

def make_req_for_volatile_stock(stock_symbol):
    csv_data = []
    data, response = make_request(stock_symbol)
    csv_data.extend([stock_symbol, data['dp'], data['c'],data['pc']]))#similar to push()
    volatile_stock_key ='{}'.format(stock_symbol)
    volatile_stock_dict.update({volatile_stock_key:csv_data})#{'AAPL':[['AAPL', 13.2, 120.5, 150]],'AMZN':[['AMZN', 13.2, 120.5, 150]]}
    return data('dp') if response.status_code == 200 else 0

"""
Save the following information to a file called `most_volatile_stock` to a CSV file.
With the following row format: stock_symbol, percentage_change, current_price, yesterday_price
"""