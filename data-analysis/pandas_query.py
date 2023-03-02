import pandas as pd
import numpy as np

print("- 데이터 프레임 생성")
df = pd.DataFrame({
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB', 'AUOI', 'AUOI', 'AUOI'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah', 'Ahyane', 'Hanulse', 'Cookie'],
    'Sales': [200, 120, 340, 124, 243, 350, 10.1, -100, 20.5]
})
print(df, '\n')

print("- 그룹 Company 별 표준 편차 조회")
std = df.groupby('Company').std()
print(std, '\n')

print("- 그룹 Company 별 평균 조회")
print(df.groupby('Company').mean(), '\n')

print("- 그룹 Company 별 합계 조회")
print(df.groupby('Company').sum(), '\n')

print("- 그룹 Company 별 합계 조회 (전치)")
print(df.groupby('Company').sum().transpose(), '\n')

print("- 그룹 Company 별 합계에서 특정 행의 값 조회")
print(df.groupby('Company').sum().loc['AUOI'], '\n')

print("- 그룹 Company 별 합계의 평균 조회")
s = df.groupby('Company').sum() # 시리즈
print(s.mean(), '\n')

print("- 그룹 Company 별 갯수 조회")
print(df.groupby('Company').count(), '\n')

print("- 그룹 Company 별 최대값 조회")
print(df.groupby('Company').max(), '\n')

print("- 그룹 Company 별 최소값 조회")
print(df.groupby('Company').min(), '\n')

print("- 그룹 Company 별 모든 분석값 설명 조회")
print(df.groupby('Company').describe(), '\n')

print("- 그룹 Company 별 모든 분석값 설명 조회 (전치)")
print(df.groupby('Company').describe().transpose(), '\n')

print("- 다른 데이터 프레임 생성")
df2 = pd.DataFrame({
    'Company': ['EGO', 'EGO', 'ID', 'ID', 'AUOI'],
    'Person': ['Sam2', 'Charla', 'Anne', 'Varrna', 'Cherry'],
    'Sales': [20, 12, 30, 24, 33],
    'Key': ['1', '2', '3', '4', '5'],
    'Key1': ['1', '2', '3', '4', '5']
})
print(df2, '\n')

print("- 데이터 프레임 열 일치 연결")
print(pd.concat([df, df2]), '\n')

print("- 데이터 프레임 행 일치 연결")
print(pd.concat([df, df2], axis=1), '\n')

print("- 다른 데이터 프레임 생성")
df3 = pd.DataFrame({
    'SecondCompany': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'BestFriend': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sally'],
    'Key': ['1', '2', '3', '4', '5', '6'],
    'Key1': ['4', '5', '6', '1', '2', np.nan],
    'Key2': ['4', '5', '6', '1', '2', '3']
})
print(df3, '\n')

print("- 데이터 프레임 병합 (이너가 기본값, 키 자동 매치)")
print(pd.merge(df2, df3), '\n')

print("- 데이터 프레임 이너 병합")
print(pd.merge(df2, df3, how='inner', on='Key'), '\n')

print("- 데이터 프레임 아우터 병합")
print(pd.merge(df2, df3, how='outer', on='Key'), '\n')

# 에러; 키에 대해 양쪽 데이터 프레임에서 모두 정의되어 있어야 함
# print("- 데이터 프레임 키 지정 아우터 병합")
# print(pd.merge(df2, df3, how='outer', on=['Key1', 'Key2']), '\n')

print("- 다른 데이터 프레임 생성")
df4 = pd.DataFrame({
    'ThirdCompany': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB'],
    'ExFriend': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Sally'],
    'Key2': ['4', '5', '6', '1', '2'],
    'Key1': ['4', '5', '6', '1', '2']
})
print(df4, '\n')

print("- 데이터 프레임 키 지정 아우터 병합")
print(pd.merge(df3, df4, on=['Key1', 'Key2']), '\n')

# 조인은 인덱싱된 열 기준으로 병합됨, 키 지정 없음
# 인덱싱된 열로 조인
print("- 데이터 프레임 이너 조인")
print(df.join(df3, how='inner'), '\n')

print("- 데이터 프레임 아우터 조인")
print(df.join(df3, how='outer'), '\n')

# 인덱스 변경 후, 조인
df.index = ['K2', 'K3', 'K5', 'K9', 'K4', 'K7', 'K1', 'K6', 'K8']
df3.index = ['K3', 'K1', 'K9', 'K4', 'K6', 'K8']
print("- 데이터 프레임 인덱스 변경 후, 이너 조인")
print(df.join(df3, how='inner'), '\n')

print("- 데이터 프레임 인덱스 변경 후, 아우터 조인")
print(df.join(df3, how='outer'), '\n')
