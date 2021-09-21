from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe')

driver.get('http:/www.newtours.demout.com/')
time.sleep(5)
print(driver.title)

driver.get('http:/www.pavantestingtools.blogpost.in/')
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)