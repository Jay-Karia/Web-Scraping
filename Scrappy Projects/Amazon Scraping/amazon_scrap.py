from bs4 import BeautifulSoup
import requests
import csv

print("Enter a product name")
p_name = input()
product_name = p_name.replace(' ', '+')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = f'https://www.amazon.in/s?k={product_name}&ref=nb_sb_noss_2'

source = requests.get(url, headers = headers).text
soup = BeautifulSoup(source, 'lxml')

Div = soup.find('div', class_='s-main-slot s-result-list s-search-results sg-row')

Lists = Div.find_all('div', {'class': 's-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col sg-col-12-of-16'})
Lists2 = Div.find_all('div', class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16')

Lists3 = Div.find_all('div', class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col sg-col-4-of-20')
Lists4 = Div.find_all('div', class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20')

minStars = "None"

def stars():
    global minStars
    print("\nEnter the minimum ratings out of 5.0")
    minStars = input()

while minStars > "5":
    stars()

print("\nEnter the maximum price")
mP = input()
intPrice = int(mP.replace(',', ''))
if ',' not in mP:
    mP = "{:,}".format(intPrice)
    mP = f"{mP}"
maxPrice = int(mP.replace(',', ''))

file = open(f'{p_name}-info.csv', 'w', encoding='UTF-8')
writer = csv.writer(file)
writer.writerow(["Product Type", "Product Name", "Product URL", "Ratings", "Price"])

try:
    def getInfo1(listname):
        for products in listname:
            try:
                names = products.find('span', class_='a-size-medium a-color-base a-text-normal').get_text().strip()
            except:
                names = "None"

            try:
                s = products.find('div', class_='a-row a-size-small')
                stars = s.find('span')['aria-label'].split('out of')[0]
            except:
                stars = "None"

            try:
                price = products.find('span', class_='a-price-whole').get_text().strip()
            except:
                price = "None"

            title = products.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
            u = title.find('a', class_='a-link-normal a-text-normal')['href']
            ur = 'https://www.amazon.in' + u

            priceInt = int(price.replace(',', ''))

            if priceInt < maxPrice:
                if stars > minStars:
                    writer.writerow([p_name, names, ur, stars, price])

    def getInfo2(listname):
        for products in listname:
            try:
                names = products.find('h5', class_='s-line-clamp-1').get_text().strip()
            except:
                try:
                    names = products.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text().strip()
                except:
                    names = "None"

            try:
                title = products.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
                u = title.find('a', class_='a-link-normal a-text-normal')['href']
                ur = 'https://www.amazon.in' + u
            except:
                try:
                    title = products.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-4')
                    u = title = title.find('a', class_='a-link-normal a-text-normal')['href']
                    ur = 'https://www.amazon.in' + u
                except:
                    title = "None"
                    u = "None"
                    ur = "None"

            try:
                s = products.find('div', class_='a-row a-size-small')
                stars = s.find('span')['aria-label'].split('out of')[0]
            except:
                stars = "None"

            try:
                price = products.find('span', class_='a-price-whole').get_text().strip()
            except:
                price = "None"

            priceInt = int(price.replace(',', '').replace('None', '0'))

            if priceInt < maxPrice:
                if stars > minStars:
                    writer.writerow([p_name, names, ur, stars, price])

    print("File Saved Successfully!")
except:
    print("An unexpected Error occurred, Sorry!")

getInfo1(Lists)
getInfo1(Lists2)

getInfo2(Lists3)
getInfo2(Lists4)

file.close()