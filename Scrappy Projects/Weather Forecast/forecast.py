# Importing Modules
from bs4 import BeautifulSoup
import requests
import csv

# Getting the Page
url = 'https://www.weather-forecast.com/locations/Rajkot/forecasts/latest'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

# Getting the information
day = soup.findAll('div', class_='b-forecast__table-days-name')
date = soup.findAll('div', class_='b-forecast__table-days-date')

for items in range(12):
    print(date[items].text)