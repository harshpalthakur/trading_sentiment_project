# 📊 Market Sentiment × Trader Performance Analysis

## Setup in 3 Steps

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your CSV files
```
data/raw/fear_greed_index.csv       ← Drop your Fear & Greed CSV here
data/raw/historical_trades.csv      ← Drop your Hyperliquid trades CSV here
```

### 3. Run notebooks IN ORDER
```
notebooks/01_data_cleaning.ipynb
notebooks/02_eda.ipynb
notebooks/03_sentiment_vs_performance.ipynb
notebooks/04_patterns_and_strategies.ipynb
```

---

## Project Structure
```
trading_sentiment_project/
├── data/
│   ├── raw/                  ← PUT YOUR CSV FILES HERE
│   └── processed/            ← Cleaned data saved here automatically
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_sentiment_vs_performance.ipynb
│   └── 04_patterns_and_strategies.ipynb
├── outputs/
│   ├── charts/               ← All plots saved here
│   └── reports/              ← Summary stats saved here
├── src/
│   └── helpers.py            ← Shared utility functions
├── requirements.txt
└── README.md
```

## Expected CSV Columns

**fear_greed_index.csv**
| timestamp | value | classification | date |

**historical_trades.csv**
| account | symbol | size | side | execution_price | closedPnL | leverage | time | startPosition | ... |
