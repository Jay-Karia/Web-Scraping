from bs4 import BeautifulSoup
import requests
import csv


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

file = open(f'{person_name}-info.csv', 'w')
writer = csv.writer(file)

writer.writerow(["Username", "Repo Name", "Repo URL", "Language", "Last Updated", "Stars", "Visibility", "Description"])

try:
    for repos in soup.find_all('div', id='user-repositories-list'):

        repo_name = repos.find(itemprop='name codeRepository')

        repo_url = repos.find('a', itemprop='name codeRepository')['href']
        url = f'https://github.com//{repo_url}'

        lang = repos.find(itemprop='programmingLanguage')

        update = repos.find('relative-time', class_='no-wrap')

        stars = repos.find('a', class_='mr-3')

        visibility = repos.find('span', class_='Label')

        description = repos.find('p', class_='col-9 d-inline-block color-text-secondary mb-2 pr-4')

        writer.writerow([person_name, name, url, lang, update, stars, visibility, description])
except:
    print("\nAn error ocurred while retriving the data. Sorry!")

file.close()