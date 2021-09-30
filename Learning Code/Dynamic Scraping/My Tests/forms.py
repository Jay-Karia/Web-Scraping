from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
# Filling the forms
url = 'https://www.w3schools.com/html/html_forms.asp'
driver.get(url)

name_field = driver.find_element_by_id('fname')
lastName_field = driver.find_element_by_id('lname')

name_field.clear()
name_field.send_keys("Jay")
time.sleep(2)
lastName_field.clear()
lastName_field.send_keys("Karia")
time.sleep(2)

submit_btn = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/form/input[3]')
submit_btn.click()

time.sleep(2)

driver.close()