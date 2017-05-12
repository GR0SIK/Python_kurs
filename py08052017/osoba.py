class Osoba(object):
    '''Definiuje informacje o osobach'''

    def __init__(self, imie, nazwisko, pesel):
        '''Inicjalizuje instancję klasy Osoba'''
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = None
        self.plec = None

        if len(str(pesel)) == 11:
            self.pesel = pesel
        else:
            print("Pesel musi mieć 11 znaków")
            self.pesel = None

    def wypisz(self):
        """Wypisuje informacje o osobie"""
        print(self.imie, self.nazwisko)

    def spr_pesel(self):
        """Sprawdza czy pesel osoby jest odpowiedniej długości"""
        if len(str(self.pesel)) == 11:
            return True
        return False