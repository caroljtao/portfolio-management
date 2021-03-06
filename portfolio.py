stocks=['JNJ','AAPL','SLF-PC.TO','QCOM']            #johnson and johnson, apple, sunlife financial, quanlcomm
portfolio=pd.DataFrame()
for i in stocks:                   
    portfolio[i]=wb.DataReader(i,data_source="yahoo",start="2020-09-01")['Adj Close']
portfolio.head() 
portfolio.iloc[0][1]
(portfolio/portfolio.iloc[0]*100).plot(figsize=(10,6)              #normalize each stock's return and plot it
(discrete_return=portfolio/portfolio.shift(1)-1).plot(figsize=（10,6))
log_return=np.log(portfolio/portfolio.shift(1)).plot(figsize=(10,6))
weight=[0.3,0.4,0.1,0.2]
np.dot(discrete_return,weight)             #return a matrix that contains the portfolo return on each day, can't be right. Gotta average the return of each stock and then dot
portfolio return = np.dot(discrete_return.mean()*250,weight)
print(portfolio_return)
# covariance calculation in the following
discrete_return.cov()*250
discrete_return.corr()          #calculate the correlation table for the portfolio (JNJ, Sunlife and QCOMM are good diversifiers)
#calculate portfolio variance and volatility
weight=np.array([0.3,0.4,0.1,0.2])
portfolio_var=np.dot(weight.T, np.dot(discrete_return.cov()*250 ,weight))    #variance
print((portfolio_var)**0.5)       #volatility
