import pandas as pd
import numpy as np
from numpy.random import randn

# 일관된 랜덤 수 생성 설정
np.random.seed(101)

print("- 시리즈 타입 생성")
s = pd.Series(data=[10, 20, 30])
print(s, '\n')

print("- 데이터 프레임 타입 생성")
df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df, '\n')

print("- 열 간 연산")
df['New'] = df['W'] + df['Y']
print(df, '\n')

# print("- 열의 인덱스로 행의 값들 조회 -> 불가")
# print(df[0])

print("- 열 삭제")
df = df.drop('New', axis=1)
print(df, '\n')

print("- 행 간 연산")
df.loc['AB'] = df.loc['A'] + df.loc['B']
print(df, '\n')

print("- 행 삭제")
df = df.drop('AB', axis=0)
print(df, '\n')

print("- 행 인덱스로 행의 값들 조회")
print(df.iloc[0], '\n')

print("- 모든 값 조건 검사")
print(df>0, '\n')

print("- 모든 값 조건 출력")
print(df[df>0], '\n')

print("- 특정 행렬 선택 조회")
print(df.loc[['A','C'],['W','Z']], '\n')

print("- 특정 열 값에 따른 조건 출력")
print(df[df['W']>0], '\n')

# print("- 특정 열 값에 따른 조건 출력 -> 불가")
# print(df[df.loc['A']>0], '\n')

print("- 행 인덱스 초기화")
df = df.reset_index()
print(df, '\n')

print("- 특정 값으로 열 생성")
df['TEST_COL'] = 'APPLE BANANA CHOM DURIAN EGGPLANT'.split()
print(df, '\n')

print("- 특정 값으로 행 생성")
df.loc['TEST_ROW'] = 'GOOD FEVER BAD NOT_BAD GOOD GREATE'.split()
print(df, '\n')

print("- 행 인덱스 초기화")
df = df.reset_index()
print(df, '\n')

print("- 특정 열을 인덱스로 설정")
df.set_index('TEST_COL', inplace=True)
print(df, '\n')

print("- 멀티 인덱스 생성")
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

print("- 멀티 인덱스 데이터 프레임 타입 생성")
gdf = pd.DataFrame(np.random.randn(6,4), index=hier_index, columns='W X Y Z'.split())
print(gdf, '\n')

print("- 단일 인덱스를 멀티 인덱스로 교체")
df.index = hier_index
print(df, '\n')

print("- 멀티 인덱스 그룹으로 조회")
print(gdf.loc['G1'], '\n')
print(df.loc['G1'], '\n')

print("- 멀티 인덱스 그룹과 세부 인덱스로 조회")
print(gdf.loc['G1'].loc[1], '\n')
print(df.loc['G1'].loc[1], '\n')

print("- 멀티 인덱스 그룹의 조건 검사")
print(gdf.loc['G1'] > 0, '\n')

print("- 인덱스 이름 설정 및 조회")
print(gdf.index.names, '\n')
print(df.index.names, '\n')
hier_index.names = ['Group','Num']
print(gdf.index.names, '\n')
print(df.index.names, '\n')

print("- 그룹으로 데이터 프레임 조회")
print(gdf.xs('G1'), '\n')
print(df.xs('G1'), '\n')

print("- 그룹과 행 인덱스로 행 조회")
print(gdf.xs(['G1', 1]), '\n')
print(df.xs(['G2', 2]), '\n')

print("- 인덱스 이름을 지정하여 데이터 프레임 조회")
print(df.xs('G1', level='Group')) # Group이 G1인 행이 모두 출력
print(df.xs(1, level='Num')) # Num이 1인 행이 모두 출력
