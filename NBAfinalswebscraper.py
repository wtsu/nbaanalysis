import urllib2 # library needed to get url

wiki = "https://en.wikipedia.org/wiki/NBA_Finals_television_ratings"

page = urllib2.urlopen(wiki)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page, "html.parser")

n = 0

#print soup.prettify()

#soup.a

#soup.find_all("a")

#all_links = soup.find_all('a')
#print all_links
#for x in all_links:
#	print x
#	n = n + 1
#	print n

right_table = soup.find('table', class_= 'wikitable sortable')
#print right_table.prettify()
#print right_table
#print all_tables

A=[]
B=[]
C=[]
D=[]

for rows in right_table.findAll('tr'):
	cells = rows.findAll('td')
	#print cells
	games = rows.findAll('th')
	#print games
	if len(cells) == 3:
		A.append(cells[0].find(text=True))
		B.append(cells[1].find(text=True))
		C.append(cells[2].find(text=True))
		D.append(games[0].find(text=True))
import pandas as pd

df=pd.DataFrame(A,columns=['Years'])
df['Network']=B
df['Results']=C
df['Avg']=D
df.to_csv("Ratings.csv", sep=',', encoding='utf-8')
