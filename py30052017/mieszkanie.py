from py30052017.ogloszenia import Ogloszenie
from bs4 import BeautifulSoup
import requests

adres = "https://www.otodom.pl/sprzedaz/mieszkanie/gdansk/?search%5Bdist%5D=5&search%5Bdistrict_id%5D=41523&search%5Bsubregion_id%5D=439&search%5Bcity_id%5D=40"

response = requests.get(adres)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

# print(response.text)

ads = soup.select(".offer-item-header a")

for ad in ads:
#    print(ad)
#    print(ad.getText())
#    print(ad.get('href'))
#    print("------\n")
    o = Ogloszenie(ad.getText(), ad.get('href'))
#    print(o.opis)

Ogloszenie.zapisz_ogloszenia('ogloszenia.dat')
