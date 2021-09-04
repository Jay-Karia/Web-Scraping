from urllib import request
from bs4 import BeautifulSoup
import requests

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')

article  = soup.find('article')
# print(article.prettify())

headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_='entry-content').p.text
# print(summary)

vid_source = article.find('iframe', class_='youtube-player')['src']
# print(vid_source)

vid_id = vid_source.split('/')[4]
vid_id = vid_id.split('?')[0]
print(vid_id)

# Time: 32:40