import sqlite3
import re
import csv

# GETS ALL SITE IDS
# opens site list
file = open('SEC Route List.txt').readlines()[0].split('\r')

site_dic = {}

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

		site_dic[id] = st


# creates site table in database
conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()

# deletes Sites table if it already exists 
cur.execute('''
DROP TABLE IF EXISTS Sites''')

cur.execute('''
CREATE TABLE Sites (id INTEGER, name TEXT)''')

for key, value in  site_dic.iteritems():
    cur.execute('''INSERT INTO Sites (id, name) 
                VALUES ( ?, ? )''', ( key, value ) )
   
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()


cur.close()


# ADDS DATA TO DATABASE IN Data TABLE

with open('80-16.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	# opens connection to sqlite database
	conn = sqlite3.connect('sitedb.sqlite')
	cur = conn.cursor()
	# gets rid of any existing tables named Data so I don't have a bunch of tables
	cur.execute('''
			DROP TABLE IF EXISTS Data''')
	
	cur.execute('''
				CREATE TABLE Data (site_id INTEGER, site TEXT, species TEXT, year INTEGER,
				 month INTEGER, date INTEGER, anglers INTEGER, catch REAL, stderr REAL)''')	
	# reads through csv for data that i want
	for row in reader:
		species = row['COMMON']
		year = row['YEAR']
		month = row['month'].zfill(2)
		date = year + '-' + month + '-01'
		catch = row['ab1ns']
		stderr = row['ab1ndse']
		anglers = row['angs']
		site = row['name']
		
		# exceptions to make names match sqlite db
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
			
		cur.execute('''INSERT INTO Data (site, species, year, month, date, anglers, catch, stderr) 
                VALUES ( ?, ? , ? , ? , ? , ?, ?, ?)''', ( site, species, year, month, date, anglers, catch, stderr ) )
	conn.commit()

cur.close()



# DOES FINAL CLEAN UP BY COMBINING DIFFERENT NAMES FOR SAME SITE
conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()

cur.execute('''UPDATE Data set 'site_id' = NULL''')
cur.execute('''SELECT * FROM Sites''')
results = [cur.fetchall()]
for row in results[0]:
	site = row[1]
	id = row[0]
	
	
	
	cur.execute('''
				UPDATE Data SET site_id = (?) WHERE site = (?) ''', (id, site)) 
# made executive decision to set Ventura Marina Harbor equal to Ventura Harbor BB
cur.execute('''UPDATE Data SET site_id = 2103 WHERE site = "Ventura Marina Harbor"
			''')
# executive decision to set Ormond Beach Pier equal to Hueneme Pier
cur.execute('''UPDATE Data SET site_id = 1001 WHERE site = "Ormond Beach Pier"
			''')
			
						 
conn.commit()
cur.close()
