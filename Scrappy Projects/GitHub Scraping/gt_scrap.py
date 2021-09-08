from bs4 import BeautifulSoup
import requests

link = 'https://github.com/Jay-Karia?tab=repositories'
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

repos = soup.find('div', id='user-repositories-list')

# for repo in repos.find_all(itemprop='name codeRepository'):
#     print(repo.get_text().replace(' ', ''))

# for lang in repos.find_all(itemprop='programmingLanguage'):
#     print(lang.get_text().replace(' ', ''))

# for update in repos.find_all('relative-time', class_='no-wrap'):
#     print(update.get_text().replace(' ', ''))

for stars in repos.find_all('a', class_='mr-3'):
    if stars == '\n\n\n\n':
        stars = 0
    print(stars.get_text().replace(' ', ''))

# visibility = repos.find_all()