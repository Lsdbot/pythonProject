import requests
from bs4 import BeautifulSoup

url = "https://geogoroda.ru/search/node/Алаберды"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")


print(soup)