#compiles with python 2.7

import urllib
import re 
import os
import json 

#listed components of the dow 30
s = open('dow_30.txt').read()
symbolList = s.split('\n')
x = 1

if not os.path.exists('dow_prices/'):
	os.makedirs('dow_prices/')

for symbol in symbolList:

	htmlText = urllib.urlopen('http://www.bloomberg.com/markets/chart/data/1D/' + symbol + ':US')
	data = json.load(htmlText)
	dataPoints = data['data_values']

	file = open('dow_prices/' + symbol + '.csv', 'a')

	for point in dataPoints:
		print symbol, point[0], point[1]
		file.write(str(point[1])+","+str(point[0])+'\n')

	if x is 30:
		print 'successfully downloaded... check the \'dow_prices\' folder'
	else:
		print "downloading files..."

	x = x + 1

	file.close()



