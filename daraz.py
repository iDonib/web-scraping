import requests
from bs4 import BeautifulSoup

url = "https://www.daraz.com.np/laptops/?min_price=100000"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', class_='product-card')
for product in products:
    name = product.find('a', class_='title').text
    price = product.find('span', class_='price').text
    if int(price.replace(',',''))>100000:
        print(name + ': ' + price)
