"""
Project: Live Algorithmic Trading Bot 
Author: Aayan Mahmood 
Date: January 2025
Source: Yahoo Finance API (yfinance)

"""

import yfinance as yf
import pandas as pd 
import matplotlib.pyplot as plt 

# Data Ingestion 

print ("Downloading live data from Wall Street... ")

# Download NVDA for the last 2 years with 1 day intervals

df = yf.download("NVDA", period="2y", interval="1d")

# clean up so we only have the close price 

df = df[["Close"]].copy()


# Mathematical modeling 

df["SMA_50"] = df["Close"].rolling(window=50).mean()
df["SMA_200"] = df["Close"].rolling(window=200).mean()

# Plotting the Graphs 

plt.figure(figsize=(14, 7))

plt.plot(df.index, df["Close"], label="Nvidia Price", color="black", alpha=0.5)

plt.plot(df.index, df["SMA_50"], label="50 day SMA", color="blue", linewidth=2)
plt.plot(df.index, df["SMA_200"], label="200 day SMA", color="orange", linewidth=2)


# logic is that if 50 day > 200 day the market is bullish and if not the market is bearish 

# fill in green for buy 

plt.fill_between(df.index, df["SMA_50"].squeeze(), df["SMA_200"].squeeze(), where=( df["SMA_50"].squeeze() > df["SMA_200"].squeeze()),
                 color="green", alpha=0.3,  label ="BULLISH" )

# fill red for sell 
plt.fill_between(df.index, df["SMA_50"].squeeze(), df["SMA_200"].squeeze(), where=( df["SMA_50"].squeeze() < df["SMA_200"].squeeze()),
                 color="red", alpha=0.3,  label ="BEARISH" )

plt.title("NVDA Algorithmic Analysis: The Golden Cross")
plt.xlabel("DATE")
plt.ylabel("Stock Price ($)")
plt.legend()
plt.grid(True)
plt.show()


                 



