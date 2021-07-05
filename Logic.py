import shelve
from random import choice
import scraper
from PyQt5 import QtWidgets

message = ""
def AddCityInDb(city):
    if scraper.CheckCityOrNot(city) == "По вашему запросу ничего не найдено":
        return 0
    db = shelve.open("dbOfWordsGame")
    firstElem = city[0]
    if firstElem in db.keys():
        a = db[firstElem]
        if city not in a:
            a.append(city)
            db[firstElem] = a
    else:
        a = [city]
        db[firstElem] = a
    db.close()
    return 1


def ChoseCity(citiesDb, cityOfPlayer):
    lastElem = cityOfPlayer[-1].upper()
    if lastElem in ["ъ", "ь", "ы"]:
        ChoseCity(cityOfPlayer[0:(len(cityOfPlayer)-1)])
    else:
        return choice(citiesDb[lastElem])
def CheckRules(usedCities, cityOfPlayer, chosedCity):
    global message
    if chosedCity[-1] in ["ъ","ь","ы"]:
        if cityOfPlayer[0] != chosedCity[-2].upper():
            message = "Твой город не на букву " + chosedCity[-1].upper()
            return 1
        elif cityOfPlayer in usedCities:
            message = "Этот город уже был"
            return 1
        else:
            return 0
    else:
        if cityOfPlayer[0] != chosedCity[-1].upper():
            print("Твой город не на букву", chosedCity[-1].upper())
            return 1
        elif cityOfPlayer in usedCities:
            print("Этот город уже был")
            return 1
        else:
            return 0

def ShowMessage(chosedCity):
    message = chosedCity
    if chosedCity[-1] in ["ь","ъ","ы"]:
        message += "\nТвой ход, тебе на " + chosedCity[-2].upper()
        return message
    else:
        message += "\nТвой ход, тебе на " + chosedCity[-1].upper()
        return message

def FirstStepOfGame(citiesDb, usedCities, cityOfPlayer):
    if (cityOfPlayer not in citiesDb) and (not AddCityInDb(cityOfPlayer)):
        return "Кажется, такого города не существует, назови другой"

    try:
        chosedCity = ChoseCity(citiesDb, cityOfPlayer)
    except Exception:
        return "Я больше не знаю городов, ты выйграл"

    citiesDb[chosedCity[0]].remove(chosedCity)
    usedCities.extend([chosedCity, cityOfPlayer])

    ShowMessage(chosedCity)
def MainOfGame(citiesDb, usedCities,chosedCity, cityOfPlayer):
    if CheckRules(usedCities, cityOfPlayer, chosedCity):
        return message
    if cityOfPlayer not in citiesDb:
        if not AddCityInDb(cityOfPlayer):
            return "Кажется, такого города не существует, назови другой"

    try:
        chosedCity = ChoseCity(citiesDb, cityOfPlayer)
    except Exception:
        return "Я больше не знаю городов, ты выйграл"

    citiesDb[chosedCity[0]].remove(chosedCity)
    usedCities.extend([chosedCity, cityOfPlayer])

    ShowMessage(chosedCity)

def Game(firstCity):
    citiesDb = shelve.open("dbOfWordsGame")
    usedCities = []
    chosedCity = ""
    print("Я даю тебе фору, начинай")
    MainOfGame(citiesDb, usedCities, chosedCity, firstCity)
    citiesDb.close()
#Я закончил на изменении метода MainOfGame()