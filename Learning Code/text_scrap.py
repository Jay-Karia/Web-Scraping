from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(html, 'html.parser')
content = soup.find('div', {'id': 'mw-content-text'}).get_text().strip()
# content = bytes(content, 'UTF-8')
content = content.encode('UTF-8')
content = content.decode('UTF-8')

print(content)