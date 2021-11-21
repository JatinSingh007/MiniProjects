import pandas_datareader.data as web
import pandas as pd
from datetime import datetime 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
startdate = '2010-01-01'
today = datetime.today().strftime('%Y-%m-%d')

def getMyPortfolio(stocks = stock_symbols, start = startdate, end = today, col = 'Adj Close'):
    data = web.DataReader(stocks, data_source = 'yahoo' ,start = start, end = end)[col]
    return data
price = web.DataReader('MS', data_source = 'yahoo', start = startdate, end = today)['Adj Close']

daily_return = price.pct_change()
daily_vol = daily_return.std()

last_price = price[-1]

num_simu = 5
num_days = 252

simulation_df = pd.DataFrame()
for x in range(num_simu):
    count = 0
    daily_vol = daily_return.std()
    
    price_series = []
    
    prices = last_price*(1 + np.random.normal(0, daily_vol))
    price_series.append(prices)
    
    for y in range(num_days):
        if count == 251:
            break
        prices = price_series[count]*(1+np.random.normal(0, daily_vol))
        price_series.append(prices)
        count += 1
    
    simulation_df[x] = price_series


simulation_df.head()
fig = plt.figure()
fig.suptitle('Monte Carlo Simulation: Morgan Stanley')
plt.plot(simulation_df, lw = 1)
plt.axhline(y = last_price, color = 'r', linestyle = '-')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()
