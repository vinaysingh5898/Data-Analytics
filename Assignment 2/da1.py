import statistics
import pandas
import unicodedata

dx = pandas.read_excel('MOVIE.xlsx', sheet='Sheet1')

imdb_score =[]
#count=0

for i in range(1,len(dx)):
	score_value=dx['Column 27'][i]
	#score_value='u'+"'"+score_value+"'"
	score_value=float(score_value)
	#unicodedata.numeric(score_value)
	#print(type(score_value))
	#count=count+1
	imdb_score.append(score_value)



avg_score=statistics.mean(imdb_score)
median=statistics.median(imdb_score)
var=statistics.variance(imdb_score)

print(avg_score)
print(median)
print(var)
