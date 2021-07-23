# conda install -c conda-forge ta-lib
# pip install yfinance --upgrade --no-cache-dir
import talib
import yfinance as yf
import matplotlib.pyplot as plt


lg = yf.Ticker("066570.KS")
df = lg.history(start='2021-01-01', end='2021-07-23')
# df = lg.history(period='1y')
# df = lg.history(period='max')
df[['Close']].plot(figsize=(12, 12))
plt.show()

df['MA'] = talib.SMA(df['Close'], 20)
df[['Close', 'MA']].plot(figsize=(12, 12))
plt.show()

df['EMA'] = talib.EMA(df['Close'], timeperiod=20)
df[['Close', 'EMA']].plot(figsize=(12, 12))
plt.show()
