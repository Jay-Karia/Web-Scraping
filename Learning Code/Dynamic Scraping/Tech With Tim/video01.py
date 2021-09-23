from selenium import webdriver

PATH = r"C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https:/techwithtim.net')
print(driver.title)
driver.close()