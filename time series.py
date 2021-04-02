import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
JNJ_regression_data=pd.read_excel("C:/Users/Caroline Tao/Desktop/JNJ.xlsx")
JNJ_regression_data.head()
Y=JNJ_regression_data['Adj Close']
X=JNJ_regression_data['Date']
Y.head(),X.head()
plt.scatter(X,Y)
plt.xlabel('time')
plt.ylabel('price')
# Time series here X needs to be converted to float int64. Date can't be used to run regression. 
constant=sm.add_constnat(X)
reg=sm.OLS(Y,constant).fit()               #turn X into float int64
slope,intercept,r,p_value,stdd_error=stats.linregress(X,Y)
slope
p_value
