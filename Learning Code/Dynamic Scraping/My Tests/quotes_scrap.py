from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
url = 'https://quotes.toscrape.com/'
driver.get(url)

file = open('quotes.csv', 'w')
writer = csv.writer(file)

writer.writerow(["Sr. no.", "Quote", "Author"])

try:
	items = driver.find_elements_by_class_name('quote')

	for index, item in enumerate(items):
		index += 1
		quote = item.find_element_by_class_name('text').text
		author = item.find_element_by_class_name('author').text
		writer.writerow([index, quote, author])
finally:
	driver.close()

file.close()