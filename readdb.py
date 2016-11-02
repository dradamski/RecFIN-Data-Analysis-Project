import sqlite3
import re
conn = sqlite3.connect('sitedb.sqlite')
cur = conn.cursor()

cur.execute('''UPDATE Data set 'site_id' = NULL''')
cur.execute('''SELECT * FROM Sites''')
results = [cur.fetchall()]
print results
for row in results[0]:
	site = row[1]
	id = row[0]
	print '...'
	
	
	cur.execute('''
				UPDATE Data SET site_id = (?) WHERE site = (?) ''', (id, site)) 
				 
conn.commit()
cur.close()