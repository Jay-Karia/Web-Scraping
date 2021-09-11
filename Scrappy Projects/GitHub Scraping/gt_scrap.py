from bs4 import BeautifulSoup
import requests
import csv


print("Enter the name of the person on GitHub")
person_name = input()

link = f'https://github.com/{person_name}?tab=repositories'
print(link)
html = requests.get(link).text
soup = BeautifulSoup(html, 'html.parser')

# file = open(f'{person_name}-info.csv', 'a')
# csvWriter = csv.writer(file)

# csvWriter.writerow(["Sr No.", "Repo Name"])

def get_repo_name(soup):
    try:
        repo = soup.find_all('a', itemprop='name codeRepository')
        print()
        for index, repo in enumerate(repo):
            index = index + 1
            repository = repo.get_text().strip()
            csvWriter.writerow([index, repository])
        print("File Saved Successfully!")
    except:
        print("An unexpected Error Occurred, Sorry!")

def get_repo_url(soup):
    repo_url = soup.find_all('a', itemprop='name codeRepository')['href']
    print()
    for index, url in enumerate(repo_url):
        index = index + 1
        print(url['href'])

# get_repo_name(soup)
get_repo_url(soup)

# file.close()