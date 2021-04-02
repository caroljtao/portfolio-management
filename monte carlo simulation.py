import numpy as np
import matplotlib.pyplot as plt
rev_mean=100
rev_stdd=20
iterations=1000
rev=np.random.normal(rev_mean,rev_stdd,iterations)
plt.figure(figsize=(10,6))
plt.plot(rev)          #shows that the mean value floats around 100
COGS=-(rev*np.random.normal(0.6,0.1))    #COGS equals 60% of the revenue and the stdd= 10%
plt.figure(figsize=(10,6))
COGS.mean()
COGS.std()
