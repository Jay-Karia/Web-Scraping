from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://www.upwork.com/search/profiles/?q=python'
driver.get(url)

mainDiv = driver.find_element_by_class_name('mt-md-0')
items = mainDiv.find_elements_by_class_name('up-card-section')

try:
    for item in items:
        # index = index + 1
        person_name = item.find_element_by_class_name('identity-name').text
        print(person_name)

finally:
    driver.close()