from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
driver.get('https://www.w3.org/TR/wai-aria-practices-1.1/examples/checkbox/checkbox-1/checkbox-1.html')

mustard = driver.find_element_by_xpath('//*[@id="ex1"]/div/ul/li[3]/div')
mustard.click()

sleep(2)

driver.close()