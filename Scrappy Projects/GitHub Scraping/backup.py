from bs4 import BeautifulSoup
import requests
import csv


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

repo = soup.find(class_='user-repositories-list')
repo_list = soup.find_all(class_='col-12 d-flex width-full py-4 border-bottom color-border-secondary private source')

# file = open(f'{person_name}-info.csv', 'w')
# writer = csv.writer(file)

# writer.writerow(["Username", "Repo Name", "Repo URL", "Language", "Last Updated", "Stars", "Visibility", "Description"])

# try:
for repo in repo_list:
    print(len(repo))
    repo_name = repo.find('a', itemprop='name codeRepository')
    name = repo_name.get_text().strip()
    repo_url = repo.find('a', itemprop='name codeRepository')['href']
    url = f'https://github.com//{repo_url}'
    u = repo.find('relative-time', class_='no-wrap')
    update = u.get_text().strip()
    v = repo.find('span', class_='Label')
    visibility = v.get_text().strip()
    print()
    print(name)
    print(url)
    print(update)
    print(visibility)
    try:
        language = repo.find(itemprop='programmingLanguage')
        lang = language.get_text().strip()
        print(lang)
    except:
        print("None")

    try:
        s = repo.find('a', class_='Link--muted mr-3')
        stars = s.get_text().strip()[0]
        print(stars)
    except:
        print("0")

    try:
        d = repo.find('p', class_='col-9 d-inline-block color-text-secondary mb-2 pr-4')
        description = d.get_text().strip()
        print(description)
    except:
        print("None")

    # writer.writerow([person_name.encode('utf-8'), repo_name.encode('utf-8'), url.encode('utf-8'), lang.encode('utf-8'), update.encode('utf-8'), stars.encode('utf-8'), visibility.encode('utf-8'), description.encode('utf-8')])
# except:
#     print("\nAn error ocurred while retriving the data. Sorry!")

# file.close()