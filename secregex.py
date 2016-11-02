# Used to get site names and ids from SEC Route List file

import re

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
print site_dic

