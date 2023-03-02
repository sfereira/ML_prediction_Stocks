import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Get the stock price data for Microsoft and Apple
msft = yf.Ticker("MSFT").history(period="10y")
aapl = yf.Ticker("AAPL").history(period="10y")

# Combine the data into a single DataFrame
df = pd.concat([msft['Close'], aapl['Close']], axis=1)
df.columns = ['Microsoft', 'Apple']


# Calculate the correlation between the Microsoft and Apple stock prices
correlation = df['Microsoft'].corr(df['Apple'])

print("The correlation between Microsoft and Apple stock prices is:", correlation)

# Plot the stock prices to visualize their relationship
plt.plot(df['Microsoft'], label='Microsoft')
plt.plot(df['Apple'], label='Apple')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Stock Price')
plt.title('Microsoft and Apple Stock Prices Over the Last 10 Years')
plt.show()

import plotly.express as px
# Plot the stock prices using Plotly

fig = px.line(df, x=df.index, y=df['Microsoft'], title=f"Correlation: {correlation}")
fig.update_traces(name='Microsoft Stock Price')
fig.add_scatter(x=df.index, y=df['Apple'], name='Apple Stock Price')
fig.update_layout(xaxis_title='Year', yaxis_title='Stock Price')
fig.show()

import plotly.graph_objs as go
fig = go.Figure()
fig.add_scatter(x=df.index, y=df['Microsoft'], name='Microsoft Stock Price')
fig.add_scatter(x=df.index, y=df['Apple'], name='Apple Stock Price')
fig.update_layout(xaxis_title='Year', yaxis_title='Stock Price($)',title=f"Correlation: {correlation}")
fig.show()

from scipy.stats import pearsonr

correlation, p_value = pearsonr(df['Microsoft'], df['Apple'])
print(f'The Pearson correlation coefficient between Microsoft and Apple stocks is {correlation:.2f}')
print(f'The P-value between Microsoft and Apple stocks is {p_value}')

import seaborn as sns

sns.jointplot(x='Microsoft', y='Apple', data=df)

import yfinance as yf
import pandas as pd
import numpy as np

# Get the stock information for Microsoft and Apple from yfinance
microsoft = yf.Ticker("MSFT")
apple = yf.Ticker("AAPL")

# Get the historical stock data for each stock
microsoft_data = microsoft.history(period="10y")
apple_data = apple.history(period="10y")

# Calculate the average trading volume for each stock
microsoft_average_volume = np.mean(microsoft_data['Volume'])
apple_average_volume = np.mean(apple_data['Volume'])

# Calculate the total dividend payment for each stock over the last 10 years
microsoft_dividend_total = sum(microsoft_data['Dividends'])
apple_dividend_total = sum(apple_data['Dividends'])

# Calculate the correlation between the Microsoft and Apple stock prices
correlation = df['Microsoft'].corr(df['Apple'])

# Print the results
print('Microsoft average trading volume: ', microsoft_average_volume)
print('Apple average trading volume: ', apple_average_volume)
print('Microsoft total dividend payment: ', microsoft_dividend_total)
print('Apple total dividend payment: ', apple_dividend_total)
print("The correlation between Microsoft and Apple stock prices is:", correlation)

# stock --> Name of the stock. eg. "AAPL", "MSFT"
# period --> The time period of data to analyze.

def single_stock_features(stock,period):
    stockx = yf.Ticker(stock)
    
    # Get the historical stock data for each stock
    stock_data = stockx.history(period=period)
    
    # Calculate the average trading volume for each stock
    stock_average_volume = np.mean(stock_data['Volume'])
    
    # Calculate the total dividend payment for each stock over the Period selected
    stock_dividend_total = sum(stock_data['Dividends'])
    
    print(f"{stock} average trading volume: {stock_average_volume} ")
    print(f"{stock} total dividend payment: {stock_dividend_total} ")
    return stock_average_volume, stock_dividend_total


# stock1 & stock2 --> Names of the stocks. eg. "AAPL", "MSFT"
def mutual_stock_features(stock1,stock2,period):
    # Get the stock price data for Microsoft and Apple
    stockx = yf.Ticker(stock1).history(period=period)
    stocky = yf.Ticker(stock2).history(period=period)

    # Combine the data into a single DataFrame
    df = pd.concat([stockx['Close'], stocky['Close']], axis=1)
    df.columns = [stock1, stock2]

    
    # Calculate the correlation between the Microsoft and Apple stock prices
    correlation = df[stock1].corr(df[stock2])
    print(f"The correlation between {stock1} and {stock2} stock prices is: {correlation}")
    return correlation
    
# Example --> 1
stock1 = 'MSFT'
stock2 = 'AAPL'
period = '10y'
mutual_stock_features(stock1,stock2,period)

# Example --> 2
stock = 'AAPL'
period = '10y'
single_stock_features(stock,period)

import yfinance as yf
import numpy as np

def stock_performance(ticker):
    stock = yf.Ticker(ticker)
    stock_data = stock.history(period="10y")
    
    # Calculate the stock return for each day
    stock_data['return'] = stock_data['Close'].pct_change()
    
    # Calculate the average daily return
    average_daily_return = np.mean(stock_data['return'])
    
    # Calculate the annual return
    annual_return = average_daily_return * 252 #Number of trading days in a year (252)
    
    return annual_return

# Example usage
microsoft_performance = stock_performance("MSFT")
apple_performance = stock_performance("AAPL")
print("Microsoft performance: ", microsoft_performance)
print("Apple performance: ", apple_performance)
