import requests
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
response = requests.get(wiki)
# print(page.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
print(soup.title.string)
W