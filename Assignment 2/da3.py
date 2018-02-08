from scipy.stats.stats import pearsonr  
import statistics
import pandas
import numpy
import numbers

basepay = []
overtime_pay = []
other_pay = [] 
benefits = [] 

	

dx = pandas.read_excel('SALARY.xlsx', sheet='Sheet1')

for i in range(0,len(dx)):
	if(dx['Year'][i]==2014):
		basepay_value=dx['BasePay'][i]
		other_value=dx['OtherPay'][i]
		overtime_value=dx['OvertimePay'][i]
		benefits_value=dx['Benefits'][i]
		if(basepay_value!="Not Provided"):
			basepay.append(basepay_value)
		if(overtime_value!="Not Provided"):
			overtime_pay.append(overtime_value)
		if(other_value!="Not Provided"):
			other_pay.append(other_value)
		if(benefits_value!="Not Provided"):
			benefits.append(benefits_value)


corr1=numpy.corrcoef(basepay,overtime_pay)[0][1]
corr2=numpy.corrcoef(basepay,other_pay)[0][1]
corr3=numpy.corrcoef(basepay,benefits)[0][1]

print corr1
print corr2
print corr3

