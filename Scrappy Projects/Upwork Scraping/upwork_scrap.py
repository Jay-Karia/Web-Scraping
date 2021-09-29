from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')

url1 = 'https://www.upwork.com/search/profiles/?q=python'
url2 = 'https://www.upwork.com/search/profiles/?page=2&q=python'

i = 0

def getInfo(url):
    global i
    driver.get(url)

    mainDiv = driver.find_element_by_class_name('mt-md-0')
    items = mainDiv.find_elements_by_class_name('up-card-section')
    try:
        for i, item in enumerate(items):
            i = i + 1
            person_name = item.find_element_by_class_name('identity-name').text
            profession = item.find_element(by=By.CLASS_NAME, value='freelancer-title').text
            location = item.find_element(by=By.CLASS_NAME, value='vertical-align-middle').text
            r = item.find_element_by_class_name('profile-stats')
            rate = r.find_element(by=By.TAG_NAME, value='strong').text+'/hr'
            try:
                e = item.find_element(by=By.CLASS_NAME, value='grid-col-2')
                earned = e.find_element_by_tag_name('p').text
            except:
                earned = "None"
            success = item.find_element_by_class_name('up-job-success-text').text.split(' ')[0]
            description = item.find_element(by=By.CLASS_NAME, value='clamped').text

            print(i)

    finally:
        driver.close()

getInfo(url1)
getInfo(url2)