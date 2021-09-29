from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')

url1 = 'https://www.upwork.com/search/profiles/?q=python'

file = open("Upwork-Python.csv", "w", encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Sr. no.", "Freelancer Name", "Profession", "Location", "Rate", "Earned", "Job Success", "Description"])

def getInfo(url):
    driver.get(url)
    # driver.get(url2)

    mainDiv = driver.find_element_by_class_name('mt-md-0')
    items = mainDiv.find_elements_by_class_name('up-card-section')
    try:
        for i, item in enumerate(items):
            i = i + 1
            try:
                person_name = item.find_element_by_class_name('identity-name').text
            except:
                person_name = "None"
            profession = item.find_element(by=By.CLASS_NAME, value='freelancer-title').text
            location = item.find_element(by=By.CLASS_NAME, value='vertical-align-middle').text
            r = item.find_element_by_class_name('profile-stats')
            rate = r.find_element(by=By.TAG_NAME, value='strong').text+'/hr'
            try:
                e = item.find_element(by=By.CLASS_NAME, value='grid-col-2')
                earned = e.find_element_by_tag_name('p').text
            except:
                earned = "None"
            try:
                success = item.find_element_by_class_name('up-job-success-text').text.split(' ')[0]
            except:
                success = "None"
            description = item.find_element(by=By.CLASS_NAME, value='clamped').text

            writer.writerow([i, person_name, profession, location, rate, earned, success, description])

    finally:
        driver.close()

getInfo(url1)

file.close()