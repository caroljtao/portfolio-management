# profit forecasing with monte carlo simulation
import numpy as np
import matplotlib.pyplot as plt
rev_mean=100
rev_stdd=20
iterations=1000
rev=np.random.normal(rev_mean,rev_stdd,iterations)
plt.figure(figsize=(10,6))
plt.plot(rev)          #shows that the mean value floats around 100
COGS=-(rev*np.random.normal(0.6,0.1))    #COGS equals 60% of the revenue and the stdd= 10%
#no need to do COGS iterations 1000 times since it's a percentage of the revenue(already 1000)
plt.figure(figsize=(10,6))
COGS.mean()
COGS.std()
gross_profit=rev+COGS
gross_profit
plt.figure(figsize=(10,6))
plt.plot(gross_profit)
gross_profit.mean()
gross_profit.max()
gross_profit.min()
gross_profit.std()
plt.figure(figsize=(15,6))
plt.hist(gross_profit,bins=20)                 #draw the histogram to show the distribution of gross profits => find it's a normal distribution

###
# asset pricing with monte carlo simulation
# use the formula for asset pricing: p(Today)=p(yesterday)*e^r, r is the log return of share price between yesterday and toda
# use Brownian motion to model r (r is a random variable)
#r equals drift+volatility of the stock price.
#drift=u-0.5*stdd^2 and volatility of stock price=stdd*Z(Rand(0;1))
# Above is actually parametric method: mean + stdd*Z score 
from scipy.stats import norm
from pandas_datareader import data as wb
%matplotlib inline
data=pd.DataFrame()
ticker="JNJ"
data[ticker]=wb.DataReader("JNJ",data_source="yahoo",start="2010-01-01")['Adj Close']
data[ticker]             #Pay attention to the last 4 lines.
logreturn=np.log(1+JNJ.pct_change())
plt.figure(figsize=(10,6))
plt.plot(logreturn)       #has a stable mean and normally distributed 
u=logreturn.mean()
drift=u-0.5*logreturn.var()
np.array(drift)
drift.values
x=np.random.rand(10,2)
z_score=norm.pff(x)
time_intervals=500      #predict the prices for the next 500 days
iterations=50

np.array(drift)
returns=np.exp(drift.values+stock_stdd.values*norm.ppf(np.random.rand(time_intervals,iterations)))
returns
S0=data.iloc[-1]
price_list=np.zeros_like(returns)
price_list[0]=S0
for t in range(1, time_intervals):
  price_list[t]=price_list[t-1]*returns[t]

plt.figure(figsize=(15,6))
plt.plot(price_list)



