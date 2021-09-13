# importing required modules
from bs4 import BeautifulSoup
import requests
import csv

# Getting the product
print("Enter a product name")
product_name = input()

# Getting the page
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = f'https://www.amazon.in/s?k={product_name}&ref=nb_sb_noss_2'

source = requests.get(url, headers = headers).text
soup = BeautifulSoup(source, 'lxml')

# Getting the closer html
Div = soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')
Lists = Div.find_all('div', {'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col sg-col-12-of-16'})

Lists2 = Div.find_all('div', class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16')

# Writing into csv
file = open(f'{product_name}-info.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(["Sr. No.", "Product Type", "Product Name", "Product URL", "Stars", "Price"])

# Getting the information
try:
    def getInfo(listname, i):
        for index, products in enumerate(listname):
            # Getting the title
            n = products.find('a', class_='a-link-normal a-text-normal')
            names = n.text

            # Getting the ratings
            try:
                s = products.find('div', class_='a-row a-size-small')
                stars = s.find('span')['aria-label'].split('out of')[0]
            except:
                stars = "None"

            # Getting the price
            try:
                price = products.find('span', class_='a-price-whole').get_text().strip()
            except:
                price = "None"

            # Filtering the data and writing it into .csv file
            if stars >= "4.0" and price != "None":
                writer.writerow([index, product_name, names, url, stars, price])

    print("File Saved Successfully!")
except:
    print("An unexpected Error occurred, Sorry!")

getInfo(Lists, len(Lists))
getInfo(Lists2, len(Lists)+len(Lists2))

file.close()