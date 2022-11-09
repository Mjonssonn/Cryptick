
import yfinance as yf
import pandas as pd
from yahooquery import Screener


class DataSource:

    def __init__(self):
        self.ticks = self.fetchTickers()

        self.periods = ['1m', '2m', '5m', '15m', '30m', '60m',
                        '90m', '1h', '1d', '5d', '1mo',
                        '3mo', '6mo', '1y', 'ytd', 'max']

        self.intervals = ['1m', '2m', '5m', '15m', '30m', '60m',
                          '90m', '1h', '1d', '5d', '1mo']

    def ticker(self, ticker, period, interval):
        coin = yf.download(
            tickers=self.ticks[ticker],
            period=self.periods[period],
            interval=self.intervals[interval])
        print(self.ticks[ticker],self.periods[period],self.intervals[interval])
        return coin

    def tickerValues(self, df):
        opening_price = list(df.Open)
        closing_price = list(df.Close)
        return opening_price[0], closing_price[-1]

    def fetchTickers(self):
        s = Screener()
        data = s.get_screeners('all_cryptocurrencies_us', count=250)
        dicts = data['all_cryptocurrencies_us']['quotes']
        symbols = [d['symbol'] for d in dicts]
        
        return symbols



