from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe')

driver.get('http:/demo.automationtesting.in/Windows.html')

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

# driver.close()
driver.quit()