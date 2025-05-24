# 📈 Cryptocurrency Price and Volatility Prediction 

## Overview
This project focuses on analyzing and predicting the price and volatility of cryptocurrencies using statistical and machine learning models. It leverages historical OHLCV (Open, High, Low, Close, Volume) data from Bitcoin, Ethereum, and Solana to model market behavior and assess forecasting accuracy.

## 🔍 Objectives
- Analyze historical trading data of major cryptocurrencies
- Model and predict price volatility using statistical and ML methods
- Compare baseline and advanced models to evaluate performance
- Provide actionable insights for risk-aware decision-making in crypto markets

## 📊 Datasets
- **Cryptos Used**: Bitcoin (BTC), Ethereum (ETH), Litecoin (LTC)
- **Format**: CSV with OHLCV structure
- **Source**: Multiple exchanges
- **Timeframe**: Multi-year historical coverage

## 🧪 Methodology
- **Exploration & Preprocessing**: Visualizations, return calculations, log returns, stationarity checks
- **Volatility Modeling**:
  - Baseline Models (Average, Random Walk)
  - ARCH/GARCH Models (Volatility clustering)
  - Machine Learning: LSTM neural networks for deep pattern learning
- **Evaluation Metrics**: RMSE, RMSPE

## 📁 Files Included
- `abc.csv`, `BTCUSDT.csv`, `ETHUSDT.csv`, `LTCUSDT.csv`: Cryptocurrency OHLCV datasets
- `Preprocess.csv`: Cleaned/preprocessed data
- `price prediction.ipynb`: Python notebook for modeling & visualization
- `btpre.py`: Python script for preprocessing
- `Volatility Prediction.pdf`: Final project report
- `group 930.pptx`: Presentation slides

## 📌 Key Takeaways
- Cryptocurrency markets are highly volatile and influenced by sentiment, news, and global factors
- GARCH and LSTM models can capture volatility patterns effectively
- Insights support traders in making data-informed decisions

## 👨‍💻 Tech Stack
- Python, Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- `statsmodels` (for GARCH), TensorFlow/Keras (for LSTM)
- GitHub for version control and collaboration