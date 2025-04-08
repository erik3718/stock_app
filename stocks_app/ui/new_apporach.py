import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
import yfinance as yf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
from data_acess.data.api_data import stocks_app
from data_acess.features.risk_evaluation.value.risk_value import  value_at_risk
from data_acess.features.risk_evaluation.beta.beta_coeficent import beta_coef
from data_acess.features.risk_evaluation.shape.shapera import shape_ratio



my_instance = stocks_app()



class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load the UI file
        uic.loadUi('stock.ui', self)

        
        self.button1.clicked.connect(self.on_click_beta_coef)  # Connect button click to the function
        self.button2.clicked.connect(self.on_click_shape_ratio)
        self.button3.clicked.connect(self.on_click_value_at_risk)
        self.load_button.clicked.connect(self.on_click_load)
                
    def on_click_load(self):
        stock_ticker = self.stock_name.text()  
        my_instance.geting_data(stock_ticker)
    
    def on_click_value_at_risk(self):
        var_1d, var_10d, log_returns = value_at_risk(my_instance) 
    
        if log_returns is None:
            return  # Exit if there's no data to plot

        # Plot histogram of returns with VaR
        plt.figure(figsize=(10, 6))
        sns.histplot(log_returns, bins=50, kde=True, color="blue")
        plt.axvline(var_10d, color="red", linestyle="dashed", linewidth=2, label=f"95% VaR (10 days): {var_10d:.4f}")

        # Final plot settings
        plt.title(f"{self.stock_name} Daily Returns & 95% VaR")
        plt.xlabel("Daily Returns")
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()

    def on_click_beta_coef(self):
        beta, data = beta_coef(my_instance)
        # 7. Plotting the log returns
        plt.figure(figsize=(10, 6))
        sns.regplot(x=data["SP500"], y=data["Stock"], marker='o', color='blue', line_kws={"color": "red"})
        
        # 8. Final plot settings
        plt.title(f"Log Returns: Stock vs S&P 500 (Beta: {beta:.4f})")
        plt.xlabel("S&P 500 Log Returns")
        plt.ylabel(f"{self.stock_name} Log Returns")
        plt.grid()
        plt.show()
        
    def on_click_shape_ratio(self):
        # Calculate Sharpe Ratio
        sharpe_ratio, average_return, risk_free_rate = shape_ratio(my_instance)  # Use 'self' if this is a method of a class

        if sharpe_ratio is None:  # Check if the calculation was successful
            return

        # Plotting the distribution of log returns
        plt.figure(figsize=(10, 6))
        sns.histplot(my_instance.stock_data["Log Returns"], bins=30, kde=True, color='blue', stat='density')
    
        # Add a vertical line for the average return
        plt.axvline(average_return, color='red', linestyle='dashed', linewidth=2, label=f'Average Return: {average_return:.4f}')
    
        # Add a vertical line for the risk-free rate
        plt.axvline(risk_free_rate, color='green', linestyle='dashed', linewidth=2, label=f'Risk-Free Rate: {risk_free_rate:.4f}')
        
        # Add a title and labels
        plt.title(f"Distribution of Log Returns\nSharpe Ratio: {sharpe_ratio:.4f}")
        plt.xlabel("Log Returns")
        plt.ylabel("Density")
        plt.legend()
        plt.grid()
        plt.show()

