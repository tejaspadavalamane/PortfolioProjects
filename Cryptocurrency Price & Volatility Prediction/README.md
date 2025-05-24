# 📈 Cryptocurrency Price and Volatility Prediction using Python

## Overview
This project analyzes and forecasts cryptocurrency market behavior using historical OHLCV data. It applies statistical models and machine learning algorithms to assess both price trends and volatility for risk-aware decision-making.

## 🔍 Objectives
- Perform time series analysis on Bitcoin, Ethereum, and Litecoin
- Predict price movements and volatility using GARCH and LSTM
- Evaluate model performance using RMSE, RMSPE
- Generate insights for traders and analysts in crypto finance

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

## 📁 Project Structure

cryptocurrency-volatility-prediction/
│
├── data/
│   ├── BTCUSDT.csv
│   ├── ETHUSDT.csv
│   ├── LTCUSDT.csv
│   └── Preprocess.csv
│
├── notebooks/
│   ├── price_prediction.ipynb
│   └── volatility_prediction.ipynb   
│
├── scripts/
│   └── btpre.py
│
├── docs/
│   ├── Project_Report.pdf
│   ├── Presentation_Slides.pptx
│   ├── Price_Prediction.pdf          
│   └── Volatility_Prediction.pdf     
│
└── README.md

## 📌 Key Takeaways
- Volatility in crypto markets shows strong temporal clustering
- GARCH models outperform baselines in short-term volatility forecasting
- LSTM models show potential for capturing complex nonlinear patterns
- Analytical results inform data-backed crypto trading strategies

## 👨‍💻 Tech Stack
- **Languages**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, `statsmodels`, TensorFlow/Keras
- **Tools**: Jupyter Notebook, Git/GitHub
