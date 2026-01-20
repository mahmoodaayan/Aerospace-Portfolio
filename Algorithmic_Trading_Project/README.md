# Algorithmic Trading Bot (Nvidia)
**Project Type:** Financial Engineering / Automation

## Overview
A live trading algorithm that queries real-time stock market data to identify trend reversals using the "Golden Cross" strategy.

## Key Features
* **Live Data Ingestion:** Uses the `yfinance` API to pull real-time market data (OHLCV) from Yahoo Finance.
* **Trend Analysis:** Calculates rolling Moving Averages (50-Day vs 200-Day) to filter market noise.
* **Signal Generation:** Automatically detects Bullish (Buy) and Bearish (Sell) signals based on crossover logic.
* **Visualization:** Renders a dynamic Matplotlib dashboard with conditional area formatting to highlight profit zones.

## Technologies
* Python (Pandas, Matplotlib, Yfinance)
