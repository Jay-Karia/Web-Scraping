from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver_win32 (2)\chromedriver.exe')

print("Enter the language to get specific products")
# languages = ["C/C++", "C#", "Dart", "DSL", "F#", "Go", "Groovy", "HTML", "Java", "JavaScript, TypeScript", "Kotlin", "Objective-C", "PHP", "Python", "R", "Ruby", "Rust", "Scala", "SQL", "Swift", "VB.NET"]
# lang = input()
lang = ""
url = 'https://www.jetbrains.com/products/'

driver.get(url)

mainDiv = driver.find_element_by_xpath('//*[@id="products-page"]/div/div[1]/div[1]')
items = mainDiv.find_element_by_xpath('//*[@id="products-page"]/div/div[1]/div[1]/div')

for item in items:
    pass