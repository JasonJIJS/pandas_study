import matplotlib                       # 191231
import pandas as pd
import matplotlib.pyplot as plt


matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# Excel 데이터를 데이터프레임 변환
df = pd.read_excel('시도별 전출입 인구수.xlsx', fillna=0, header=0)

# 전출지별에서 누락값(NaN)을 앞 데이터로 채움(엑셀 양식 병합 부분)
df = df.fillna(method='ffill')

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별': '전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

df_4['합계'] = df_4.sum(axis=1) # 2010~2017년 이동 인구 수를 합계하여 새로운 열로 추가
df_total = df_4[['합계']].sort_values(by='합계', ascending = True)  # 가장 큰 값부터 정렬

# 스타일 서식 지정
plt.style.use('ggplot')

# 수평 막대 그래프 그리기
df_total.plot(kind = 'barh', color = 'cornflowerblue', figsize = (20, 10), width=0.5 )

plt.title('서울 -> 타시도 인구 이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')

plt.show()