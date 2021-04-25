# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

style.use('ggplot')
# Historic Data Since 1 Jan 2015. Change According to your choice in the form of yy,mm,dd
start=dt.datetime(2015,1,1)
end=dt.datetime.now()

def get_stock_price(ticker):
    df = web.DataReader(ticker,"yahoo",start,end)
    df.reset_index(inplace=True)
    return(df)

def get_moving_avg(ticker):
    df = get_stock_price(ticker)
    df['20 ma'] = df['Adj Close'].rolling(window=20,min_periods=0).mean()
    ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
    ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
    ax1.plot(df['Date'],df['Adj Close'],label='Stock Price',color='yellow')
    ax1.plot(df['Date'],df['20 ma'],label='20 Days Moving Average',color='cyan')
    ax2.bar(df['Date'],df['Volume'],label='Volume Traded',color='blue')
    ax1.legend()
    ax2.legend()
    C = df['Adj Close'].tolist()
    D = df['20 ma'].tolist()
    E = df['Date'].tolist()
    for i in range(len(C)):
        if (C[i]>D[i]):
            ax1.scatter(E[i],C[i],label='Buy',color='green')
        elif (C[i]<D[i]):
            ax1.scatter(E[i],C[i],label='Sell',color='red')        
    plt.show()
   
ticker=input('Enter Ticker Symbol ')
get_moving_avg(ticker)

# Enter Ticker Symbol
# This Program will show a Graph in which :
# Stock Price is denoted by Yellow color..
# 20 Day Moving Average price by Cyan..
# Blue color Bar will Denote on that day, how many share were Traded..
# Green Points denote Buy..
# Red Point denote Sell on that Day..
