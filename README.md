# Stock Analysis using yfinance library

This Python code analyzes the performance of a single stock or multiple stocks using the yfinance library.

## Dependencies : 
This code requires the following Python libraries to be installed:

* yfinance <br>
* pandas <br>
* numpy <br>

You can install them using pip:

> pip install yfinance pandas numpy

## Functions

This code defines three functions to analyze stocks:

### Stock Performance
* This function takes a stock ticker as input and returns the annual return of the stock over the last 10 years. <br>
* It uses the yf.Ticker() method to get the historical stock data and calculates the daily returns and the average daily return using numpy.

### Single Stock Features
* This function takes a stock ticker and a period as input and returns the average trading volume and total dividend payment of the stock over the given period. <br>
* It uses the yf.Ticker() method to get the historical stock data and calculates the average trading volume and total dividend payment using numpy.

### Mutual Stock Features
* This function takes two stock tickers and a period as input and returns the correlation between the stock prices of the two stocks over the given period. <br>
It uses the yf.Ticker() method to get the historical stock data and calculates the correlation using pandas.


## Credits
* This code is written by Mr. Fereira and is based on the yfinance library.
