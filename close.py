"""
    @ Author    : hong-il
    @ Date      : 2021-07-24
    @ File name : close.py
    @ File path : 
    @ Description : 
"""
from datetime import datetime
import pandas_datareader as pa
from financeDB import financeDB

# DB 커넥션 클래스 초기화
fb = financeDB()
# DB 커넥트
conn = fb.get_connection()

start = datetime(2021, 7, 22)
end = datetime(2021, 7, 23)

# LG 일렉트로닉스
df = pa.DataReader("066570.KS", "yahoo", start, end)
# 데이터프레임 → 딕셔너리 변환
dd = df["Adj Close"].to_dict()

# 딕셔너리 키, 밸류 반복문
for k, v in dd.items():
    sql = (f"""
        INSERT INTO stock_close (
            ID
            , DT
            , ADJ_CLOSE
            , REG_DTM
            , REG_ID
        ) VALUES (
            '066570.KS'
            , {str(k).replace('-', '')[0:8]}
            , {v}
            , NOW()
            , 'init'
        ) ON DUPLICATE KEY UPDATE 
            ADJ_CLOSE = {v}
            , REG_DTM = NOW()
            , REG_ID = 'modi'
    """)
    # SQL 실행
    with conn.cursor() as cur:
        cur.execute(sql)

# DB 커밋
conn.commit()
