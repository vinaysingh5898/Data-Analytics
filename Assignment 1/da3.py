import csv
import statistics

with open('AUTOMOBILES.csv') as csvfile:
	readCSV=csv.reader(csvfile,delimiter=',')

	symboling=[]
	normalized_losses=[]
	wheel_base=[]
	length=[]

	for row in readCSV:
		if(row[0]=='?'):
			row[0]='0'
		if(row[1]=='?'):
			row[1]='0'
		if(row[9]=='?'):
			row[9]='0'
		if(row[10]=='?'):
			row[10]='0'
		symboling1=row[0]
		normalized_losses1=row[1]
		wheel_base1=row[9]
		length1=row[10]

		symboling.append(symboling1)
		normalized_losses.append(normalized_losses1)
		wheel_base.append(wheel_base1)
		length.append(length1)

if(symboling[0]=='symboling'):
	del symboling[0]
if(normalized_losses[0]=='normalized-losses'):
	del normalized_losses[0]
if(wheel_base[0]=='wheel-base'):
	del wheel_base[0]
if(length[0]=='length'):
	del length[0]


normalise_col=['symboling','aspiration','make','fuel-type','num-of-doors','body-style','engine-size','horsepower']
ordinal_col=['normalized-losses','drive-wheels','engine-location','engine-type','num-of-cylinders','fuel-system']
interval_col=['wheel-base','curb-weight','compression-ratio','peak-rpm']
ratio_col=['length','width','height','bore','stroke','city-mpg','highway-mpg','price']

print "******Normalise***********"
print normalise_col
print ""
print "******Ordinal*************"
print ordinal_col
print ""
print "******Interval************"
print interval_col
print ""
print "******Ratio***************"
print ratio_col
print ""

symboling=map(int,symboling)
normalized_losses=map(int,normalized_losses)
wheel_base=map(float,wheel_base)
length=map(float,length)

sym_mean=statistics.mean(symboling)
sym_mode=statistics.mode(symboling)
sym_median=statistics.median(symboling)
print 'symboling mean:',sym_mean,' mode:',sym_mode,' median:',sym_median

norm_mean=statistics.mean(normalized_losses)
norm_mode=statistics.mode(normalized_losses)
norm_median=statistics.median(normalized_losses)
print 'normalized-loss mean:',norm_mean,' mode:',norm_mode,' median:',norm_median

wb_mean=statistics.mean(wheel_base)
wb_mode=statistics.mode(wheel_base)
wb_median=statistics.median(wheel_base)
print 'wheel-base mean:',wb_mean,' mode:',wb_mode,' median:',wb_median

len_mean=statistics.mean(length)
len_mode=statistics.mode(length)
len_median=statistics.median(length)
print 'length mean:',len_mean,' mode:',len_mode,' median:',len_median