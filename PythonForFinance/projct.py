# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

style.use('ggplot')
start=dt.datetime(2015,1,1)
end=dt.datetime.now()

def get_stock_price(ticker):
    df = web.DataReader(ticker,"yahoo",start,end)
    df.reset_index(inplace=True)
    df.set_index("Date",inplace=True)
    return(df)

get_stock_price('TSLA')

def get_moving_avg():
    df = get_stock_price('KO')
    df['20 ma'] = df['Adj Close'].rolling(window=20,min_periods=0).mean()
    ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
    ax2=plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)
    ax1.plot(df.index,df['Adj Close'])
    ax1.plot(df.index,df['20 ma'])
    ax2.bar(df.index,df['Volume'])
    plt.show()
    
get_moving_avg()