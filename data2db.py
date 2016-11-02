# goes through data file and create data sqlite database

import sqlite3
import csv
# opens up csv file
with open('80-16.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile)
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
	for row in spamreader:
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
                