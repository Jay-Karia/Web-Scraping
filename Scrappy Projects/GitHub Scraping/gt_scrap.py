from bs4 import BeautifulSoup
import requests
import xlsxwriter


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

try:
    repos = soup.find('div', id='user-repositories-list')

    repo = repos.find_all(itemprop='name codeRepository')

    lang = repos.find_all(itemprop='programmingLanguage')

    update = repos.find_all('relative-time', class_='no-wrap')

    stars = repos.find_all('a', class_='mr-3')

    visibility = repos.find_all('span', class_='Label')

    description = repos.find_all('p', class_='col-9 d-inline-block color-text-secondary mb-2 pr-4') 
except:
    print("\nAn error ocurred while retriving the data. Sorry!")

# Writing into excel file