from selenium import webdriver

PATH = r'C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
# Navigating and Clicking Buttons

link = driver.find_element_by_link_text("Python Programming")
link.click()
link2 = driver.find_element_by_link_text("Beginner Python Tutorials")
link2.click()
link3 = driver.find_element_by_id('sow-button-19310003')
link3.click()

driver.back()
driver.back()
driver.back()
driver.forward()

driver.quit()