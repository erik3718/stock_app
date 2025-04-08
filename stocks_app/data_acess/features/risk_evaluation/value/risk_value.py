import pandas as pd
import numpy as np
from scipy.stats import norm
from data_acess.data.api_data import stocks_app

def value_at_risk(stock_app_instance):
    # Ensure that the stock data is available
    if stock_app_instance is None:
        print("Please run getting_data() first to fetch stock data.")
        return None, None, None  # Return None if data is not available

    daily_volatility = stock_app_instance.daily_volatility
    confidence_lvl = 0.95
    z_score = norm.ppf(1 - confidence_lvl)
    var_1d = z_score * daily_volatility  # VaR for 1 day
    var_10d = var_1d * np.sqrt(10)  # VaR for 10 days

    print(f"Value at Risk (1 day, {confidence_lvl * 100}% confidence): {var_1d:.2%}")
    print(f"Value at Risk (10 days, {confidence_lvl * 100}% confidence): {var_10d:.2%}")

    # Get the log returns
    log_returns = stock_app_instance.stock_data["Log Returns"].dropna()  # Ensure no NaN values



    return var_1d, var_10d, log_returns