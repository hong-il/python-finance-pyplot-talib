"""
    @ Author    : hong-il
    @ Date      : 2021-07-23
    @ File name : bband.py
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

# LG 일렉트로닉스
df = pa.DataReader("066570.KS", "yahoo", start, end)

p_start = time.time()
# 볼린저 밴드 직접 연산
df['p_MA'] = df['Adj Close'].rolling(window=20).mean()
df['p_STD'] = df['Adj Close'].rolling(window=20).std()
df['p_bb_UPPER'] = df['p_MA'] + (df['p_STD'] * 1.5)
df['p_bb_LOWER'] = df['p_MA'] - (df['p_STD'] * 1.5)
print(f"Pandas 시간 측정 : {time.time() - p_start}")
# 그래프 사이즈
plt.figure(figsize=(12.5, 5))
# 그래프 타이틀
plt.title('p_bband')
# 꺾은선 그래프 3종
plt.plot(df.index, df['p_bb_UPPER'], label='upper_bband')
plt.plot(df.index, df['p_MA'], label='ma')
plt.plot(df.index, df['p_bb_LOWER'], label='lower_bband')
# 범례 위치
plt.legend(loc='upper right')
plt.show()

t_start = time.time()
# ta-lib 연산
df['t_bb_UPPER'], df['t_MA'], df['t_bb_LOWER'] = ta.BBANDS(df['Adj Close'], 20, 1.5)
print(f"TA-LIB 시간 측정 : {time.time() - t_start}")
# 그래프 사이즈
plt.figure(figsize=(12.5, 5))
# 그래프 타이틀
plt.title('t_bband')
# 꺾은선 그래프 3종
plt.plot(df.index, df['t_bb_UPPER'], label='upper_bband')
plt.plot(df.index, df['t_MA'], label='ma')
plt.plot(df.index, df['t_bb_LOWER'], label='lower_bband')
# 범례 위치
plt.legend(loc='upper right')
plt.show()



