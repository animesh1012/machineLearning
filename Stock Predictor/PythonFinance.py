# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import pandas_datareader.data as web

class Finance():
    def __init__(self):
        style.use('ggplot')
        # Historic Data Since 1 Jan 2015. Change According to your choice in the form of yy,mm,dd
        self.start=dt.datetime(2015,1,1)
        self.end=dt.datetime.now()
    
    def get_stock_price(self,ticker):
        self.df = web.DataReader(ticker,"yahoo",self.start,self.end)
        self.df.reset_index(inplace=True)
        return(self.df)
    
    def get_moving_avg(self,ticker):
        self.df = self.get_stock_price(ticker)
        self.df['1 ma'] = self.df['Adj Close'].rolling(window=5,min_periods=0).mean()
        ax1=plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
        
        ax1.plot(self.df['Date'],self.df['Adj Close'],label='Stock Price',color='yellow')
        ax1.plot(self.df['Date'],self.df['1 ma'],label='Daily Moving Average',color='cyan')
        
        ax1.legend()
        
        C = self.df['Adj Close'].tolist()
        D = self.df['1 ma'].tolist()
        E = self.df['Date'].tolist()
        for i in range(len(C)):
            if (C[i]>D[i]):
                action='BUY/HOLD'
            elif (C[i]<D[i]):
                action='SELL'
        plt.title("Ticker Symbol : {}\nAction : {}".format(ticker,action))
        plt.show()
        
       
    #ticker=input('Enter Ticker Symbol ')
    #get_moving_avg(ticker)
#finance = Finance()
#finance.get_moving_avg("KO")    
    # Enter Ticker Symbol
    # This Program will show a Graph in which :
    # Stock Price is denoted by Yellow color..
    # 20 Day Moving Average price by Cyan..
    # Blue color Bar will Denote on that day, how many share were Traded..
    # Green Points denote Buy..
    # Red Point denote Sell on that Day..
