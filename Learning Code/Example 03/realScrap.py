from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    when = soup.find('span', class_='sim-posted').text
    if 'few' in when:
        company_name = soup.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills = soup.find('span', class_='srp-skills').text.replace(' ', '')

        print(f'''
        Company Name: {company_name}
        Skills Required: {skills}
        Posted: {when}
        ''')

        print('-'*20)