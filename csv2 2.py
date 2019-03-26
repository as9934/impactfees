import urllib.request
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.request.urlopen("https://www.townofchapelhill.org/town-hall/departments-services/planning-and-sustainability/gis-analytics/development-activity-report").read(), 'lxml')

tbody = soup('table', {"class":"tableData tablesorter tablesorter-blue hasFilters hasStickyHeaders"}) [0].find_all('tr')
for row in tbody: 
	cols = row.findChildren(recursive=False)
	print(cols)
	