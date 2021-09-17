from bs4 import BeautifulSoup
import requests
import csv


def DailyForecast():
    try:
        url = 'https://weather.com/en-IN/weather/tenday/l/efdc1f9159c1023991dbc88aa4fd4592aa13eec53c0937a0e793693ac7bb82c3#detailIndex5'
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        mainDiv = soup.find('div', class_='DailyForecast--DisclosureList--msYIJ')
        Lists = mainDiv.find_all('details', class_='Disclosure--themeList--25Q0H')

        file = open("Daily-forecast.csv", "w")
        csvWriter = csv.writer(file)

        csvWriter.writerow(["Sr no.", "Day", "Max Temp", "Min Temp", "Weather", "Rain %", "Wind Speed"])
        for index,items in enumerate(Lists):

            index = index + 1

            day = items.find('h2', class_='DetailsSummary--daypartName--2FBp2').get_text().strip()
            maxTemp = items.find('span', class_='DetailsSummary--highTempValue--3Oteu').get_text().strip()
            minTemp = items.find('span', class_='DetailsSummary--lowTempValue--3H-7I').get_text().strip()
            weather = items.find('div', class_='DetailsSummary--condition--24gQw').span.get_text().strip()
            rainPer = items.find('div', class_='DetailsSummary--precip--1ecIJ').span.get_text().strip()
            wind = items.find('span', class_='Wind--windWrapper--3aqXJ undefined').get_text().strip().split(" ")[1]+" km\h"

            csvWriter.writerow([index, day, maxTemp, minTemp, weather, rainPer, wind])

        file.close()

        print("File saved Successfully!!")
    except:
        print("An Unexpected Error occurred, Sorry!")

def HourlyForecast():
    url = 'https://weather.com/en-IN/weather/hourbyhour/l/efdc1f9159c1023991dbc88aa4fd4592aa13eec53c0937a0e793693ac7bb82c3'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    mainDiv = soup.find('div', class_='HourlyForecast--DisclosureList--3CdxR')
    Lists = mainDiv.find_all('details', class_='DaypartDetails--DayPartDetail--1up3g Disclosure--themeList--25Q0H')

    for index,items in enumerate(Lists):
        time = t.find('h2', class_='DetailsSummary--daypartName--2FBp2').get_text().strip()
        print(time)

HourlyForecast()
