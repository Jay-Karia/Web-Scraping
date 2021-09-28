from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://www.jetbrains.com/products/'
driver.get(url)

mainDiv = driver.find_element_by_xpath('//*[@id="products-page"]/div/div[1]/div[1]')
items = mainDiv.find_elements_by_class_name('_wt-card_ru6f9_1')

try:
    for index, item in enumerate(items):
        index = index + 1
        product_name = item.find_element_by_class_name('wt-link_hardness_hard').text
        description = item.find_element_by_class_name('wt-offset-top-12').text
        version = item.find_element_by_class_name('wt-text-2_theme_light').text
        if '.' not in version:
            version = "None"
        url = item.find_element_by_class_name('wt-link_hardness_hard').get_attribute('href')
finally:
    driver.close()