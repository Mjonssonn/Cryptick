
import yfinance as yf
import pandas as pd

# Fetching the data


class DataSource:

    def __init__(self):
        self.ticks = ['BTC-USD']

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
        return coin

    def tickerValues(self, df):
        opening_price = list(df.Open)
        closing_price = list(df.Close)
        return opening_price[0], closing_price[-1]

    # def fetchTickers(self, ticker):
    #     '''fetch tickers'''
    #     return yf.ticker['AMZN']


'''
                    Open          High           Low         Close     Adj Close        Volume
Date
2022-11-06  21285.056641  21345.376953  20920.191406  20926.486328  20926.486328   35082693210
2022-11-07  20924.621094  21053.246094  20489.972656  20602.816406  20602.816406   53510852236
2022-11-08  20600.671875  20664.607422  17603.544922  18541.271484  18541.271484  118992465607
2022-11-09  18509.156250  18590.458984  16997.904297  17027.648438  17027.648438  122418585600
'''

# 2022-11-06 ------------ 2022-11-09
# date (open) jämfört med date (close)

# Fyra dagars intervall:
# df[0, 'Open'] jämför med df[3, 'Close']

# En dags intervall:
# df[0, 'Open'] jämför med df[1, 'Close']

# En veckas intervall:
# df[0, 'Open'] jämför med df[6, 'Close']
print(yf.download('BTC-USD', '1wk', '1d'))
