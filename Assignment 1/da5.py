import pandas
import numpy as np
import xlrd
import matplotlib.pyplot as plt

min_temp=[]
max_temp=[]

for i1 in range(5,60):
	df1 = pandas.read_excel('WEATHER.xlsx', sheetname=i1)
	for j1 in range (3,26):
		min_temp1=df1['Unnamed: 4'][j1]
		min_temp.append(min_temp1)
df2 = pandas.read_excel('WEATHER.xlsx', sheetname=60)
for k1 in range(3,15):
		min_temp2=df2['Unnamed: 3'][k1]
		min_temp.append(min_temp2)

for i in range(5,60):
	df11= pandas.read_excel('WEATHER.xlsx', sheetname=i)
	for j in range (3,26):
		max_temp1=df11['Unnamed: 3'][j]
		max_temp.append(max_temp1)

df22 = pandas.read_excel('WEATHER.xlsx', sheetname=60)
for k in range(3,15):
		max_temp2=df22['Unnamed: 3'][k]
		max_temp.append(max_temp2)

for i in range(5,60):
	df11= pandas.read_excel('WEATHER.xlsx', sheetname=i)
	for j in range (3,26):
		max_temp1=df11['Unnamed: 3'][j]
		max_temp.append(max_temp1)

df22 = pandas.read_excel('WEATHER.xlsx', sheetname=60)
for k in range(3,15):
		max_temp2=df22['Unnamed: 3'][k]
		max_temp.append(max_temp2)

print(max_temp)
print(min_temp)