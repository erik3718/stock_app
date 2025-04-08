import pandas as pd
import numpy as np
from data_acess.data.api_data import stocks_app


def beta_coef(stock_app_instance):
        # Ensure that the data is available
        if stock_app_instance.stock_data is None or stock_app_instance.sp500_data is None:
            print("Please run getting_data() first to fetch stock data.")
            return
    
        #removing the Nan values
        data = pd.DataFrame({
            "Stock": stock_app_instance.stock_data["Log Returns"], 
            "SP500" : stock_app_instance.sp500_data["Log Returns"]
            }).dropna()

        #calculating the variance
        cov_matrix = np.cov(data["Stock"], data["SP500"])
        beta = cov_matrix[0, 1] / cov_matrix[1, 1]

        print(f"Beta coefficient: {beta}") 
        return beta, data                   #if beta bigger than 1 then stock riskier than the market
    