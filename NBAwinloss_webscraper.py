import urllib2 # library needed to get url

wiki = "http://www.basketball-reference.com/leagues/NBA_1983.html"

page = urllib2.urlopen(wiki)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "html.parser")
#soup=soup.encode('utf-8')
all_tables=soup.find_all('tbody')
east_table=soup.find('table', id="divs_standings_E")
west_table=soup.find('table', id="divs_standings_W")
#right_table=soup.find('table)
#print all_tables
#print right_table

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]
for rows in east_table.findAll("tr"):
	name = rows.findAll("th")
	cells = rows.findAll("td")
	if len(cells)==7:
		A.append(name[0].find(text=True))
		B.append(cells[0].find(text=True))
		C.append(cells[1].find(text=True))
		D.append(cells[2].find(text=True))
		E.append(cells[3].find(text=True))
		F.append(cells[4].find(text=True))
		G.append(cells[5].find(text=True))
		H.append(cells[6].find(text=True))
		
for rows in west_table.findAll("tr"):
	name = rows.findAll("th")
	cells = rows.findAll("td")
	if len(cells)==7:
		A.append(name[0].find(text=True))
		B.append(cells[0].find(text=True))
		C.append(cells[1].find(text=True))
		D.append(cells[2].find(text=True))
		E.append(cells[3].find(text=True))
		F.append(cells[4].find(text=True))
		G.append(cells[5].find(text=True))
		H.append(cells[6].find(text=True))
		
import pandas as pd
df1=pd.DataFrame(A, columns = ['Team'])
df1['wins']=B
df1['losses']=C
df1['win_loss_pct']=D
df1['gb']=E
df1['pts_per_g']=F
df1['opp_pts_per_g'] =G
df1['srs'] = H
df1.to_csv("1983_Record.csv", sep=',', encoding='utf-8')


# A1=[]
# B2=[]
# C3=[]
# D4=[]
# E5=[]
# F6=[]
# G7=[]
# H8=[]
# for rows in west_table.findAll("tr"):
	# name = rows.findAll("th")
	# cells = rows.findAll("td")
	# if len(cells)==7:
		# A1.append(name[0].find(text=True))
		# B2.append(cells[0].find(text=True))
		# C3.append(cells[1].find(text=True))
		# D4.append(cells[2].find(text=True))
		# E5.append(cells[3].find(text=True))
		# F6.append(cells[4].find(text=True))
		# G7.append(cells[5].find(text=True))
		# H8.append(cells[6].find(text=True))

# df2=pd.DataFrame(A1, columns = ['Team'])
# df2['wins']=B2
# df2['losses']=C3
# df2['win_loss_pct']=D4
# df2['gb']=E5
# df2['pts_per_g']=F6
# df2['opp_pts_per_g'] =G7
# df2['srs'] = H8
# df2.to_csv("2017_West_Record.txt", sep=',', encoding='utf-8')