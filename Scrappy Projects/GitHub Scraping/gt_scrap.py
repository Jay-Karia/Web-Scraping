from bs4 import BeautifulSoup
import requests
import csv


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

# file = open(f'{person_name}-info.csv', 'w')
# writer = csv.writer(file)

# writer.writerow(["Username", "Repo Name", "Repo URL", "Language", "Last Updated", "Stars", "Visibility", "Description"])

# try:
for repos in soup.find_all('div', id="user-repositories-list"):

    repo_name = repos.find('a', itemprop='name codeRepository')
    name = repo_name.get_text().strip()
    repo_url = repos.find('a', itemprop='name codeRepository')['href']
    url = f'https://github.com//{repo_url}'
    u = repos.find('relative-time', class_='no-wrap')
    update = u.get_text().strip()
    v = repos.find('span', class_='Label')
    visibility = v.get_text().strip()
    print()
    print(name)
    print(url)
    print(update)
    print(visibility)
    try:
        language = repos.find(itemprop='programmingLanguage')
        lang = language.get_text().strip()
        print(lang)
    except AttributeError:
        print("None")

    try:
        s = repos.find('a', class_='Link--muted mr-3')
        stars = s.get_text().strip()
        print(stars)
    except:
        print("None")

    try:
        d = repos.find('p', class_='col-9 d-inline-block color-text-secondary mb-2 pr-4')
        description = d.get_text().strip()
        print(description)
    except:
        print("None")

    # writer.writerow([person_name.encode('utf-8'), repo_name.encode('utf-8'), url.encode('utf-8'), lang.encode('utf-8'), update.encode('utf-8'), stars.encode('utf-8'), visibility.encode('utf-8'), description.encode('utf-8')])
# except:
#     print("\nAn error ocurred while retriving the data. Sorry!")

# file.close()