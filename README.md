

# Brent Oil Price Analysis

## Project Overview

This project aims to analyze how significant political, economic, and technological events affect Brent oil prices. By examining the impact of factors like geopolitical events, economic indicators, and regulatory changes, this analysis provides insights for investors, analysts, and policymakers. The project is conducted by **Birhan Energies** to support stakeholders in making informed decisions in the volatile oil market.

### Key Objectives

1. **Identify Events Impacting Oil Prices**: Analyze historical Brent oil prices to find correlations with major events.
2. **Understand Influencing Factors**: Assess the role of economic indicators, technological advancements, and regulatory changes on oil prices.
3. **Provide Actionable Insights**: Generate insights for investment, policy, and operational strategies.
4. **Dashboard for Visualization**: Develop an interactive dashboard for exploring analysis results.

## Situational Overview

Birhan Energies is a consultancy firm specializing in providing data-driven insights to the energy sector. Given the volatility of the oil market, investors, policymakers, and energy companies require detailed analyses to inform their strategies and decision-making processes. This project provides a comprehensive approach to understanding Brent oil price trends and the factors affecting them.

## Data

- **Source**: Historical daily prices of Brent oil from **May 20, 1987, to September 30, 2022**.
- **Fields**:
  - `Date`: The date of the recorded Brent oil price.
  - `Price`: The price of Brent oil in USD per barrel on the corresponding date.

Additional datasets include economic indicators, such as GDP growth, inflation rates, and exchange rates.

## Project Structure

The project folder is structured as follows:

```plaintext
.
├── .github/workflows            # GitHub workflows for CI/CD
├── data                          # Data folder
│   ├── external                  # External datasets (e.g., exchange rates, GDP growth)
│   ├── processed                 # Processed data with features
│   └── raw                       # Raw data files (Brent oil prices, merged datasets)
├── models                        # Models for statistical and machine learning analyses
├── notebooks                     # Jupyter Notebooks for exploratory data analysis (EDA) and modeling
├── src                           # Source code for the main application
│   ├── dashboard                 # React frontend for the dashboard
│   └── data_processing           # Data processing scripts
└── tests                         # Unit tests
```

## Installation

### Prerequisites

- Python 3.8 or above
- Node.js and npm
- Libraries and dependencies listed in `requirements.txt`

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/brent-oil-price-analysis.git
   cd brent-oil-price-analysis
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**:
   ```bash
   cd src/dashboard
   npm install
   ```

## Data Analysis Workflow

The analysis process is divided into the following tasks:

### Task 1: Define Data Analysis Workflow
- Outline analysis steps and processes.
- Understand data and models, identify assumptions, and prepare data for processing.

### Task 2: Statistical and Econometric Analysis
- Apply time series models (e.g., ARIMA, GARCH) and explore economic indicators, technological changes, and political factors impacting oil prices.
- Use models like Vector Autoregression (VAR) and Markov-Switching ARIMA.

### Task 3: Develop an Interactive Dashboard
- **Backend (Flask)**: Serve data and analysis results.
- **Frontend (React)**: Create a user-friendly interface for visualization.
- **Key Features**:
  - Visualize historical trends, forecasts, and correlations with events.
  - Interactive filters, date ranges, and event highlights.

## Usage

### Running the Dashboard

1. **Start the Flask backend**:
   ```bash
   python src/data_processing/brent_oil_data_analysis.py
   ```

2. **Start the React frontend**:
   ```bash
   cd src/dashboard
   npm start
   ```

3. **Access the dashboard** at `http://localhost:3000`.

## Data Processing and Modeling

1. **Data Collection**:
   - External datasets such as `GDP`, `Inflation`, and `Exchange Rates` are sourced from organizations like the World Bank and IMF.

2. **Data Preprocessing**:
   - Data cleaning, handling missing values, and standardizing formats for consistency.

3. **Exploratory Data Analysis (EDA)**:
   - Visualizations and statistical analyses to identify trends and relationships in data.

4. **Model Building**:
   - Develop models including ARIMA, VAR, and LSTM to capture time series patterns.

## Tests

Unit tests are located in the `tests` folder. Run tests using:

```bash
pytest tests/
```



## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Contributing

Contributions are welcome! Please follow the guidelines in `CONTRIBUTING.md`.





