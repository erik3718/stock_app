import yfinance as yf
import numpy as np
import pandas as pd
from scipy.stats import norm


class stocks_app:
    def __init__(self):
        self.answer = None
        self.daily_volatility = None
        self.annual_volatilitiy = None
        self.stock_data = None
        self.sp500_data = None
        
    def geting_data(self, word):
        self.answer = str(word)
        #getting the data
        self.stock_data = yf.download(self.answer, period="6mo")
        self.sp500_data = yf.download("^GSPC", period="6mo")
        #daily returns
        self.stock_data["Log Returns"] = np.log(self.stock_data["Close"] / self.stock_data["Close"].shift(1))
        self.sp500_data["Log Returns"] = np.log(self.sp500_data["Close"] / self.sp500_data["Close"].shift(1))

        self.daily_volatility = self.stock_data["Log Returns"].std() #standard deviation
        self.annual_volatility = self.daily_volatility * np.sqrt(252) # calculating for a year
        print(f"Daily volatility: {self.daily_volatility}")
        print(f"Annual Volatility:{self.annual_volatility}") # oboje se izrazava u postotku
        
        

    def __repr__(self):
        return f"stocks_app(company={self.answer}, daily_volatility={self.daily_volatility}, annual_volatility={self.annual_volatility})"
    
    

    