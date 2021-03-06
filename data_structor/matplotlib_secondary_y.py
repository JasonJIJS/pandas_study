import matplotlib                       # 191231
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'NanumGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 스타일 서식 지정
plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus']=False

df= pd.read_excel('./남북한발전전력량.xlsx', convert_float=True)
df= df.loc[5:9]
df.drop('전력량 (억kwh)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace = True)
df = df.T

df = df.rename(columns = {'합계':'총발전량'})
df['총발전량 -1년'] = df['총발전량'].shitf(1)
df['증감율'] = ((df['총발전량'] / df['총발전량 - 1년'])-1) * 100
print(df.head())

# 2축 그래프 그리기
ax1 = df[['수력', '화력']].plot(kind='bar', figsize =(20,10), width=0.7, stacked = True)
ax2 = ax1.twinx()
ax2.plot(df.index, df.증감율, ls='--', marker = 'o', markersize=20, color='green', label ='전년대비 증감율(%)')

ax1.set_ylim(0, 500)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size = 20)
ax1.set_ylabel('발전량(억 kwh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량(1990 ~ 2016)', size = 30)
ax1.legend(loc = 'upper left')

plt.show()
