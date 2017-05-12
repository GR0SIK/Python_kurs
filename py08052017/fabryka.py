from py08052017.samochod2 import *

# tworzymy instancję klasy Samochód
# inaczej - tworzymy obiekt typu Samochod
auto1 = Samochod("Toyota", "Yaris", "Niebieska")

# wypisujemy pola (zmienne) specyficzne dla tej instancji
print(auto1.marka)
print(auto1.model)
print(auto1.color)

print(auto1.silnik)
auto1.silnik = "1.0 90 KM"
print(auto1.silnik)

# pole il_drzwi nie jest zdefiniowane w klasie
# będzie więc ono tylko w tej instancji
# nie będzie jego w żadnej innej instancji (chyba, że w niej zdeklarujemy)
auto1.il_drzwi = 3
print(auto1.il_drzwi)

# auto1.jedz()
# print(auto1.czy_jedzie)
#
auto2 = Samochod("Volvo", "XC60 nowe", "Dark Grey")
# print(auto2.marka)
# print(auto2.model)
# print(auto2.color)
# auto2.jedz()
#
# auto1.zatrzymaj()
# print(auto1.czy_jedzie)


# print(auto2.il_drzwi)