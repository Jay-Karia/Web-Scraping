from bs4 import BeautifulSoup
import requests
import time

print('Put some skills you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering Out {unfamiliar_skills}')

def find_jobs():
    html = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        when = job.find('span', class_='sim-posted').text
        if 'few' in when:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            link = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'{index}.txt', 'w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Required Skills: {skills.strip()}\n")
                    f.write(f"More Info: {link}")
                print(f'File save: {index}')

if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"\nWaiting {time_wait} minutes...\n")
        time.sleep(time_wait * 60)
        print()