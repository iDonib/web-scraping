import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "http://books.toscrape.com/index.html"
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the book elements on the page
books = soup.find_all("article", class_="product_pod")

# Iterate through the books and print their details
for book in books:
    title = book.h3.a["title"]
    price = book.select(".price_color")[0].get_text()
    availability = book.select(".availability")[0].get_text().strip()
    print("Title:", title)
    print("Price:", price)
    print("Availability:", availability)

