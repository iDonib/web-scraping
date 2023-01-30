import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/BTC-USD/history?period1=1262300800&period2=1609459200&interval=1d&filter=history&frequency=1d"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'W(100%) M(0)'})
rows = table.find_all('tr')

for row in rows:
    date = row.find_all('td')[0].text
    close_price = row.find_all('td')[4].text
    print(date, close_price)

