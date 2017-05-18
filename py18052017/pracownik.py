class Pracownik(object):

# __ prywatna zmiena

    liczba_pracownikow = 0
    roczna_podwyzka = 5

    def __init__(self, imie, nazwisko):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__stanowisko = None
        self.__wynagrodzenie = None
        Pracownik.liczba_pracownikow += 1
# bez metody która oddaje imie nie bedzie widoczny w instancji
    def wypisz_imie(self):
        """Wypisuje imie pracownika"""
        print(self.__imie)

    def oblicz_podwyzke(self):
        return self.__wynagrodzenie * (Pracownik.roczna_podwyzka / 100)

    @property
    def stanowisko(self):
        if self.__stanowisko is not None:
            return self.__stanowisko.capitalize()
        else:
            return "Nieokreślone"



    @stanowisko.setter
    def stanowisko(self, nazwa):
        if str(nazwa).isalpha():
            self.__stanowisko = nazwa

    @property
    def pensja(self):
        return self.__wynagrodzenie

    @pensja.setter
    def pensja(self, kwota):
        if kwota <= 10000:
            self.__wynagrodzenie = kwota
        else:
            self.__wynagrodzenie = 10000

    def __del__(self):
        Pracownik.liczba_pracownikow -= 1
        print("Liczba pracowników: ", Pracownik.liczba_pracownikow)
    def __str__(self):
        return "{} {] stanowisko: {}".format(self.__imie, self.__nazwisko, self.__stanowisko)

