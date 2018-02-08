import pandas
import numpy as np
import xlrd
import matplotlib.pyplot as plt

def reject_outlier(data, m=2):
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def five_points(data):
    minx   = np.min(data)
    Q1     = np.percentile(data, 25)
    median = np.median(data)
    Q3     = np.percentile(data, 75)
    maxx   = np.max(data)
 
    return (minx,Q1,median,Q3,maxx)

df = pandas.read_excel('EARTHQUAKE.xlsx', sheet='Sheet1') 

latitude_array=[]
longitude_array=[]
depth_array=[]
magnitude_array=[]

for i in range(0,len(df)):
	latitude_value=df['Latitude'][i]
	longitude_value=df['Longitude'][i]
	depth_value=df['Depth/Km'][i]
	magnitude_value=df['Magnitude'][i]

	latitude_array.append(latitude_value)
	longitude_array.append(longitude_value)
	depth_array.append(longitude_value)
	magnitude_array.append(longitude_value)

fpoint_latitude=five_points(latitude_array)
fpoint_longitude=five_points(longitude_array)
fpoint_depth=five_points(depth_array)
fpoint_magnitude=five_points(magnitude_array)

data_points=[fpoint_latitude,fpoint_longitude,fpoint_depth,fpoint_magnitude]

plt.figure()
plt.boxplot(data_points)

plt.show()

print(fpoint_latitude)
print("\n")
print(fpoint_longitude)
print("\n")
print(fpoint_depth)
print("\n")
print(fpoint_magnitude)
 

