import seaborn as sns                # 200106

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 분할
grouped = df.groupby(['class'])

print("# 그룹별 age 열의 평균 집계 연산")
age_mean = grouped.age.mean()
print(age_mean, '\n')

print("# 그룹별 age 열의 표준편차 집계 연산")
age_std = grouped.age.std()
print(age_std, '\n')

print("# 그룹 객체의 age 열을 iteration 으로 z-score를 계산하여 출력")
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin :', key)
    print(group_zscore.head(3), '\n')

# z-score 를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

print("# transform()메소트를 이용하여 age 열의 데이터를 z-score로 변환")
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]], '\n')
print(len(age_zscore), '\n')
print(age_zscore.loc[0:9], '\n')
print(type(age_zscore))