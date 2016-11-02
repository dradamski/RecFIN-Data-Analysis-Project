# makes Site sqlite database

import sqlite3
import re

# Gets all site IDs
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


	
	
	
	
	
# creates site database
conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()

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


# puts data into a database













