from flask import Flask

# Import functions from DataSource class
from datasource import DataSource


app = Flask(__name__)


@app.route("/")
def landing_page():
    return "Hello, this is cryptick"


# GET all tickers
@app.route("/ticker-list")
def getTickerList():
    return DataSource().fetchTickers()


# User sends a POST request with given values:
# (ticker: str, period: int, interval: int)
# After successful post request, return a GET request
@app.route("/ticker")
def getTicker():
    return DataSource().ticker()
