from bs4 import BeautifulSoup
import requests
import csv

url = 'https://weather.com/en-IN/weather/tenday/l/efdc1f9159c1023991dbc88aa4fd4592aa13eec53c0937a0e793693ac7bb82c3#detailIndex5'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

mainDiv = soup.find('div', class_='DailyForecast--DisclosureList--msYIJ')
Lists = mainDiv.find_all('details', class_='Disclosure--themeList--25Q0H')

file = open("Weather-forecast.csv", "w")
csvWriter = csv.writer(file)

csvWriter.writerow(["Day", "Max Temp", "Min Temp", "Weather", "Rain %", "Wind Speed"])

def getInfo():
    for items in Lists:
        day = items.find('h2', class_='DetailsSummary--daypartName--2FBp2').get_text().strip()
        maxTemp = items.find('span', class_='DetailsSummary--highTempValue--3Oteu').get_text().strip()
        minTemp = items.find('span', class_='DetailsSummary--lowTempValue--3H-7I').get_text().strip()
        weather = items.find('div', class_='DetailsSummary--condition--24gQw').span.get_text().strip()
        rainPer = items.find('div', class_='DetailsSummary--precip--1ecIJ').span.get_text().strip()
        wind = items.find('span', class_='Wind--windWrapper--3aqXJ undefined').get_text().strip().split(" ")[1]+" km\h"

        csvWriter.writerow([day, maxTemp, minTemp, weather, rainPer, wind])

getInfo()
file.close()