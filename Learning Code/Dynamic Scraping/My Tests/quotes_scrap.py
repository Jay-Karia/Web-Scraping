from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://quotes.toscrape.com/'
driver.get(url)

try:
	items = driver.find_elements_by_class_name('quote')

	for item in items:
		title = item.find_element_by_class_name('text').text
		author = item.find_element_by_class_name('author').text
finally:
	driver.close()