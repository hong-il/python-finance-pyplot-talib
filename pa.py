"""
    @ Author    : hong-il
    @ Date      : 2021-07-23
    @ File name : pa.py
    @ File path : 
    @ Description : 
"""
import time
from datetime import datetime

import pandas_datareader as pa
import talib as ta
import matplotlib.pyplot as plt

start = datetime(2021, 1, 1)
end = datetime(2021, 7, 23)

df = pa.DataReader("066570.KS", "yahoo", start, end)

p_start = time.time()
df['p_MA'] = df['Adj Close'].rolling(20).mean()
print(f"Pandas 시간 측정 : {time.time() - p_start}")
df['p_MA'].plot(figsize=(12.5, 5))
plt.title('p_MA')
plt.show()

t_start = time.time()
df['t_MA'] = ta.MA(df['Adj Close'], 20)
print(f"TA-LIB 시간 측정 : {time.time() - t_start}")
df['t_MA'].plot(figsize=(12.5, 5))
plt.title('t_MA')
plt.show()
