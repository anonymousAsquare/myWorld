import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('machine Learning/ml1/test_scores.csv')
x= np.array(df[['math']])
y = np.array(df['cs'])

reg = linear_model.LinearRegression()
reg.fit(x,y)
print(reg.coef_)
print(reg.intercept_)

