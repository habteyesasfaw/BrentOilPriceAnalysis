# tests/test_task1_analysis.py

import pytest
import pandas as pd
import sys
import os

# Set the base path of the project
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/data_processing'))
sys.path.insert(0, base_path)

# Create the data/raw directory if it doesn't exist
data_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/raw'))
os.makedirs(data_directory, exist_ok=True)

from brent_oil_data_analysis import load_data, preprocess_data, eda, check_stationarity

@pytest.fixture
def sample_data():
    """Sample data for testing."""
    data = {
        'Date': pd.to_datetime(['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05']),
        'Price': [65, 67, 68, 70, 69]
    }
    return pd.DataFrame(data)



    # Use pd.testing to compare DataFrames
    pd.testing.assert_frame_equal (data.reset_index(drop=True), sample_data.reset_index(drop=True))

def test_preprocess_data(sample_data):
    """Test the data preprocessing function."""
    processed_data = preprocess_data(sample_data)
    assert not processed_data.isnull().values.any()  # Ensure there are no missing values

