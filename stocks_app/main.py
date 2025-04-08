# Importing necessary functions from the features package
from data_acess.features.risk_evaluation.beta.beta_coeficent import beta_coef
from data_acess.features.risk_evaluation.shape.shapera import shape_ratio  # Importing the function directly
from data_acess.features.risk_evaluation.value.risk_value import value_at_risk 
from data_acess.data.api_data import stocks_app  # Importing the stocks_app class
from ui.new_apporach import MyApp
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
import yfinance as yf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def main():
    print('I launched')
    

if __name__ == "__main__":
    main()
    app = QApplication(sys.argv)
    window = MyApp()
    #window.refresh_api_signal.connect(refresh_api)
    window.show()
    sys.exit(app.exec())