from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')

print("Enter your language")
language = input()
lang = language.lower()

if lang == 'c++' or lang == 'csharp' or lang == 'c#' or lang == 'c':
    lang = 'cpp'

if 'javascript' in lang or 'typescript' in lang:
    lang = 'js'

if 'objective-c' in lang:
    lang = 'obc'

if 'vb.net' in lang:
    lang = 'vbnet'

url = f'https://www.jetbrains.com/products/#lang={lang}'
print(url)
driver.get(url)

mainDiv = driver.find_element_by_xpath('//*[@id="products-page"]/div/div[1]/div[1]')
items = mainDiv.find_elements_by_class_name('_wt-card_ru6f9_1')

file = open("JetBrains-Info.csv", "w", encoding='utf-8')
writer = csv.writer(file)

writer.writerow(["Sr. no.", "Language", "Product Name", "Product URL", "Version", "Description"])

try:
    for index, item in enumerate(items):
        index = index + 1
        product_name = item.find_element_by_class_name('wt-link_hardness_hard').text
        description = item.find_element_by_class_name('wt-offset-top-12').text
        version = item.find_element_by_class_name('wt-text-2_theme_light').text
        if '.' not in version:
            version = "None"
        url = item.find_element_by_class_name('wt-link_hardness_hard').get_attribute('href')

        writer.writerow([index, language, product_name, url, version, description])

    print("File Saved Successfully!!!")
except:
    print("An error occurred, Sorry!")

finally:
    driver.close()

file.close()
