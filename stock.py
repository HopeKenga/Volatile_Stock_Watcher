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
