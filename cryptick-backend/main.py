# Raw Package
import numpy as np
import pandas as pd
import yfinance as yf

# class - functions
from userinput import UserInput
from datasource import DataSource

# opening_price, closing_price = DataSource().tickerValues(data)


# Calculate percentage difference
def percentage(opening_price, closing_price):
    return ((closing_price/opening_price) - 1)*100


def percentageDecimals(opening_price, closing_price):
    return ((closing_price/opening_price))


def printValues(opening_price, closing_price):
    # Opening price
    print(f'Open:{opening_price : .2f}')

    # Closing price
    print(f'Close:{closing_price : .2f}')

    # Percentage
    print(f'Percentage: {percentage(opening_price, closing_price) : .2f} %')


printValues(opening_price, closing_price)
