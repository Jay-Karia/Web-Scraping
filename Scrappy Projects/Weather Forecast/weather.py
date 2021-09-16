from bs4 import BeautifulSoup
import requests
import csv

# Getting the place from user
print("Enter the place")
place = input()

# Getting the place
url = f'https://www.google.com/search?q=weather+of+{place}'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')