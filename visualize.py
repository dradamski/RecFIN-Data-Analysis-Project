# select Ventura Pier and show catch, anglers or Catch Per Unit Effort CPUE,
# Graph CPUE

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()

# this allows for customization of which site i want  to look at
stuff = cur.execute('''
			SELECT * FROM Data WHERE site = 'Ventura Pier' ORDER BY date''')

date_dict = dict()
total_catch = dict()
for line in stuff:
	# helps me know how to call each datatype
	id = line[0]
	site = line[1]
	species = line[2]
	year = line[3]
	month = line[4]
	date = str(line[5])
	angs = line[6]
	number = line[7]
	std = line[8]
	
	if date not in date_dict:
		date_dict[date] = list()
		date_dict[date].append({'anglers': angs})
		total_catch[date] =  list()
	
	date_dict[date].append({species: number})
	total_catch[date].append(number)

catch_by_date = dict()
for date in total_catch:
	catch_by_date[date] = sum(total_catch[date])
sort_dates = sorted(catch_by_date)

tots = []
cpue =[]


for i in sort_dates:
	tots.append(int(catch_by_date[i]))
	cpue.append(float(catch_by_date[i])/date_dict[i][0]['anglers'])



########################################################################
# for i in range 1980-2016:											   #
#	for j in range 1-12												   #
#		list of every date w/ or w/o data.append(str(i) + '-' + str(j))#
########################################################################
# year_date = []													   #
# for i in range(1980, 2017):										   #
#	for j in range(12):												   #
#		year_date.append(str(i) + '-' + str(j + 1).zfill(2) + '-01')   #
########################################################################		
plt.figure(1)
plt.subplot(211)
x = range(len(sort_dates))
plt.xticks(x, sort_dates, rotation = 70)
plt.plot(x, cpue)
plt.locator_params(nbins=10)
plt.xlabel('Month')
plt.ylabel('CPUE')
plt.title('CPUE at Ventura Pier 2000-2010')
#plt.show()


#Graphing
plt.subplot(212)
x = range(len(sort_dates))
plt.xticks(x, sort_dates, rotation = 70)
plt.plot(x, tots)
plt.locator_params(nbins=12)
plt.xlabel('Month')
plt.ylabel('Total Individuals Caught')
plt.title('Total Catch at Ventura Pier 2000-2010')
plt.show()

