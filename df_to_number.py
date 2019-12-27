import seaborn as sns       # 191226
import pandas as pd
pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 600)

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
print(titanic.head())
df = titanic.loc[:, ['age', 'fare']]

print(df.head(), type(df), sep='\n')
print()

print("# 데이터프레임에 숫자 10 더하기")
addition = df + 10
print(addition.head(), type(addition), sep = '\n') # 첫 5행만 표시


