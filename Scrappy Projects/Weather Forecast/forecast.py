# Importing Modules
from bs4 import BeautifulSoup
import requests
import csv

# Getting the Page
url = 'https://weather.com/en-IN/weather/tenday/l/67856cfb73906043597e1db40eb79b4354db97fe544f648abaa7cf6b9dcebdc1#detailIndex5'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

# Getting current information
def getCurrent(soup):
    '''
    Call this method to get the current information
    '''
    currentDay = soup.find('span', class_='DailyContent--daypartDate--2A3Wi').get_text().strip()
    currentTemperature = soup.find('span', class_='DailyContent--temp--3d4dn').get_text().strip()
    currentWeather = soup.find('div', class_='DailyContent--Condition--bQKA2').get_text().strip().title()
    currentHumidity = soup.find('span', class_='DetailsTable--value--1q_qD').get_text().strip()
    currentMaxTemp = soup.find('span', class_='DetailsSummary--highTempValue--3Oteu').get_text().strip()
    currentMinTemp = soup.find('span', class_='DetailsSummary--lowTempValue--3H-7I').get_text().strip()
    currentWind = soup.find('span', class_='Wind--windWrapper--3aqXJ DailyContent--value--37sk2').get_text().strip().split('SSW')[1]

getCurrent(soup)
