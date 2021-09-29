from selenium import webdriver
import csv

print("Enter your language")
language = input()
lang = language.lower()

if lang == 'c++' or lang == 'csharp' or lang == 'c#' or lang == 'c' or lang == 'c sharp':
    lang = 'cpp'

if 'javascript' in lang or 'typescript' in lang:
    lang = 'js'

if 'objective-c' in lang:
    lang = 'objc'

if 'vb.net' in lang:
    lang = 'vbnet'

if lang == 'r':
    lang = 'r-lang'

if lang == 'f#' or lang == 'f sharp':
    lang = 'fsharp'

if lang == 'php':
    lang = 'php-lang'

url = f'https://www.jetbrains.com/products/#lang={lang}'
print(f"\n{url}")

driver = webdriver.Chrome(executable_path='C:\\Programming\\Chrome WebDriver\\app\\chromedriver')
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

    print("\nFile Saved Successfully!!!")
except:
    print("\nAn error occurred, Sorry!")

finally:
    driver.close()

file.close()