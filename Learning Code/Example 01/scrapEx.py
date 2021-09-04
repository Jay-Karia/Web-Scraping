from bs4 import  BeautifulSoup
import requests

with open('Example 01\\index.html') as html:
    soup = BeautifulSoup(html, 'lxml')

for article in soup.find_all('div', {'class': 'article'}):
    headline = article.h2.a.text
    print(headline)
    summary = article.p.text
    print(summary)

    print()