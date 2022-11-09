# Raw Package
import numpy as np
import pandas as pd
import yfinance as yf


# class - functions
from userinput import UserInput
from datasource import DataSource

# Fetching user input, passing the number to the ticker function
print("Enter a number: ")
number = int(input())

# Printing the ticker with the index given by user
data = DataSource().ticker(number, 6, 3)

opening_price, closing_price = DataSource().tickerValues(data)


# Calculate percentage difference
def percentage(opening_price, closing_price):
    return ((closing_price/opening_price) - 1)*100


def printValues(opening_price, closing_price):
    # Opening price
    print(f'Open:{opening_price : .2f}')

    # Closing price
    print(f'Close:{closing_price : .2f}')

    # Percentage
    print(f'Percentage: {percentage(opening_price, closing_price) : .2f} %')


printValues(opening_price, closing_price)

# Fetching 250 crypto tickers
t = DataSource().fetchTickers()
# print(t)
