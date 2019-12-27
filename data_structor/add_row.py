import pandas as pd     # 191224
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름': ['서준', '우현', '인아'],
             '수학':[90, 80, 70],
             '영어':[98, 89, 95],
             '음악':[85, 95, 100],
             '체육':[100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df = df.set_index('이름')
print(df)
print()

print("# 새로운 행(row)을 추가- 같은 원소 값을 입력")
df.loc['재삼'] = 90      # 한개 넣을때는 그냥
print(df)
print()

df.loc['창도'] = [100, 100, 100, 100]
print(df)
print()

df.loc['승영'] = df.iloc[4]
print(df)
print()
