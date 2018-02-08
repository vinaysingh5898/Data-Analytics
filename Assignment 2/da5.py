import pandas as pd
import numpy as np

dx = pd.read_excel('GAMES.xlsx')

Rating = []
Year_of_Release = []

for i in range(0,len(dx)):
	Rating.append ( dx['Rating'][i] )
	Year_of_Release.append( dx['Year_of_Release'][i])

df=pd.DataFrame({'Year_of_Release' :Year_of_Release,'Rating':Rating})
s = df.groupby('Year_of_Release').agg({'Rating': ['count']}).reset_index(level=0)
s.columns = [col[1] if col[1] else col[0] for col in s.columns.tolist()]
print(s)