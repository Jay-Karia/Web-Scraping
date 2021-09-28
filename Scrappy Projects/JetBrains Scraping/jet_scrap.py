from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://www.jetbrains.com/products/'
driver.get(url)

mainDiv = driver.find_element_by_xpath('//*[@id="products-page"]/div/div[1]/div[1]')
items = mainDiv.find_elements_by_tag_name('div')

try:
    print(mainDiv.text)
finally:
    driver.close()