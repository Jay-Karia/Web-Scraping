# Importing required modules
from bs4 import BeautifulSoup
import requests
import csv

# Getting the product name
print("Enter a product name")
product_name = input()

# Getting the page
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = f'https://www.amazon.in/s?k={product_name}&ref=nb_sb_noss_2'

source = requests.get(url, headers = headers).text
soup = BeautifulSoup(source, 'lxml')

# Getting the closer html
Div = soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')

# Getting the custom filters from the user
print("\nEnter the minimum stars out of 5.0")
minStars = input()

print("\nEnter the maximum price")
maxPrice = input()

# Creating a csv file
file = open(f'{product_name}-info.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(["Product Type", "Product Name", "Product URL", "Stars", "Price"])

# Getting the information
try:
    def getInfo(listname):
        for products in listname:
            # Getting the product title
            names = products.find('span', class_='a-size-medium a-color-base a-text-normal').get_text().strip()

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

            # Getting the url of the product
            title = products.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
            u = title.find('a', class_='a-link-normal a-text-normal')['href']
            ur = 'https://www.amazon.in' + u

            # Filtering the data and writing it into csv file
            # if stars >= minStars:
            if price <= maxPrice:
                writer.writerow([product_name, names, ur, stars, price])

    def getInfo2(listname):
        for products in listname:
            n = products.find('h5', class_='s-line-clamp-1')
            names = n.find('span', class_='a-size-base-plus a-color-base').get_text().strip()

            title = products.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
            u = title.find('a', class_='a-link-normal a-text-normal')['href']
            ur = 'https://www.amazon.in' + u

            try:
                s = products.find('div', class_='a-row a-size-small')
                stars = s.find('span')['aria-label'].split('out of')[0]
            except:
                stars = "None"

            writer.writerow([product_name, names, ur, stars])

    print("File Saved Successfully!")
except:
    print("An unexpected Error occurred, Sorry!")

# try:
Lists = Div.find_all('div', {'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col sg-col-12-of-16'})
Lists2 = Div.find_all('div', class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16')
getInfo(Lists)
getInfo(Lists2)
# except:
Lists3 = Div.find_all('div', class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col sg-col-4-of-20')
Lists4 = Div.find_all('div', class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20')
getInfo2(Lists3)
getInfo2(Lists4)

file.close()
