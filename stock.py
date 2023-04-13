
"""
Use htpps:finnhub.io free stock price API to query stock price 
for specific tech stocks. Use the `requests` package in Python.
"""
import requests
import csv

csv_header =[]
volatile_stock_dict = dict()
most_volatile_stock = []#declared as an array to get the max value of it

def get_stock_price(stock_symbol):#destructuring. Asssigning return values to the declared method
    data,response = make_request(stock_symbol)
    return data['c'] if response.status_code == 200 else 'Access Denied!'

"""
Get the latest price for Apple, Netflix, Facebook, Google.
"""
def get_latest_price(lst_of_stocks):
    stock_prices = {}
    # for every item in the list, look up it's price
    for stock in lst_of_stocks:
        # Append the item name and it's stock price to the dictionary
        stock_prices[stock] = get_stock_price(stock)
    # return the dictionary
    return stock_prices
"""
Between Apple, Amazon, Netflix, Facebook, Google: find the 
stock that has moved the most percentage points from yesterday.
Call this stock the "most_volatile_stock".
"""
def make_req_for_volatile_stock(stock_symbol):
    csv_data = []
    data,response = make_request(stock_symbol)
    csv_data.extend([stock_symbol, data['dp'], data['c'], data['pc']])#similar to a push() method. 
    volatile_stock_key = '{}'.format(stock_symbol)
    volatile_stock_dict.update({volatile_stock_key:csv_data})#{'AAPL':[['AAPL', 13.2, 120.5, 150]],'AMZN':[['AMZN', 13.2, 120.5, 150]]}
    return data['dp'] if response.status_code == 200 else 0

def get_most_volatile_stock(stock_symbol_list):
    stock_price_list = {}
    for stock_symbol in stock_symbol_list:
        stock_price = make_req_for_volatile_stock(stock_symbol)
        if stock_price is not None:
            stock_price_list[stock_symbol] = stock_price
    most_volatile_stock.extend(volatile_stock_dict[max(stock_price_list, key=stock_price_list.get)])
    return stock_price_list[max(stock_price_list, key=stock_price_list.get)]



"""
Save the following information to a file called `most_volatile_stock` to a CSV file.
With the following row format: stock_symbol, percentage_change, current_price, yesterday_price
"""
header = ['stock_symbol','percentage_change','current_price','last_close_price']
def save_to_file():
    with open("most_volatile_stock.csv", "w", newline='') as f:
        writer = csv.writer(f)#returns file object
        writer.writerow(header)
        writer.writerow(most_volatile_stock)
        
"""
Generic function for making requests to the Stock API
"""
def make_request(stock_symbol):
    url = 'https://finnhub.io/api/v1/quote'
    symbol = '{}'.format(stock_symbol)
    token = 'cgs2f9pr01qkrsgj1080cgs2f9pr01qkrsgj108g'#get token from the finnhub stock quote
    response = requests.get(url, params={'symbol':symbol, 'token':token})
    data = response.json()#key value pairs.
    return (data, response)#tuple

if __name__ == "__main__":
    stock_symbol_list = ["AAPL", "AMZN", "NFLX", "FB", "GOOG"]
    print(get_latest_price(stock_symbol_list))
    print(get_most_volatile_stock(stock_symbol_list))
    save_to_file()

