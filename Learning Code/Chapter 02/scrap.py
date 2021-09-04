from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html.read(), 'html.parser')

nameList = soup.findAll('span', {'class': 'green'})
for  name in nameList:
    print(name.get_text())