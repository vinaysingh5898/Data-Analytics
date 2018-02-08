import csv
import numpy as np 
import pandas
from sklearn.svm import SVR
import matplotlib.pyplot as pyplot

dx = pandas.read_excel('STOCKS.xlsx', sheet='Sheet1')

Date=[]
Open=[]
High=[]
Low=[]
Close=[]
Volume=[]
Name=[]

def predict_prices(dates,price,x):
	dates=np.reshape(dates,(len(dates),1))

	svr_lin=SVR(kernel='linear',C=1e3)
	svr_poly=SVR(kernel='poly',C=1e3,degree=2)
	svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)

	plt.scatter(dates,prices,color='black',label='Data')
	plt.plot(dates,svr_rbf.predict(dates),color='red',label='RBF model')
	plt.plot(dates,svr_lin.predict(dates),color='green',label='Linear model')
	plt.plot(dates,svr_poly.predict(dates),color='blue',label='Polynomial')
	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Vector Regression')
	plt.legend()
	plt.show()
	return svr_rbf.predict(x)[0],svr_lin.predict(x)[0],svr_poly.predict(x)[0]


for i in range(0,len(dx)):
	date_value=dx['Date'][i].day
	open_value=dx['Open'][i]
	high_value=dx['High'][i]
	low_value=dx['Low'][i]
	close_value=dx['Close'][i]
	vol_value=dx['Volume'][i]
	name_value=dx['Name'][i]
	Date.append(date_value)
	Open.append(high_value)
	Low.append(low_value)
	Close.append(close_value)
	Volume.append(vol_value)
	Name.append(name_value)

#predicted_prices=predict_prices(Date,Open,30)
#print(predicted_prices)
