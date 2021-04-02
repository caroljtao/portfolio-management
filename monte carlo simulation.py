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

# asset pricing with monte carlo simulation
