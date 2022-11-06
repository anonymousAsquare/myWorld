import pandas as pd
import numpy as np
from sklearn import linear_model
import math
from word2number import w2n

df =  pd.read_csv('hiring.csv')
test_score = df['test_score']
median_test_score = math.floor(test_score.median())
#print(median_test_score)
df['test_score']=df.fillna(median_test_score)
df['experience']= df.fillna(0)
test_scor = []
exp = []
for i,j in zip(df.test_score,df.experience):
    a = w2n.word_to_num(str(i))
    b = w2n.word_to_num(str(j))
    test_scor.append(a)
    exp.append(b)
test_scor = list(test_scor)
exp = list(exp)
df.test_score = test_scor
df.experience = exp

x = np.array(df.drop(df[['salary']],1))
y = np.array(df['salary'])

reg = linear_model.LinearRegression()
reg.fit(x,y)
predict = reg.predict([[12,10,10]])
print(predict)
