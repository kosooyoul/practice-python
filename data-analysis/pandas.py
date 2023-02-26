import pandas as pd
import numpy as np

from numpy.random import randn
np.random.seed(101)

s = pd.Series(data=[10, 20, 30])
print(s)

df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df['W'])
print(df['W'] + df['Y'])