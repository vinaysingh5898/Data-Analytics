import csv
import statistics
import math,operator
from scipy import stats

with open('CARS.csv') as csvfile:
	readCSV=csv.reader(csvfile,delimiter=',')

	speed=[]
	distance=[]

	for row in readCSV:
		speed1=row[1]
		distance1=row[2]

		speed.append(speed1)
		distance.append(distance1)


if(speed[0]=='speed'):
	del speed[0]
if(distance[0]=='dist'):
	del distance[0]
speed=map(int,speed)
distance=map(int,distance)

amean_speed=statistics.mean(speed)
amean_distance=statistics.mean(distance)

gmean_speed=stats.gmean(speed)
gmean_distance=stats.gmean(distance)

hmean_speed=stats.hmean(speed)
hmean_distance=stats.hmean(distance)

print 'speed means are','AM ',amean_speed,'GM ',gmean_speed,'HM ',hmean_speed
print 'distance means are','AM ',amean_distance,'GM ',gmean_distance,'HM ',hmean_distance
