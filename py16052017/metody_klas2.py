class Pracownik(object):
#   wspolne dla wszystkich instancji
    roczna_podw = 5
    ilosc_pracownikow = 0

    def __init__(self, imie, stanowisko):
#       self - zmienna klasy
        self.imie = imie
        self.stanowisko = stanowisko
        self.wynagrodzenie = None
        Pracownik.ilosc_pracownikow +=1

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (1/procent)

    def __del__(self):
        Pracownik.ilosc_pracownikow -= 1

    def __str__(self):
        return "{} - {} ma wynagrodzenie: {}".format(self.imie, self.stanowisko, self.wynagrodzenie)

emp1 = Pracownik("Jhon Turturo", "aktor")
emp1.ustaw_pensje(5000)
print("Ilość pracowników", Pracownik.ilosc_pracownikow)
emp2 = Pracownik("Jhon Travolta", "gwiazda")
print("Ilość pracowników", Pracownik.ilosc_pracownikow)
emp2.ustaw_pensje(8000)
print(emp1)
print(emp2)

print()

print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)

print()

Pracownik.roczna_podw = 8

print()

print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)

print()

emp2.roczna_podw = 12

print()

print(Pracownik.roczna_podw)
print(emp1.roczna_podw)
print(emp2.roczna_podw)

print()
del emp2
print("Ilość pracowników", Pracownik.ilosc_pracownikow)
# print(emp1.__dict__)
# print(emp2.__dict__)

