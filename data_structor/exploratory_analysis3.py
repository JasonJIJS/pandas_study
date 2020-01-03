import pandas as pd     # 191230

# read_csv 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header = None)

# 열 이름을 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

print("# 평균값")
print(df.mean())
print()

print(df['mpg'].mean())
print(df.mpg.mean())
print()
print(df[['mpg', 'weight']].mean())
print()
print("#중간값")
print(df.median())
print()
print(df['mpg'].median())
print()
print("# 최대값")
print(df.max())
print()
print(df['mpg'].max())