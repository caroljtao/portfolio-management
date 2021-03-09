# portfolio-management.py
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

JNJ=wb.DataReader("JNJ",data_source="yahoo",start="2020-09-01")
JNJ.head()
JNJ['Adj Close'].plot(figsize=(10,6))                    #plot the price trend
JNJ['discrete return']=JNJ['Adj Close']/JNJ['Adj Close'].shift(1)-1    #calculate the simple return
JNJ['discrete return'].head()
JNJ['discrete return'].plot(figsize=(10,6))              #check out the chart of simple return
average_discrete_return=JNJ['discrete return'].mean()
print(average_discrete_return)                 # calculate the average return in the period
annualized_discrete_return = average_discrete_return*250              #the annulized return is 0.12085043873983932 (jupyter notebook's output)
log_return=np.log(JNJ['discrete return']/JNJ['discrete return'].shift(1))
log_return.plot(figsize=(10,6))


