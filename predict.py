import sqlite3
import matplotlib.pyplot as plt
from collections import OrderedDict
import numpy as np



# Connect to database
conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()



months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
			'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


avg_list = []
std_list = []
for i in range(1, 13, 1):	
	stuff = cur.execute('''
			SELECT * FROM Data WHERE month = ? ORDER BY date''', (str(i), ))
	# catch from each month
	month_catch = []
	for line in stuff:		
		month_catch.append(line[7])
	
	high = max(month_catch)
	
	month_catch = month_catch.remove(high)
	
	avg = np.mean(month_catch)
	std_dev = np.std(month_catch)
	
# list of avg ordered by month
	avg_list.append(avg)
# list of std deviations ordered by month
	std_list.append(std_dev)


# Graph of normal distribution of predictions
for i in range(len(avg_list)):
	mu = avg_list[i]
	sigma = std_list[i]

	s = np.random.normal(mu, sigma, 1000)


	count, bins, ignored = plt.hist(s, 30, normed=True)
	plt.title('Normal Distribution of Predicted Catch in %s' % months[i])
	plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * 
				np.exp( - (bins - mu)**2 / (2 * sigma**2) ), 
				linewidth=2, color='r')
	axes = plt.gca()
	axes.set_xlim(0,)
	plt.show()








#plt.figure(1)
#plt.bar(range(len(avg_catch)), avg_catch.values(), align='center')
#plt.xticks(range(len(avg_catch)), avg_catch.keys())
#plt.xlabel('Month')
#plt.ylabel('Average Catch')
#plt.title('Average Catch at Ventura County Shore Sites 2000-2010')
#plt.show()

