from py18052017.pracownik import Pracownik


prac1 = Pracownik("Jan", "Kowalski")

prac1.wypisz_imie()

print(prac1.stanowisko)

prac1.stanowisko = "mechanik"

print(prac1.stanowisko)

prac1.pensja = 16000
print("Mechanik zarabia {}".format(prac1.pensja))