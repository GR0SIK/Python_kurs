from py08052017.samochod import Samochod
from py08052017.silnik import *

# tworzymy instancję klasy SIlnik
t8 = Silnik(2000, 400, "Benzyna + prąd")
print(t8.paliwo)

# tworzymy instancję klasy Samochod
# jako argument silnik - podajemy instancję obiektu Silnik
volvo = Samochod("Volvo", "XC 60", t8)
print("{} {} ma silnik {}".format(volvo.marka, volvo.model, volvo.silnik.V))
print("Silnik Volvo pracuje na:", volvo.silnik.paliwo)

bmw = Samochod("BMW", "3", None)

# tworzymy kolejną instancje klasy Silnik
silnik_bmw = Silnik(3000, 180, "Diesel")

# ten obiekt Silnik przypisujemy do zmiennej instancji
# obiektu bmw
bmw.silnik = silnik_bmw

print("Silnik w BMW ma moc:", bmw.silnik.KM)

# print(volvo)




