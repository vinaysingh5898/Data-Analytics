import pandas
import statistics
import random

dx = pandas.read_excel('IRIS.xlsx', sheet='Sheet1')

sepallength_array=[]
sepalwidth_array=[]
petallength_array=[]
petalwidth_array=[]

for i in range(0,len(dx)):
	sl_value=dx['SepalLengthCm'][i]
	sw_value=dx['SepalWidthCm'][i]
	pl_value=dx['PetalLengthCm'][i]
	pw_value=dx['PetalWidthCm'][i]

	sepallength_array.append(sl_value)
	sepalwidth_array.append(sw_value)
	petallength_array.append(pl_value)
	petalwidth_array.append(pw_value)

avg_sl=statistics.mean(sepallength_array)
avg_sw=statistics.mean(sepalwidth_array)
avg_pl=statistics.mean(petallength_array)
avg_pw=statistics.mean(petalwidth_array)

random_sl=random.sample(sepallength_array, 50)
random_sw=random.sample(sepalwidth_array, 50)
random_pl=random.sample(petallength_array, 50)
random_pw=random.sample(petalwidth_array, 50)

random_sl_var=statistics.pvariance(random_sl)
random_sw_var=statistics.pvariance(random_sw)
random_pl_var=statistics.pvariance(random_pl)
random_pw_var=statistics.pvariance(random_pw)

sample_sl_var=statistics.variance(sepallength_array)
sample_sw_var=statistics.variance(sepalwidth_array)
sample_pl_var=statistics.variance(petallength_array)
sample_pw_var=statistics.variance(petalwidth_array)

print 'sample variance: ',sample_sl_var,'population variance : ',random_sl_var
print 'sample variance: ',sample_sw_var,'population variance : ',random_sw_var
print 'sample variance: ',sample_pl_var,'population variance : ',random_pl_var
print 'sample variance: ',sample_pw_var,'population variance : ',random_pw_var