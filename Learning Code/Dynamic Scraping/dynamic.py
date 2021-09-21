from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe')

driver.get('http:/newtours.demoaut.com/')

print(driver.title) # Title of the page

print(driver.current_url) # Returns the URL of the Page

print(driver.page_source) # HTML code for the page

driver.close() # Close the browser