# task1_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from statsmodels.tsa.stattools import adfuller
from typing import Tuple

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path: str) -> pd.DataFrame:
    """Loads data from a CSV file and parses dates."""
    try:
        data = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
        logging.info("Data loaded successfully.")
        return data
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses data: removes missing values and renames columns."""
    # Drop missing values
    data = data.dropna()
    # Rename columns to be more uniform
    data.columns = ['Date', 'Price']
    # Set date as index for time series analysis
    data.set_index('Date', inplace=True)
    logging.info("Data preprocessed successfully.")
    return data

def eda(data: pd.DataFrame):
    """Performs exploratory data analysis and visualization on the dataset."""
    # Summary statistics
    logging.info("Performing EDA...")
    print(data.describe())

    # Plotting the time series
    plt.figure(figsize=(12, 6))
    plt.plot(data['Price'], label='Brent Oil Price')
    plt.title('Brent Oil Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

    # Distribution plot
    plt.figure(figsize=(10, 5))
    sns.histplot(data['Price'], bins=50, kde=True)
    plt.title('Distribution of Brent Oil Prices')
    plt.xlabel('Price (USD)')
    plt.ylabel('Frequency')
    plt.show()
    logging.info("EDA completed.")

def check_stationarity(data: pd.Series, window: int = 12) -> Tuple[float, float]:
    """Checks the stationarity of the time series using rolling statistics and ADF test."""
    rolling_mean = data.rolling(window=window).mean()
    rolling_std = data.rolling(window=window).std()

    # Plot rolling statistics
    plt.figure(figsize=(12, 6))
    plt.plot(data, label='Original')
    plt.plot(rolling_mean, color='red', label='Rolling Mean')
    plt.plot(rolling_std, color='black', label='Rolling Std')
    plt.legend()
    plt.title('Rolling Mean and Standard Deviation')
    plt.show()

    # Perform ADF test
    adf_test = adfuller(data)
    adf_stat, p_value = adf_test[0], adf_test[1]
    logging.info(f"ADF Statistic: {adf_stat}")
    logging.info(f"p-value: {p_value}")

    return adf_stat, p_value
