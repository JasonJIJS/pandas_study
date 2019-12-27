import pandas as pd                          # 191227

df = pd.read_csv('stock-data.csv')
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수

print("# 문자열인 날짜 데이터를 판다스 Timestamp로 변환")
df['new_Date'] = pd.to_datetime(df['Date'])     # 새로운 열에 추가
df = df.set_index('new_Date')                   # 행 인덱스로 지정
print(df.head(), '\n', df.index, '\n')

print("# 날짜 인덱스를 이용하여 데이터 선택")
df_y = df['2018']
print(df_y.head(), '\n')

print("# loc 인덱서 활용")
df_ym = df.loc['2018-07']
print(df_ym, '\n')

print("# 열 범위 슬라이싱")
df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols, '\n')
df_ymd = df['2018-07-02']
print(df_ymd, '\n')

print("# 날짜 범위 지정")
df_ymd_range = df['2018-06-25':'2018-06-20']
print(df_ymd_range, '\n')

print("# 시간, 간격 계산, 최근 180일 ~189일 사이의 값들만 선택")
today = pd.to_datetime('2018-12-15')        # 기준일 생성
df['time_delta'] = today - df.index        # 날짜 차이 계산
df = df.set_index('time_delta')             # 행 인덱스로 지정
df_180 = df['180 days':'189days']
print(df_180)