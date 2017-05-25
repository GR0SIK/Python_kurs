import requests

#odpowiedz = requests.get("http://gdansk.pl")
#print(odpowiedz.status_code)

obrazek = "http://rozklad-pkp.pl/files/files/936/medium/tablica_rozklad_polecamy.jpg"

odpowiedz = requests.get(obrazek)
#print(odpowiedz.status_code)
# wb - oznacza write binarnie
with open("pliczek.jpg", "wb") as plik:
    for kawalek in odpowiedz.iter_content(100000):
        bajty = plik.write(kawalek)
        print(bajty)

