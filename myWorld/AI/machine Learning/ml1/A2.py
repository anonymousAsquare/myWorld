import numpy as np
import pandas as pd 
import math

def linear_gradient(x,y):
    m = 0
    b = 0
    n = len(x)
    a = 0
    iteration = 1200000
    learningRate = 0.0001
    for i in range(iteration):
        y_predict = m * x + b
        cost = (1/n) * sum([i**2 for i in (y-y_predict)])
        md = -(2/n) * sum(x*(y-y_predict))
        bd = -(2/n) * sum(y-y_predict)
        m = m - learningRate * md
        b = b - learningRate * bd

        print('m{}, b{}, cost{}, iteration{}'.format( m, b, cost, i))
        l = math.isclose(a,cost,rel_tol=1e-20)
        print(l)
        a = cost
        if l:
            break

df = pd.read_csv('machine Learning/ml1/test_scores.csv')
x= np.array(df['math'])
y = np.array(df['cs'])

linear_gradient(x,y)
