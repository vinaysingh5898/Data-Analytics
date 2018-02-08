from scipy.stats.stats import pearsonr  
import statistics
import pandas
import numpy

sugar = []
rating = []  

# Polynomial Regression
def polyfit(x, y, degree):
    results = {}

    coeffs = numpy.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results['determination']



dx = pandas.read_excel('NUTRITION.xlsx', sheet='Sheet1')

for i in range(1,len(dx)):
	sugar_value=dx['sugars'][i]
	print(sugar_value)
	rating_value=dx['rating'][i]
	sugar.append(sugar_value)
	rating.append(rating_value)

print("correlation matrix")
print numpy.corrcoef(sugar,rating)
print("")
print ("Negative correlation\n")

r_sq=polyfit(sugar,rating,3)
print 'R-squred-',r_sq