import seaborn as sns

print("# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기")
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age', 'fare']]
print(df.head())

print()

# 사용자 함수 정의
def min_max(x): # 최대값 - 최소값
    return x.max() - x.min()

print("# 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환")
result = df.apply(min_max, axis=0)      #기본값 axis = 0
print(result, type(result), sep = '\n')

result2 = df.apply(min_max, axis=1)      #기본값 axis = 0
print(result2, type(result2), sep = '\n')
