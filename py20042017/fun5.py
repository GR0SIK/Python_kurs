# mozemy miec kilka argumentow wymaganych i domyslnych

def wypisz_dane(imie, nazwisko, kurs="Python", ilosc_dni = 15):
    print(imie, nazwisko, kurs, ilosc_dni)

wypisz_dane("Grzegorz", "Kowalski")
wypisz_dane("Grzegorz", "Kowalski", "PHP")
wypisz_dane("Grzegorz", "Kowalski", "PHP", 54)
wypisz_dane("Anna", "Nowak", ilosc_dni=12)


