from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://www.upwork.com/search/profiles/?q=python'
driver.get(url)

mainDiv = driver.find_element_by_class_name('mt-md-0')
items = mainDiv.find_elements_by_class_name('up-card-section')

try:
    for item in items:
        # index = index + 1
        person_name = item.find_element_by_class_name('identity-name').text
        profession = item.find_element(by=By.CLASS_NAME, value='freelancer-title').text
        location = item.find_element(by=By.CLASS_NAME, value='vertical-align-middle').text
        r = item.find_element_by_class_name('profile-stats')
        rate = item.find_element(by=By.TAG_NAME, value='strong').text+'/hr'
        print(rate)

finally:
    driver.close()