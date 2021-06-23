import requests
from bs4 import BeautifulSoup

def CheckCityOrNot(cityOfPlayer):
    url = "https://geogoroda.ru/search/node/"+cityOfPlayer
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup.find_all("h2")[1].text



