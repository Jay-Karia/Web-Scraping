from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r'C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techwithtim.net')
# Getting the search results from the search bar of the website

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.ENTER)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements_by_tag_name("articles")
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)

finally:
    driver.quit()