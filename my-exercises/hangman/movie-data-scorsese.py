# Using requests pandas etc.
import pandas as pd
import requests
website_url = requests.get("https://en.wikipedia.org/wiki/Martin_Scorsese_filmography").text

from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())

My_table = soup.find('table',{'class':'wikitable sortable'})
#print(My_table)

links = My_table.findAll('a')
print(links)

Movies = []
for link in links:
    Movies.append(link.get('title'))

print(Movies)
pd.DataFrame(Movies).to_clipboard(excel = False, header = False, index = False)