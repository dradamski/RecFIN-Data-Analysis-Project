# used to find differences in site names between SEC site list and CSV data

import re
import csv

file = open('SEC Route List.txt').readlines()[0].split('\r')

site_dic = []

# puts sites in sites list and creates id for each to go in id list
for line in file:
	site = re.findall('(^.+) \((M{2}|B{2})\)-111\/([0-9]+)', line)
	if len(site) == 1:
		st = site[0][0]		
		if re.search('^\t', st):
			st = st.replace('\t', '')
	
		if site[0][1] == 'BB':	
			id = 2000 + int(site[0][2])
		elif site[0][1] == 'MM':
			id = 1000 + int(site[0][2])

		site_dic.append(st)



site_names = []
with open('00-102.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
	
	for row in spamreader:
		species = row['COMMON']
		year = row['YEAR']	
		month = row['month']
		catch = row['ab1ns']
		anglers = row['angs']
		site = row['name']
		
# exceptions to match sql 
		if site == 'Rincon':
			site = site + ' Beaches'
		if site == 'Solimar':
			site = site + ' Beach'
		if 'Big Sycamore' in site:
			site = 'Big Sycamore Beach'
		if 'County' in site:
			site = 'County Line'
		if 'Small' in site:
			site = site + ' (7)'
		site_names.append(site)

	
names = []
for site in site_names:
	if site in names:
		continue
	else:
		if site not in site_dic:
			names.append(site)
			
print names
