import pandas as pd
import numpy as np
from data_acess.data.api_data import stocks_app


def shape_ratio(stock_app_instance):
    # Ensure that the data is available
    if stock_app_instance.stock_data is None or stock_app_instance.sp500_data is None:
        print("Please run getting_data() first to fetch stock data.")
        return
    
    risk_free_rate = 0.03 /252
    average_return = stock_app_instance.stock_data["Log Returns"].mean()
    daily_volatility = stock_app_instance.daily_volatility
    sharpe_ratio = (average_return - risk_free_rate) / daily_volatility
    print(f"Shape Ratio:{sharpe_ratio}") 
    
    return sharpe_ratio, average_return, risk_free_rate