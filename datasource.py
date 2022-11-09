
import yfinance as yf
import pandas as pd
from yahooquery import Screener


class DataSource:

    def __init__(self):

        # Fetching the ticker name from the fetchTickers() function
        self.ticks = self.fetchTickers()

        # Time intervals
        self.periods = ['1m', '2m', '5m', '15m', '30m', '60m',
                        '90m', '1h', '1d', '5d', '1mo',
                        '3mo', '6mo', '1y', 'ytd', 'max']
        # Time intervals
        self.intervals = ['1m', '2m', '5m', '15m', '30m', '60m',
                          '90m', '1h', '1d', '5d', '1mo']

    # Fetching 250 tickers
    def fetchTickers(self):
        s = Screener()
        data = s.get_screeners('all_cryptocurrencies_us', count=250)
        dicts = data['all_cryptocurrencies_us']['quotes']
        symbols = [d['symbol'] for d in dicts]
        return sorted(symbols)

    # Passing the required arguments for the yf.download() function:
    def ticker(self, ticker, period, interval):
        coin = yf.download(
            tickers=self.ticks[ticker],
            period=self.periods[period],
            interval=self.intervals[interval])
        print(
            self.ticks[ticker],
            self.periods[period],
            self.intervals[interval])
        return coin

    # Fetching the ticker values:
    # Open - Start period
    # Close - Current price
    def tickerValues(self, df):
        opening_price = list(df.Open)
        closing_price = list(df.Close)
        return opening_price[0], closing_price[-1]
