stocks=['JNJ','AAPL','SLF-PC.TO','QCOM']            #johnson and johnson, apple, sunlife financial, quanlcomm
portfolio=pd.DataFrame()
for i in stocks:
    portfolio(i)=wb.DataReader(i,data_source="yahoo",start="2020-09-01")
