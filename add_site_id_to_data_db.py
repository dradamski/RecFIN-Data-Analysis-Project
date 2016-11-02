import sqlite3
import re
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