from bs4 import BeautifulSoup
import requests
import csv


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

file = open(f'{person_name}-info.csv', 'w', encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Sr no.", "Developer Name", "Repo Name", "Repo URL", "Language", "Last Updated", "Stars", "Visibility", "Description"])

try:
    userRepoDiv = soup.find('div', id='user-repositories-list')
    userRepoList = userRepoDiv.find_all('li', class_='col-12 d-flex width-full py-4 border-bottom color-border-secondary public source')

    for index, repo in enumerate(userRepoList):
        index = index + 1
        name = repo.find('a', itemprop='name codeRepository')
        repo_name = name.get_text().strip()
        repo_url = repo.find('a', itemprop='name codeRepository')['href']
        url = f'https://github.com//{repo_url}'
        u = repo.find('relative-time', class_='no-wrap')
        update = u.get_text().strip()
        v = repo.find('span', class_='Label')
        visibility = v.get_text().strip()

        lang = None
        stars = None
        description = None
        try:
            language = repo.find(itemprop='programmingLanguage')
            lang = language.get_text().strip()
        except:
            lang = "None"

        try:
            s = repo.find('a', class_='Link--muted mr-3')
            stars = s.get_text().strip()[0]
        except:
            stars = "0"

        try:
            d = repo.find('p', class_='col-9 d-inline-block color-text-secondary mb-2 pr-4')
            description = d.get_text().strip()
        except:
            description = "None"

        writeP = [index, person_name, repo_name, url, lang, update, stars, visibility, description]

        writer.writerow(writeP)


    print("\nFile Successfully Saved!!")
except:
    print("\nAn error occurred while retrieving the data. Sorry!")

file.close()