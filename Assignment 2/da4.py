from scipy.stats.stats import pearsonr  
import statistics
import pandas
import numpy

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

liking = []
salt = []
sweet = []
acid = []
crunch = []  


dx = pandas.read_excel('SNACKS.xls', sheet='Sheet1')

for i in range(0,len(dx)):
    liking_val=dx['Liking scores'][i]
    salt_val=dx['Saltiness'][i]
    sweet_val=dx['Sweetness'][i]
    acid_val=dx['Acidity'][i]
    crunch_val=dx['Crunchiness'][i]

    liking.append(liking_val)
    salt.append(salt_val)
    sweet.append(sweet_val)
    acid.append(acid_val)
    crunch.append(crunch_val)

print("correaltion matrix")	
print numpy.corrcoef([liking,salt,sweet,acid,crunch])

print("Coefficient of determination")
print "liking score-salt" 
print polyfit(liking,salt,3)
print""

print "liking score-sweet" 
print polyfit(liking,sweet,3)
print""
print "liking score-acid" 
print polyfit(liking,acid,3)
print""
print "liking score-crunch" 
print polyfit(liking,crunch,3)