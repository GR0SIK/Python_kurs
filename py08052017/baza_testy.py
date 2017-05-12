from py08052017.osoba import *
baza = []

# tworzymy instancję obiektu Osoba
# przechowujemy ją w zmiennej os1
os1 = Osoba("Adam", "Kowalski", 230948230239)

# korzystamy z metody zdefiniowanej w klasie Osoba
os1.wypisz()
# wypisujemy zmienną instancji pesel
print(os1.pesel)

os2 = Osoba("Jan", "Matejko", 38472364283)
os3 = Osoba("Janina", "Nowak", 846823762823)
os2.wypisz()
os3.wypisz()
print(os1.spr_pesel())

baza.append(os1)
baza.append(os2)
baza.append(os3)

print(baza)

for o in baza:
    # Wszystkie obiekty są typu Osoba
    # mają więc pole imie, możemy więc
    # ze wszystkich wydobyć ich zawartość
    print(o.imie)
