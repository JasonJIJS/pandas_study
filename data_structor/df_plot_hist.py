import pandas as pd                     # 191230
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]              # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']        # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)

# 한글 설정
matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 행, 열 전치하여 히스토그램 그리기
tdf_ns = df_ns.T
tdf_ns.plot(kind = 'hist', title = '남북한 발전 전력량')

plt.show()