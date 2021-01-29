from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text

soup = BeautifulSoup(source, 'lxml')
#print(soup)


tbody = soup.find('tbody', class_='lister-list')
tr= tbody.find_all('tr')

for i in tr :
    title = i.find('td', class_='titleColumn').text
    print(title)