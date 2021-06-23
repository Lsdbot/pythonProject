import shelve
import random

def AddCityInDb(city):
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

def LoadDbInProgramm():
    db = shelve.open("dbOfWordsGame")
    return db

def ChoseCity(cityOfPlayer):
    lastElem = cityOfPlayer[-1].upper()
    if lastElem in ["ъ", "ь", "ы"]:
        ChoseCity(cityOfPlayer[0:(len(cityOfPlayer)-1)])
    else:
        return random.choice(citiesDb[lastElem])
def CheckCityOfPlayer(cityOfPlayer, chosedCity):
    if chosedCity[-1].upper() in ["ъ","ь","ы"]:
        if cityOfPlayer[0] != chosedCity[-2].upper():
            print("Твой город не на букву", chosedCity[-1].upper())
            return 1
        elif cityOfPlayer in usedCities:
            print("Этот город уже был")
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

citiesDb = LoadDbInProgramm()
usedCities = []
chosedCity = ""

print("Я даю тебе фору, начинай")

cityOfPlayer = input()
while cityOfPlayer.find("хватит") == -1:
    if chosedCity:
        if CheckCityOfPlayer(cityOfPlayer, chosedCity):
            cityOfPlayer = input()
            continue
    AddCityInDb(cityOfPlayer)
    try:
        chosedCity = ChoseCity(cityOfPlayer)
    except Exception:
        print("Я больше не знаю городов, ты выйграл")
        break
    citiesDb[chosedCity[0]].remove(chosedCity)
    usedCities.extend([chosedCity, cityOfPlayer])

    print(chosedCity)
    print("Твой ход, тебе на", chosedCity[-1].upper())
    cityOfPlayer = input()
citiesDb.close()
